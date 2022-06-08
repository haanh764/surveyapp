<template>
  <v-container
    fluid
    tag="section"
    class="survey-build"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class="pa-10"
      >
        <v-text-field
          v-model.trim="formData.title"
          name="title"
          placeholder="Survey name..."
        />
        <v-text-field
          v-model.trim="formData.description"
          name="description"
          placeholder="Survey description"
        />
      </v-col>
      <v-divider />
      <v-col
        cols="12"
        class="pa-10"
      >
        <form-builder v-model="formData.list" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FormBuilder from "@/form-builder/components/FormBuilder.vue";
export default {
  name: "SurveyBuild",
  components: {
    FormBuilder,
  },
  data() {
    return {
      formData: {
        title: "",
        description: "",
        list: [],
      },
    };
  },
  watch: {
    formData: {
      deep: true,
      handler(val) {
        this.$emit("input", val);
      },
    },
  },
  methods: {
    getData() {
      return this.formData;
    },
  },
};
</script>

<style lang="scss" scoped>
.survey-build {
}
</style>
