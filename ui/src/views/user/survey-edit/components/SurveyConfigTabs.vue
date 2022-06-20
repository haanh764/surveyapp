<template>
  <div class="survey-config-tabs">
    <v-tabs
      v-model="tab"
      centered
      grow
      class="survey-tab"
    >
      <v-tabs-slider color="primary" />
      <v-tab
        v-for="item in items"
        :key="item.title"
      >
        {{ item.title }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item.title"
      >
        <component
          :is="item.component"
          v-model="formData.config"
          :survey="survey"
        />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import SurveyElements from "@views/user/survey-edit/components/SurveyElements.vue";
import SurveySettings from "@views/user/survey-edit/components/SurveySettings.vue";

export default {
  name: "SurveyConfigTabs",
  components: {
    SurveyElements,
    SurveySettings
  },
  props: {
    survey: {
      type: Object,
      default() {
        return {
          data: {
            title: "",
            description: "",
            formBuilder: {
              list: [],
              models: {}
            }
          },
          config: {}
        };
      }
    }
  },
  data() {
    return {
      tab: "Elements",
      formData: {
        config: {}
      },
      items: [
        {
          title: "Elements",
          component: SurveyElements
        },
        {
          title: "Settings",
          component: SurveySettings
        }
      ]
    };
  },
  created() {
    this.setFormDataFromSurveyProp();
  },
  methods: {
    setFormDataFromSurveyProp() {
      this.formData.config = {
        ...this.formData.config,
        ...this.survey.config
      };
    },
    getData() {
      return this.formData;
    }
  }
};
</script>
<style lang="scss" scoped>
</style>
