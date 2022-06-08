<template>
  <v-container
    id="survey-edit-view"
    class="fill-height text-center"
    :class="{'--is-mobile': isMobile, '--is-desktop': !isMobile}"
    tag="section"
  >
    <template v-if="isMobile">
      mobile view
    </template>
    <template v-else>
      <v-row
        justify="space-between"
        class="mb-2"
      >
        <v-col
          cols="9"
          class="text-left"
        >
          <h1>
            Edit survey
          </h1>
        </v-col>
        <v-col
          cols="3"
          class="text-right"
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
        <v-col cols="12">
          <v-card>
            <v-row>
              <v-col
                cols="8"
                class="pa-0"
              >
                <survey-edit-tabs ref="surveyEditTabs" />
              </v-col>
              <v-col
                cols="4"
                class="pa-0"
              >
                <survey-config-tabs ref="surveyConfigTabs" />
              </v-col>
            </v-row>
          </v-card>
        </v-col>
      </v-row>
    </template>
  </v-container>
</template>

<script>
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
  },
  data() {
    return {
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

      console.log({ data: surveyData, config: settingData });
    },
    onSaveAndPublishOptionClick() {
      console.log("save and publish");
      // call api
      // save
      // go to detail page
    },
  },
};
</script>

<style lang="scss">
.survey-edit-view {
  padding: calculate-space(5) 0;
}
</style>
