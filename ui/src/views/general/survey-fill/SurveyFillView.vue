<template>
  <v-container
    id="survey-fill-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile ? 12: 10">
        <v-card
          :elevation="isMobile ? 0 : 2"
          class="pa-5"
        >
          <generate-form
            ref="generateForm"
            :form-data="survey.data"
            :value="survey.data.formBuilder.models"
            :can-submit="canSubmit"
            @submit="onClickSubmitButton"
          />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import surveyDataSample from "@/assets/json/survey-data-sample.json";
import GenerateForm from "@/form-builder/components/GenerateForm.vue";

export default {
  name: "SurveyFillView",
  components: { GenerateForm },
  data() {
    return {
      survey: {
        data: {
          title: "",
          description: "",
          formBuilder: {
            list: [],
            models: {},
          },
        },
        config: {
          startDate: "",
          endDate: "",
        },
      },
    };
  },
  computed() {},
  created() {
    this.survey = { ...this.survey, ...surveyDataSample };
  },
};
</script>

<style lang="scss">
</style>
