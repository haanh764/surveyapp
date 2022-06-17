<template>
  <v-container
    class="text-center survey-detail-view"
    tag="section"
    :class="{'pa-0': isMobile, '--is-desktop': !isMobile }"
  >
    <v-row justify="center">
      <v-col
        :cols="isMobile? 12 : 10"
        :class="{'pa-0': isMobile }"
      >
        <v-card :elevation="isMobile? 0 : 2">
          <v-tabs
            v-model="tab"
            class="survey-tab"
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
              <component :is="item.component" />
            </v-tab-item>
          </v-tabs-items>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>


<script>
import DetailQuestions from "./components/DetailQuestions.vue";
import DetailResponses from "./components/DetailResponses.vue";
import DetailSummary from "./components/DetailSummary.vue";

export default {
  name: "SurveyDetailView",
  data() {
    return {
      tab: "",
      items: [
        {
          title: "Survey",
          component: DetailQuestions
        },
        {
          title: "Responses",
          component: DetailResponses
        },
        { title: "Summary", component: DetailSummary }
      ]
    };
  }
};
</script>
<style lang="scss">
.survey-detail-view {
  &.--is-desktop {
    margin: 20px 0;
  }
}
</style>
