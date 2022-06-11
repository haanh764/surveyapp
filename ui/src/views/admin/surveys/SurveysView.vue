<template>
  <v-container
    id="admin-surveys-view"
    class="admin-surveys-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 10">
        <v-card
          class="admin-surveys-card text-center"
          elevation="2"
          :class="{'--is-mobile': isMobile, '--is-desktop': !isMobile}"
        >
          <v-row justify="center">
            <v-col cols="12">
              <!-- SURVEYS DATATABLE STARTS HERE : MOBILE -->
              <template v-if="isMobile">
                <v-row justify="center">
                  <v-col cols="9" class="mb-2">
                    <v-text-field
                      v-model.trim="keyword"
                      solo
                      dense
                      height="48"
                      class="admin-surveys-search"
                      label="Search survey by name"
                      append-icon="mdi-magnify"
                    />
                    <p class="text-left text-secondary">
                      {{ surveys.length }} surveys
                    </p>
                  </v-col>
                  <v-col cols="3" class="text-right">
                    <v-btn
                      text
                      icon
                      elevation="2"
                      height="48"
                      width="48"
                      class="v-btn--default"
                      @click="isSortedAscending = !isSortedAscending"
                    >
                      <v-icon>
                        {{ isSortedAscending ? 'mdi-sort-alphabetical-ascending' : 'mdi-sort-alphabetical-descending' }}
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
                <v-list>
                  <v-list-item
                    v-for="survey in filteredSurveys"
                    :key="survey.id"
                    cols="12"
                    class="pa-0"
                  >
                    <v-list-item-content class="pa-2 pb-4">
                      <v-row justify="space-between">
                        <v-col
                          cols="auto"
                          align-self="start"
                        >
                          <h2 class="mb-1">
                            {{ survey.title }}
                          </h2>
                          <span class="text-secondary">
                            {{ survey.responses }} responses received
                          </span>
                        </v-col>
                        <v-col cols="auto">
                          <span class="text-xs-right">
                            {{ survey.lastUpdatedDate | standardDate }}
                          </span>
                        </v-col>
                      </v-row>
                      <v-divider />
                    </v-list-item-content>
                  </v-list-item>
                </v-list>
              </template>
              <!-- SURVEYS DATATABLE ENDS HERE : MOBILE -->
              <!-- SURVEYS DATATABLE STARTS HERE : DESKTOP -->
              <template v-else>
                <v-row
                  justify="start"
                  class="mb-2"
                >
                  <v-col
                    cols="7"
                    class="text-left"
                  >
                    <h1>
                      Surveys
                    </h1>
                  </v-col>
                </v-row>
                <v-data-table
                  :headers="tableHeaders"
                  :items="filteredSurveys"
                  item-key="name"
                  class="elevation-1 admin-surveys-table"
                  :search="keyword"
                >
                  <template #top>
                    <v-row
                      justify="start"
                      class="admin-surveys-table__top"
                    >
                      <v-col cols="auto">
                        <v-text-field
                          v-model.trim="keyword"
                          solo
                          dense
                          class="admin-surveys-search --is-desktop"
                          prepend-inner-icon="mdi-magnify"
                          label="Search survey by name"
                        />
                      </v-col>
                    </v-row>
                  </template>
                  <template #item.lastUpdatedDate="{ item }">
                    {{ item.lastUpdatedDate | standardDate }}
                  </template>
                  <template #item.status="{ item }">
                    <v-chip
                      small
                      :color="getItemStatus(item.status).color"
                      :text-color="getItemStatus(item.status).textColor"
                    >
                      {{ getItemStatus(item.status).text }}
                    </v-chip>
                  </template>
                  <template #item.id="{item}">
                    <v-row justify="space-between">
                      <v-col cols="12">
                        <v-btn
                          text
                          icon
                          elevation="1"
                          small
                          class="v-btn--default"
                          @click="onClickItemDelete(item)"
                        >
                          <v-icon small>
                            mdi-delete
                          </v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                  </template>
                </v-data-table>
              </template>
              <!-- SURVEYS DATATABLE ENDS HERE : DESKTOP -->
            </v-col>
          </v-row>
        </v-card>

        <modal
          v-model="isDeleteItemModalShown"
          name="delete-modal"
          title="Delete Survey"
          content="Are you sure you want to delete this survey? This action cannot be undone."
          primary-action-button-text="OK"
          @click:primary-action="onDeleteConfirmation"
        />

      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { get, sync } from "vuex-pathify";
