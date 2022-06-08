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
          :data="value"
          :value="formData.models"
        />
      </v-col>
      <v-col
        v-if="value.list.length"
        cols="12"
      >
        <v-btn
          height="53"
          class="v-btn--primary"
          block
          disabled
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
  props: {
    value: {
      type: Object,
      default() {
        return {
          list: [],
          models: {},
        };
      },
    },
  },
  data() {
    return {
      generateFormKey: 1,
      formData: {
        list: [],
        models: {},
      },
    };
  },
  watch: {
    value: {
      deep: true,
      handler() {
        this.generateFormKey += 1;
      },
    },
  },
  created() {
    this.setFormData();
    this.setModels();
  },
  methods: {
    setFormData() {
      this.formData = { ...this.value };
      console.log(this.value);
    },
    setModels() {
      let modelObject = {};
      this.formData.list.forEach((widget) => {
        console.log(widget.options.defaultValue);
        modelObject[widget.model] = widget.options.defaultValue
          ? widget.options.defaultValue
          : "";
      });
      this.formData.models = modelObject;
    },
    getData() {
      console.log(JSON.stringify(this.formData));
    },
  },
};
</script>

<style>
</style>
