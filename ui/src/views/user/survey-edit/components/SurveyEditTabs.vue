<template>
  <div>
    <v-tabs
      v-model="tab"
      class="survey-tab "
      :centered="isMobile"
      :grow="isMobile"
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
          :ref="item.ref"
          v-model="formData.formBuilder"
        />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import SurveyBuild from "@views/user/survey-edit/components/SurveyBuild.vue";
import SurveyPreview from "@views/user/survey-edit/components/SurveyPreview.vue";

export default {
  name: "SurveyEditTabs",
  components: {
    SurveyBuild,
    SurveyPreview,
  },
  data() {
    return {
      tab: "Build",
      formData: {
        title: "",
        description: "",
        formBuilder: {
          list: [],
          models: {},
        },
      },
      items: [
        {
          title: "Build",
          component: SurveyBuild,
          ref: "surveyBuild",
        },
        {
          title: "Preview",
          component: SurveyPreview,
          ref: "surveyPreview",
        },
      ],
    };
  },
  methods: {
    getData() {
      return this.formData;
    },
  },
};
</script>
