<template>
  <v-container
    id="user-surveys-view"
    class="user-surveys-view"
    :class="{
      '--no-padding':
        isMobile && (isPrivacyPolicyModalShown || isTnCModalShown),
    }"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile ? 12 : 10">
        <v-card
          class="user-surveys-card text-center"
          elevation="2"
          :class="{ '--is-mobile': isMobile, '--is-desktop': !isMobile }"
        >
          <v-row justify="center">
            <v-col cols="12">
              <template
                v-if="
                  isMobile && (isPrivacyPolicyModalShown || isTnCModalShown)
                "
              >
                <template v-if="isPrivacyPolicyModalShown">
                  <conditions-interaction
                    title="Privacy Policy"
                    link="http://www.google.com"
                    :content="privacyPolicyContent"
                    @confirm="onConfirmPrivacyPolicy"
                  />
                </template>
                <template v-else-if="isTnCModalShown">
                  <conditions-interaction
                    title="Terms and Conditions"
                    link="http://www.google.com"
                    :content="tnCContent"
                    @confirm="onConfirmTnC"
                  />
                </template>
              </template>
              <template v-else>
                <template v-if="!hasAcceptedConditions">
                  <center>
                    <v-img
                      :src="require('@assets/svg/man-filling-form.svg')"
                      :max-height="isMobile ? 220 : 420"
                      :max-width="isMobile ? 320 : 600"
                    />
                  </center>
                  <h1 class="mb-2">This feature is currently disabled</h1>
                  <p class="text-secondary">
                    You cannot use our services until you have accepted our
                    Terms and Conditions and Privacy Policy.
                  </p>
                  <v-btn
                    v-show="!hasAcceptedTnC"
                    block
                    class="
                      text-capitalize
                      v-btn--default
                      mb-5
                      surveys-view__tnc-button
                    "
                    height="53"
                    @click="isTnCModalShown = true"
                  >
                    Review Terms and Conditions
                  </v-btn>
                  <v-btn
                    v-show="!hasAcceptedPrivacyPolicy"
                    block
                    class="v-btn--default mb-5 surveys-view__privacy-button"
                    height="53"
                    @click="isPrivacyPolicyModalShown = true"
                  >
                    Review Privacy Policy
                  </v-btn>
                </template>
                <template v-else-if="hasAcceptedConditions && !surveys.length">
                  <center class="mb-2">
                    <v-img
                      :src="require('@assets/svg/man-filling-form.svg')"
                      :max-height="isMobile ? 220 : 420"
                      :max-width="isMobile ? 320 : 600"
                    />
                  </center>
                  <h1 class="mb-2">Reach your respondents</h1>
                  <p class="text-secondary">
                    Save a draft survey and it will show up in here
                  </p>
                  <v-btn
                    :block="isMobile"
                    height="53"
                    :width="isMobile ? undefined : 600"
                    :disabled="surveys.length >= 20"
                    class="v-btn--accent surveys-view__create-button"
                    @click="createSurvey"
                  >
                    <v-icon class="pr-1"> mdi-plus </v-icon>
                    CREATE SURVEY
                  </v-btn>
                </template>
                <template v-else>
                  <template v-if="isMobile">
                    <v-row justify="center">
                      <v-col cols="12" class="mb-2">
                        <v-btn
                          block
                          height="53"
                          :disabled="surveys.length >= 20"
                          class="v-btn--accent surveys-view__create-button"
                          @click="createSurvey"
                        >
                          <v-icon class="pr-1"> mdi-plus </v-icon>
                          CREATE SURVEY
                        </v-btn>
                      </v-col>
                      <v-col cols="9">
                        <v-text-field
                          v-model.trim="keyword"
                          solo
                          dense
                          height="48"
                          class="user-surveys-search"
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
                            {{
                              isSortedAscending
                                ? "mdi-sort-alphabetical-ascending"
                                : "mdi-sort-alphabetical-descending"
                            }}
                          </v-icon>
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-list class="user-surveys-list">
                      <v-list-item
                        v-for="survey in filteredSurveys"
                        :key="survey.id"
                        cols="12"
                        class="pa-0 user-surveys-list__item"
                        @click="onClickSurveyListItem(survey)"
                      >
                        <v-list-item-content class="pa-2 pb-4">
                          <v-row justify="space-between">
                            <v-col cols="auto" align-self="start">
                              <h2 class="mb-1">
                                {{ survey.title }}
                              </h2>
                              <span class="text-secondary">
                                {{ survey.startDate }}
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
                  <template v-else>
                    <v-row justify="start" class="mb-2">
                      <v-col cols="7" class="text-left">
                        <h1>My Surveys</h1>
                        <p>
                          {{
                            surveys.length == 20
                              ? `Maximum ${surveys.length} surveys reached`
                              : `${surveys.length} surveys`
                          }}
                        </p>
                      </v-col>
                      <v-col cols="5">
                        <v-btn
                          block
                          height="53"
                          :disabled="surveys.length >= 20"
                          class="v-btn--accent surveys-view__create-button"
                          @click="createSurvey"
                        >
                          <v-icon class="pr-1"> mdi-plus </v-icon>
                          CREATE SURVEY
                        </v-btn>
                      </v-col>
                    </v-row>
                    <v-data-table
                      :headers="tableHeaders"
                      :items="filteredSurveys"
                      item-key="name"
                      class="elevation-1 user-surveys-table"
                      :search="keyword"
                      @dblclick:row="onClickTableRowItem"
                    >
                      <template #top>
                        <v-row justify="start" class="user-surveys-table__top">
                          <!-- not defined in requirements but shown in design -->
                          <!-- <v-col cols="1">
                            <v-btn
                              text
                              icon
                              class="v-btn--default"
                            >
                              <v-icon>
                                mdi-filter
                              </v-icon>
                            </v-btn>
                          </v-col> -->
                          <v-col cols="auto">
                            <v-text-field
                              v-model.trim="keyword"
                              solo
                              dense
                              class="user-surveys-search --is-desktop"
                              prepend-inner-icon="mdi-magnify"
                              label="Search survey by name"
                            />
                          </v-col>
                        </v-row>
                      </template>
                      <template #item.index="{ item, index }">
                        {{ index + 1 }}
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
                      <template #item.id="{ item }">
                        <v-row justify="space-between">
                          <v-col cols="12">
                            <v-btn
                              text
                              icon
                              elevation="1"
                              small
                              class="
                                v-btn--default
                                mr-2
                                surveys-view__edit-button
                              "
                              @click="onClickItemEdit(item)"
                            >
                              <v-icon small> mdi-pencil </v-icon>
                            </v-btn>

                            <v-btn
                              text
                              icon
                              elevation="1"
                              small
                              class="v-btn--default surveys-view__delete-button"
                              @click="onClickItemDelete(item)"
                            >
                              <v-icon small> mdi-delete </v-icon>
                            </v-btn>
                          </v-col>
                        </v-row>
                      </template>
                    </v-data-table>
                  </template>
                </template>
              </template>
            </v-col>
          </v-row>
        </v-card>

        <template v-if="!isMobile">
          <modal
            v-if="isPrivacyPolicyModalShown"
            v-model="isPrivacyPolicyModalShown"
            name="privacy-policy-modal"
            :is-close-button-shown="false"
            :is-footer-shown="false"
          >
            <conditions-interaction
              title="Privacy Policy"
              link="http://www.google.com"
              :content="privacyPolicyContent"
              @confirm="onConfirmPrivacyPolicy"
            />
          </modal>
          <modal
            v-if="isTnCModalShown"
            v-model="isTnCModalShown"
            name="tnc-modal"
            :is-close-button-shown="false"
            :is-footer-shown="false"
          >
            <conditions-interaction
              title="Terms and Conditions"
              link="http://www.google.com"
              :content="tnCContent"
              @confirm="onConfirmTnC"
            />
          </modal>
          <modal
            v-if="isDeleteItemModalShown"
            v-model="isDeleteItemModalShown"
            name="delete-modal"
            title="Delete"
            content="Are you sure you want to delete this item? This action cannot be undone."
            primary-action-button-text="OK"
            @click:primary-action="onDeleteConfirmation"
          />
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { get, sync } from "vuex-pathify";
import { mapGetters } from "vuex";
import { userListSurveys, userDeleteSurvey } from "@api";
import { convertToStandardDate } from "@util/dates.js";
import tnc from "@assets/json/tnc.json";
import pp from "@assets/json/pp.json";

