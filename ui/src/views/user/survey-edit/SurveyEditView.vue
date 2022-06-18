<template>
  <v-container
    id="survey-edit-view"
    class="fill-height text-center"
    :class="{'--is-mobile': isMobile, '--is-desktop': !isMobile}"
    tag="section"
  >
    <v-row
      justify="space-between"
      class="mb-2"
    >
      <v-col
        cols="6"
        class="text-left pl-0"
      >
        <h1>
          Edit survey
        </h1>
      </v-col>
      <v-col
        cols="6"
        class="text-right pr-0"
      >
        <v-menu offset-y>
          <template #activator="{ on, attrs }">
            <v-btn
              class="v-btn--accent text-left"
              v-bind="attrs"
              width="150"
              v-on="on"
            >
              <v-icon class="mr-1">
                mdi-chevron-down
              </v-icon>
              Save
            </v-btn>
          </template>
          <v-list>
            <v-list-item
              v-for="(item, index) in saveOptions"
              :key="index"
              @click.stop="onOptionClick(item.callback)"
            >
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item>
          </v-list>
        </v-menu>
      </v-col>
    </v-row>
    <v-row>
      <v-col
        cols="12"
        class="survey-edit-view__card-wrapper"
      >
        <v-card
          class="survey-edit-view__card"
          elevation="0"
        >
          <v-row>
            <v-col
              :cols="isMobile ? 12 : 8"
              class="pa-0"
            >
              <survey-edit-tabs
                ref="surveyEditTabs"
                v-model="activeSurveyEditTab"
              />
            </v-col>
            <v-col
              v-if="!isMobile"
              cols="4"
              class="pa-0 survey-config-tabs-wrapper"
            >
              <survey-config-tabs ref="surveyConfigTabs" />
            </v-col>
          </v-row>
        </v-card>
      </v-col>
    </v-row>
    <v-row
      v-if="isMobile && activeSurveyEditTab == 0"
      justify="center"
    >
      <v-col
        cols="10"
        class="pa-0 survey-edit-view__mobile-menu"
      >
        <v-card elevation="3">
          <v-card-actions class="pa-0">
            <v-btn
              class="menu-button"
              text
              @click="onClickNewSurveyElementsButton"
            >
              <v-icon>
                mdi-plus
              </v-icon>
              <span>New survey elements</span>
            </v-btn>
            <v-btn
              class="menu-button"
              text
              @click="onClickSettingsButton"
            >
              <v-icon>
                mdi-cog
              </v-icon>
              <span>Settings</span>
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-col>
    </v-row>
    <bottom-sheet
      ref="menuBottomSheet"
      v-model="isBottomSheetShown"
      :title="bottomSheetTitle"
      :fullscreen="bottomSheetContent == 'settings'"
      :distance="bottomSheetContent == 'settings' ? 0 : 100"
      align-title="center"
    >
      <template #content>
        <template v-if="bottomSheetContent == 'surveyElements'">
          <survey-elements @update:addWidget="isBottomSheetShown = false" />
        </template>

        <template v-if="bottomSheetContent == 'settings'">
          <survey-settings
            ref="surveySettings"
            v-model="formData.config"
          />
        </template>
      </template>
    </bottom-sheet>
    <!-- dirty: added as gimmick to communicate with the settings component -->
    <survey-settings
      v-show="false"
      ref="surveySettings"
      v-model="formData.config"
    />
  </v-container>
</template>

<script>
import { EventBus } from "@/util/event-bus";
import { userGetSurvey, userAddSurvey, userEditSurvey } from "@api";

