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
          cols="12"
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
import { userGetSurveyDatatable } from "@api";

export default {
  name: "DetailResponses",
  data() {
    return {
      responsesUrl: "",
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
  computed: {
    surveyId() {
      return this.$route.params.id;
    }
  },
  created() {
    this.getSurveyDatatableApi(this.surveyId);
  },
  methods: {
    getSurveyDatatableApi(surveyId) {
      this.$notify.toast("Preparing data...");
      userGetSurveyDatatable(surveyId).then(() => {
        this.responsesUrl =
          process.env.VUE_APP_API_BASE_URL + "dash_datatable/";
      });
    },
    onLoadIframe() {
      this.$notify.toast("Responses successfully loaded.");
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
