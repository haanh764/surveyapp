<template>
  <v-container
    fluid
    tag="section"
    class="fill-height detail-summary"
  >
    <v-row>
      <v-col cols="12">
        <vue-friendly-iframe
          :src="summaryUrl"
          @load="onLoadSummaryPage"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { userGetSurveySummary } from "@api";

export default {
  name: "DetailSummary",
  data() {
    return {
      summaryUrl: ""
    };
  },
  computed: {
    surveyId() {
      return this.$route.params.id;
    }
  },
  created() {
    this.getSurveySummaryApi(this.surveyId);
  },
  methods: {
    getSurveySummaryApi(surveyId) {
      this.$notify.toast("Preparing data...");
      userGetSurveySummary(surveyId).then(() => {
        this.summaryUrl = "http://localhost:8000/dashboard/";
      });
    },
    onLoadSummaryPage() {
      this.$notify.toast("Stats summary loaded successfully.");
    }
  }
};
</script>
<style lang="scss">
.detail-summary {
  .vue-friendly-iframe {
    iframe {
      width: 100%;
      min-height: 500px;
      -ms-transform: scale(1.75);
      -moz-transform: scale(1.75);
      -o-transform: scale(1.75);
      -webkit-transform: scale(1.75);
      transform: scale(1.75);
      -ms-transform-origin: 0 0;
      -moz-transform-origin: 0 0;
      -o-transform-origin: 0 0;
      -webkit-transform-origin: 0 0;
      transform-origin: 0 0;
    }
  }
}
</style>
