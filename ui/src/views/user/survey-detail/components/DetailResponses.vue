<template>
  <div class="detail-responses">
    <v-container
      fluid
      tag="section"
      class="pa-5"
    >
      <v-row
        justify="start"
        class="mt-2"
      >
        <v-col
          cols="7"
          class="text-left detail-responses__info"
        >
          <h1 class="title">
            {{ survey.data.title }}
          </h1>
          <p class="ma-0 description text-secondary">
            {{ survey.data.description }}
          </p>
        </v-col>
        <v-col
          cols="5"
          class="text-right"
        >
          <v-btn
            :block="isMobile"
            small
            height="44"
            class="v-btn--accent"
            @click="onClickDownloadButton"
          >
            <v-icon class="pr-1">
              mdi-download
            </v-icon>
            DOWNLOAD AS CSV
          </v-btn>
        </v-col>
        <v-col
          cols="12"
          class="mt-10"
        >
          <vue-friendly-iframe
            :src="responsesUrl"
            @load="onLoadIframe"
          />
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import surveyDataSample from "@/assets/json/survey-data-sample.json";

export default {
  name: "DetailResponses",
  data() {
    return {
      keyword: "",
      responsesUrl: "http://localhost:8000/",
      survey: {
        data: {
          title: "",
          description: "",
          formBuilder: {
            list: [],
            models: {}
          }
        },
        config: {}
      }
    };
  },
  created() {
    this.survey = { ...this.survey, ...surveyDataSample };
  },
  methods: {
    onClickDownloadButton() {
      // do something
      // fetch the api
      this.$notify.toast("File has been downloaded");
    },
    onLoadIframe() {
      // do something
    }
  }
};
</script>
<style lang="scss">
.detail-responses {
  .vue-friendly-iframe {
    iframe {
      width: 100%;
      min-height: 500px;
    }
  }
}
</style>