import { getSurveys } from "@api";

export default {
  name: "AdminSurveysView",
  data() {
    return {
      keyword: "",
      isSortedAscending: true,
      isDeleteItemModalShown: false,
      selectedSurvey: {},
      surveys: [
        {
          id: 1,
          owner: "sadBoy123@wroclaw.pl",
          title: "Earnings 2022",
          responses: 10,
          status: 1,
          lastUpdatedDate: "01/02/2022 08:00:00",
        },
        {
          id: 2,
          owner: "happyGirl456@wroclaw.pl",
          title: "Chicken 2022",
          responses: 11,
          status: 2,
          lastUpdatedDate: "09/08/2022 08:00:00",
        },
      ],
    };
  },
  computed: {
    ...get("user", ["userData"]),
    ...sync("app", ["mini"]),
    filteredSurveys() {
      let surveys = this.keyword
        ? this.surveys.filter((survey) => {
            return survey.title.toLowerCase().includes(this.keyword);
          })
        : this.surveys;
      return surveys.sort((a, b) => {
        return this.isSortedAscending
          ? a.title.localeCompare(b.title)
          : b.title.localeCompare(a.title);
      });
    },
    tableHeaders() {
      return [
        { text: "Survey name", value: "title" },
        { text: "Owner", value: "owner" },
        { text: "Last updated at", value: "lastUpdatedDate" },
        { text: "Status", value: "status" },
        { text: "Responses", value: "responses" },
        { text: "Actions", value: "id" },
      ];
    },
  },
  created() {
    // get survey api
    // add certain columns to survey data
    this.processSurveyData();
  },
  mounted() {},
  methods: {
    onDeleteConfirmation() {
      // call delete api
      // delete
      // refresh table
      // hide modal
      this.isDeleteItemModalShown = false;
    },
    onClickItemDelete(item) {
      this.selectedSurvey = { ...item };
      this.isDeleteItemModalShown = true;
    },
    processSurveyData() {
      this.surveys = this.surveys.map((survey, index) => {
        return {
          ...survey,
          ...{
            index,
          },
        };
      });
    },
    getItemStatus(itemStatus) {
      let item = {};
      switch (itemStatus) {
        case 1:
          item = { color: "#bb86fc1f", text: "Draft", textColor: "primary" };
          break;
        case 2:
          item = { color: "#e1fcef", text: "Published", textColor: "success" };
          break;
        default:
          item = { color: "default", text: "Unknown" };
          break;
      }
      return item;
    },
    getSurveyApi() {
      // example of fetching api directly with fetch
      fetch("http://localhost:8000")
        .then((response) => response.json())
        .then((data) => {
          this.message = data.message;
        })
        .catch((error) => {
          console.log(error);
        });

      // example 1 with axios
      this.$axios
        .get("https://api.coindesk.com/v1/bpi/currentprice.json")
        .then((response) => {
          if (response.status == 200) {
            // do something
          } else {
            // error
            // do something
          }
        })
        .catch((error) => {
          // do something on error
          console.error(error);
        });

      // example 2
      // recommended because this way the api is centered in one place/file
      // dont forget to handle errors
      getSurveys()
        .then((response) => {
          console.log(response);
          // do something with the response
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>
<style lang="scss">
.admin-surveys-view {
  margin: 20px 0;

  &.--no-padding {
    *[class~="col"] {
      padding: 0;
    }
  }
}

.admin-surveys-card {
  padding: 20px 0 40px;

  &.--is-mobile {
    box-shadow: none !important;
  }

  &.--is-desktop {
    box-shadow: none !important;
    background: none !important;
  }
}

.admin-surveys-table {
  &__top {
    background-color: $light-blue;
    margin: 0;
    overflow: hidden;
  }

  .v-data-table-header {
    background-color: $light-blue;

    th[role="columnheader"] {
      text-transform: uppercase;

      > span {
        font-weight: 600;
      }
    }
  }
}

.admin-surveys-search {
  &.--is-desktop {
    .v-input__slot {
      box-shadow: none !important;
      border: 1px solid $light-gray;
    }
  }
}
</style>