export default {
  name: "UserSurveysView",
  components: {
    ConditionsInteraction: () =>
      import(
        /* webpackChunkName: "conditions-interaction" */
        "./components/ConditionsInteraction"
      ),
  },
  data() {
    return {
      keyword: "",
      isSortedAscending: true,
      isPrivacyPolicyModalShown: false,
      isTnCModalShown: false,
      isDeleteItemModalShown: false,
      selectedSurvey: {},
      privacyPolicyContent: pp.long,
      tnCContent: tnc.long,
      surveys: []
    };
  },
  computed: {
    ...get("user", ["userData"]),
    ...sync("app", ["mini"]),
    ...mapGetters("user", ["hasAcceptedPrivacyPolicy", "hasAcceptedTnC"]),
    hasAcceptedConditions() {
      return this.hasAcceptedPrivacyPolicy && this.hasAcceptedTnC;
    },
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
        { text: "#", value: "index" },
        { text: "Last updated at", value: "lastUpdatedDate" },
        { text: "Survey name", value: "title" },
        { text: "Status", value: "status" },
        { text: "Start date", value: "startDate" },
        { text: "Actions", value: "id" },
      ];
    },
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
      userDeleteSurvey(apiData).then((response) => {
        this.$notify.toast(response["message"]);
        this.getSurveysApi();
        this.processSurveyData();
      });
      this.isDeleteItemModalShown = false;
    },
    onClickItemEdit(item) {
      this.$router.push(`/user/surveys/${item.id}/edit`);
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
    onClickTableRowItem(event, { item }) {
      this.$router.push(`/user/surveys/${item.id}`);
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
    createSurvey() {
      this.$router.push("/user/surveys/new/edit");
    },
    onClickSurveyListItem(survey) {
      this.$router.push(`/user/surveys/${survey.id}`);
    },
    onConfirmPrivacyPolicy(isPrivacyPolicyConfirmed) {
      // call api to confirm privacy policy
      // set vuex
      this.$store.dispatch(
        "user/setHasAcceptedPrivacyPolicy",
        isPrivacyPolicyConfirmed
      );
      this.isPrivacyPolicyModalShown = false;
    },
    onConfirmTnC(isTncConfirmed) {
      // call api to confirm TnC
      // set vuex
      this.$store.dispatch("user/setHasAcceptedTnC", isTncConfirmed);
      this.isTnCModalShown = false;
    },
    getSurveysApi() {
      userListSurveys().then((response) => {
        this.surveys.length = 0;
        response.forEach((item) => {
          const respDateTimeFormat = "ddd, DD MMM YYYY hh:mm:ss zz";
          let rawSurveyStatus = 1;
          if (item["isPublished"] == true) {
            rawSurveyStatus = 2;
          }
          const rawSurveyStartDateMoment = convertToStandardDate(
            item["startDate"],
            respDateTimeFormat
          );
          let rawSurvey = {
            id: item["id"],
            title: item["title"],
            startDate: rawSurveyStartDateMoment,
            status: rawSurveyStatus,
            lastUpdatedDate: new Date(item["modificationDate"]),
          };
          this.surveys.push(rawSurvey);
        });
      });
    },
  },
};
</script>
<style lang="scss">
.user-surveys-view {
  margin: 20px 0;

  &.--no-padding {
    *[class~="col"] {
      padding: 0;
    }
  }
}

.user-surveys-card {
  padding: 20px 0 40px;

  &.--is-mobile {
    box-shadow: none !important;
  }

  &.--is-desktop {
    box-shadow: none !important;
    background: none !important;
  }
}

.user-surveys-table {
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

.user-surveys-search {
  &.--is-desktop {
    .v-input__slot {
      box-shadow: none !important;
      border: 1px solid $light-gray;
    }
  }
}
</style>
