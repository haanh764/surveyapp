<template>
  <div>
    <v-tabs
      v-model="tab"
      align-with-title
    >
      <v-tabs-slider color="yellow" />
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
        <component :is="item.component" />
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
    SurveyPreview
  },
  data() {
    return {
      tab: "",
      items: [
        {
          title: "Build",
          component: SurveyBuild
        },
        {
          title: "Preview",
          component: SurveyPreview
        }
      ]
    };
  }
};
</script>
