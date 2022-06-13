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
export default {
  name: "DetailSummary",
  data() {
    return {
      summaryUrl: "http://localhost:8080/",
    };
  },
  created() {
    this.getSurveySummary();
  },
  computed: {
    surveyId() {
      return this.$route.params.id;
    },
  },
  methods: {
    onLoadSummaryPage() {
      // do something
    },
    getSurveySummary() {
      // get survey summary by id
      // assign to summaryUrl
      // load
    },
  },
};
</script>
<style lang="scss">
.detail-summary {
  .vue-friendly-iframe {
    iframe {
      width: 100%;
      min-height: 100vh;
    }
  }
}
</style>
