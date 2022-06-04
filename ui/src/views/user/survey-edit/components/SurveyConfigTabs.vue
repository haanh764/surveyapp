<template>
  <div>
    <v-tabs
      v-model="tab"
      align-with-title
    >
      <v-tabs-slider color="yellow"></v-tabs-slider>
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
import SurveyElements from "@views/user/survey-edit/components/SurveyElements.vue";
import SurveySettings from "@views/user/survey-edit/components/SurveySettings.vue";

export default {
  name: "SurveyConfigTabs",
  components: {
    SurveyElements,
    SurveySettings,
  },
  data() {
    return {
      tab: "",
      items: [
        {
          title: "Elements",
          component: SurveyElements,
        },
        {
          title: "Settings",
          component: SurveySettings,
        },
      ],
    };
  },
};
</script>