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
        cols="8"
        class="text-left pl-0"
      >
        <h1>
          Edit survey
        </h1>
      </v-col>
      <v-col
        cols="4"
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
              <survey-edit-tabs ref="surveyEditTabs" />
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
      v-if="isMobile"
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
    >
      <template #content>
        <h2 class="text-center mb-2">
          New survey elements
        </h2>
        <survey-elements @update:addWidget="isBottomSheetShown = false" />
      </template>
    </bottom-sheet>
  </v-container>
</template>

<script>
import copyText from "@/util/copy.js";

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
  },
  data() {
    return {
      isBottomSheetShown: false,
      formData: {
        data: {},
        config: {},
      },
      saveOptions: [
        {
          title: "Save as draft",
          callback: "onSaveAsDraftOptionClick",
        },
        {
          title: "Save and publish",
          callback: "onSaveAndPublishOptionClick",
        },
      ],
    };
  },
  methods: {
    onOptionClick(functionName) {
      this[functionName]();
    },
    onSaveAsDraftOptionClick() {
      const surveyData = this.$refs.surveyEditTabs.getData();
      const settingData = this.$refs.surveyConfigTabs.getData();

      const finalOutput = { data: surveyData, config: settingData.config };
      console.log(JSON.stringify(finalOutput));
      copyText(JSON.stringify(finalOutput));

      this.$notify.toast("Survey has been successfully saved");
    },
    onSaveAndPublishOptionClick() {
      console.log("save and publish");
      // call api
      // save
      // go to detail page
    },
    onClickNewSurveyElementsButton() {
      this.isBottomSheetShown = true;
    },
    onClickSettingsButton() {},
  },
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
