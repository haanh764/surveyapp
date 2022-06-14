<template>
  <v-container
    fluid
    tag="section"
    class="survey-preview"
  >
    <v-row justify="start">
      <v-col cols="12">
        <generate-form
          ref="generateForm"
          :key="generateFormKey"
          :form-data="value"
          :value="value.formBuilder.models"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import GenerateForm from "@/form-builder/components/GenerateForm.vue";

export default {
  name: "SurveyPreview",
  components: {
    GenerateForm
  },
  props: {
    value: {
      type: Object,
      default() {
        return {
          formBuilder: {
            list: [],
            models: {}
          }
        };
      }
    }
  },
  data() {
    return {
      generateFormKey: 1
    };
  },
  watch: {
    "value.formBuilder.list": {
      deep: true,
      handler() {
        this.generateFormKey += 1;
        this.$nextTick(() => {
          this.$forceUpdate();
        });
      }
    }
  }
};
</script>

<style>
</style>
