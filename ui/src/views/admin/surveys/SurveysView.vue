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
                  <v-col
                    cols="9"
                    class="mb-2"
                  >
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
                  <v-col
                    cols="3"
                    class="text-right"
                  >
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
                            {{ survey.startDate }}
                          </span>
                        </v-col>
                        <v-col cols="auto">
                          <span class="text-xs-right">
                            {{ survey.lastUpdatedDate }}
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
                    {{ item.lastUpdatedDate }}
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
import { adminListSurveys, adminDeleteSurvey } from "@api";
import { convertToStandardDate, isTodayAfterGivenDate } from "@util/dates.js";

export default {
  name: "AdminSurveysView",
  data() {
    return {
      keyword: "",
      isSortedAscending: true,
      isDeleteItemModalShown: false,
      selectedSurvey: {},
      surveys: []
    };
  },
  computed: {
    ...get("user", [ "userData" ]),
    ...sync("app", [ "mini" ]),
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
        { text: "Last update", value: "lastUpdatedDate" },
        { text: "Name", value: "title" },
        { text: "Status", value: "status" },
        { text: "Owner", value: "owner" },
        { text: "Start date", value: "startDate" },
        { text: "Actions", value: "id" }
      ];
    }
  },
  created() {
    this.getSurveysApi();
    this.processSurveyData();
  },
  mounted() {},
  methods: {
    onClickItemDelete(item) {
      this.selectedSurvey = { ...item };
      this.isDeleteItemModalShown = true;
    },
    onDeleteConfirmation() {
      const apiData = { id: this.selectedSurvey.id };
      adminDeleteSurvey(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getSurveysApi();
        this.processSurveyData();
      });
      this.isDeleteItemModalShown = false;
      this.isDeleteItemModalShown = false;
    },
    processSurveyData() {
      this.surveys = this.surveys.map((survey, index) => {
        return {
          ...survey,
          ...{
            index
          }
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
    getSurveysApi() {
      adminListSurveys()
        .then((response) => {
          this.surveys.length = 0;
          const rawSurveys = response["surveys"];
          const rawSurveyIds = Object.keys(rawSurveys);
          rawSurveyIds.forEach(rawSurveyId => {
            const respDateTimeFormat = "ddd, DD MMM YYYY hh:mm:ss zz";
            let rawSurveyStatus = 1;
            if( isTodayAfterGivenDate(rawSurveys[rawSurveyId]["startDate"], respDateTimeFormat) ) {
              rawSurveyStatus = 2;
            }
            const rawSurveyStartDateMoment = convertToStandardDate(rawSurveys[rawSurveyId]["startDate"], respDateTimeFormat);
            const rawSurveyModificationDateMoment = convertToStandardDate(rawSurveys[rawSurveyId]["modificationDate"], respDateTimeFormat);
            let rawSurvey = {
              id: rawSurveyId,
              owner: rawSurveys[rawSurveyId]["surveyOwner"],
              title: rawSurveys[rawSurveyId]["title"],
              startDate: rawSurveyStartDateMoment,
              status: rawSurveyStatus,
              lastUpdatedDate: rawSurveyModificationDateMoment
            };
            this.surveys.push(rawSurvey);
          });
        });
    }
  }
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