export default {
  name: "SurveyEditView",
  components: {
    SurveyEditTabs: () =>
      import(
        /* webpackChunkName: "survey-edit-tabs" */
        "./components/SurveyEditTabs"
      ),
    SurveyConfigTabs: () =>
      import(
        /* webpackChunkName: "survey-config-tabs" */
        "./components/SurveyConfigTabs"
      ),
    SurveyElements: () =>
      import(
        /* webpackChunkName: "survey-elements" */
        "./components/SurveyElements"
      ),
    SurveySettings: () =>
      import(
        /* webpackChunkName: "survey-settings" */
        "./components/SurveySettings"
      )
  },
  data() {
    return {
      isBottomSheetShown: false,
      bottomSheetContent: "surveyElements", // surveyElements, settings
      activeSurveyEditTab: 0,
      currentSurveyId: "new",
      formData: {
        data: {
          formBuilder: {
            list: []
          }
        },
        config: {}
      },
      saveOptions: [
        {
          title: "Save as draft",
          callback: "onSaveAsDraftOptionClick"
        },
        {
          title: "Save and publish",
          callback: "onSaveAndPublishOptionClick"
        }
      ]
    };
  },
  computed: {
    bottomSheetTitle() {
      const title = {
        surveyElements: "New survey elements",
        settings: "Survey settings"
      };
      return title[this.bottomSheetContent];
    }
  },
  mounted() {
    this.mountListeners();
  },
  created() {
    const surveyId = this.$route.params.id;
    if (surveyId != "new") {
      this.currentSurveyId = surveyId;
      this.getSurveyApi(surveyId);
    }
  },
  beforeDestroy() {
    this.destroyListeners();
  },
  methods: {
    destroyListeners() {
      EventBus.$off("event:setFormBuilderData");
    },
    mountListeners() {
      EventBus.$on("event:setFormBuilderData", ({ data, key }) => {
        this.formData[key] = data;
      });
    },
    onOptionClick(functionName) {
      this[functionName]();
    },
    getData() {
      EventBus.$emit("event:getFormBuilderData");

      this.formData.data.formBuilder.list = this.formData.data.formBuilder.list
        .map(
          // eslint-disable-next-line no-unused-vars
          ({ asset, ...widget }) => widget
        )
        .filter((widget) => !!widget.key)
        .map((widget, index) => {
          return {
            ...widget,
            order: index,
            model: widget.model ? widget.model : `${widget.type}_${widget.key}`
          };
        });

      return this.formData;
    },
    onSaveAsDraftOptionClick() {
      console.log("save as draft");
      const finalOutput = this.getData();
      console.log(JSON.stringify(finalOutput));

      this.saveUserSurveyApi(finalOutput);
    },
    onSaveAndPublishOptionClick() {
      console.log("save and publish");
      const finalOutput = this.getData();
      console.log(JSON.stringify(finalOutput));

      this.saveUserSurveyApi(finalOutput);
      // call api for publishing (sending email invitations) here
    },
    saveUserSurveyApi(finalOutput) {
      const areEmptyStartEndDates = (finalOutput["config"]["startDate"] == "" || finalOutput["config"]["endDate"] == "");
      if(areEmptyStartEndDates) {
        this.$notify.toast("Please give survey's start date and end date!");
      } else {
        if (this.currentSurveyId == "new") {
          userAddSurvey(finalOutput)
          .then(() => {
            this.$notify.toast("Your survey has been saved!");
            this.$router.push("/user/surveys/");
          }).catch((error) => {
            this.$notify.toast(error["message"]);
          });
        } else {
          finalOutput["config"]["id"] = this.currentSurveyId;
          userEditSurvey(finalOutput)
          .then(() => {
            this.$notify.toast("Your survey has been saved!");
            this.$router.push("/user/surveys/");
          }).catch((error) => {
            this.$notify.toast(error["message"]);
          });
        }
      }
    },
    onClickNewSurveyElementsButton() {
      this.isBottomSheetShown = true;
      this.bottomSheetContent = "surveyElements";
    },
    onClickSettingsButton() {
      this.isBottomSheetShown = true;
      this.bottomSheetContent = "settings";
    },
    getSurveyApi(surveyId) {
      console.log("running getSurveyApi() with param:");
      console.log(surveyId);
      userGetSurvey(surveyId)
        .then((response) => {
          console.log(JSON.stringify(response));
          // how to load the response into the formData?
        })
        .catch((error) => {
          console.log(error);
        });
    }
  }
};
</script>

<style lang="scss">
.survey-edit-view {
  padding: calculate-space(5) 0;

  &__card-wrapper {
    border: 1px solid $light-gray;
    background-color: $white;
    border-radius: 2px;
    overflow: hidden;
  }

  &__card {
  }

  &__mobile-menu {
    position: absolute;
    bottom: 10vh;
    flex: 1 1 auto;

    .v-card {
      overflow: hidden;
    }
    .menu-button {
      text-transform: none;
      word-spacing: 0;
      width: 50%;
      min-height: 60px;
      padding: 15px;

      span {
        display: block;
        font-weight: 300;
        @include font-size(0.875);
        letter-spacing: 0;
        color: $dark-gray;
        margin-top: calculate-space(0.5);
      }
    }
  }
}

.survey-config-tabs-wrapper {
  border-left: 1px solid $light-gray;
}
</style>
