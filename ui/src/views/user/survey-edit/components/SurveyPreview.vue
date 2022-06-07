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
          :data="widgetForm"
          :value="widgetForm.value"
        />
      </v-col>
      <v-col cols="12">
        <v-btn
          height="53"
          class="v-btn--primary"
          block
          @click="getData"
        >
          SUBMIT
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import GenerateForm from "@/form-builder/components/GenerateForm.vue";
import formBuilderListSample from "@assets/json/form-builder-list-sample.json";

export default {
  name: "SurveyPreview",
  components: {
    GenerateForm,
  },
  data() {
    return {
      widgetForm: {
        list: formBuilderListSample.sample,
        value: {},
      },
    };
  },
  created() {
    this.setModels();
  },
  methods: {
    setModels() {
      let modelObject = {};
      this.widgetForm.list.forEach((widget) => {
        modelObject[widget.model] = widget.options.defaultValue
          ? widget.options.defaultValue
          : "";
      });
      this.widgetForm.value = modelObject;
    },
    getData() {
      console.log(JSON.stringify(this.widgetForm));
    },
    reset() {
      this.$refs.generateForm.resetFields();
    },
  },
};
</script>

<style>
</style>
