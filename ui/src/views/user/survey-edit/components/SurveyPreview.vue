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
    let modelObject = {};
    this.widgetForm.list.forEach((widget) => {
      modelObject[widget.model] = widget.options.defaultValue
        ? widget.options.defaultValue
        : "0";
    });
    this.widgetForm.value = modelObject;
  },
  methods: {
    setModels() {},
    getData() {
      return new Promise((resolve, reject) => {
        this.$refs.generateForm.validate((valid) => {
          if (valid) {
            resolve(this.models);
          } else {
            reject(new Error("error").message);
          }
        });
      });
    },
    reset() {
      this.$refs.generateForm.resetFields();
    },
  },
};
</script>

<style>
</style>
