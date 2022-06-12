<template>
  <v-container
    fluid
    tag="section"
    class="detail-questions fill-height"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class="detail-questions__info"
      >
        <v-row justify="start">
          <v-col cols="3">
            <v-icon>mdi-calendar</v-icon>
            {{ survey.config.startDate | convertToStandardDate }} - {{ survey.config.endDate }}
          </v-col>
          <v-col cols="4">
            <v-icon>
              mdi-user
            </v-icon>
            <template v-if="survey.config.isPublic">
              Public
              <v-btn
                text
                small
                outlined
                rounded
                class="text-secondary"
              >
                <v-icon
                  class="pr-2"
                  small
                >mdi-content-copy</v-icon>
                Copy link
              </v-btn>
            </template>
            <template v-else>
              Invite-only to {{ survey.config.emails.length }} participants
            </template>
          </v-col>
          <v-col cols="5">
            <strong class="d-block text-primary">
              <v-icon
                small
                class="mr-2"
              >mdi-clock</v-icon>
              {{ timeDifferenceBeforePublication }}
            </strong>
            <v-btn
              text
              small
              outlined
              rounded
              class="mr-2 text-secondary"
            >
              <v-icon
                small
                class="pr-2"
              >mdi-edit</v-icon>
              Edit survey
            </v-btn>
            <v-btn
              text
              small
              outlined
              rounded
              class="text-secondary"
            >
              <v-icon
                small
                class="pr-2"
                rounded
              >mdi-trash</v-icon>
              <u>Delete survey</u>
            </v-btn>
          </v-col>
        </v-row>
      </v-col>
      <v-col cols="12">
        <generate-form
          ref="generateForm"
          :form-data="survey.data"
          :value="survey.data.formBuilder.models"
          :is-submit-button-shown="false"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import surveyDataSample from "@/assets/json/survey-data-sample.json";
import GenerateForm from "@/form-builder/components/GenerateForm";
import { isTodayBeforeGivenDate } from "@/util/dates";

export default {
  name: "DetailQuestions",
  components: {
    GenerateForm,
  },
  data() {
    return {
      survey: {
        data: {
          isPublished: true,
        },
        config: {},
      },
    };
  },
  created() {
    this.survey = { ...this.survey, ...surveyDataSample };
    fetch("http://localhost:8000/api/authentication/signup", {
      method: "POST",
    }).then((response) => {
      console.log(response);
    });
  },
  computed: {
    timeDifferenceBeforePublication() {},
  },
};
</script>
