<template>
  <v-container
    fluid
    tag="section"
    class="survey-build"
  >
    <v-row justify="start">
      <v-col cols="12">
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
      <v-col cols="12">
        <form-builder />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import FormBuilder from "@/form-builder/components/FormBuilder.vue";
export default {
  name: "SurveyBuild",
  components: {
    FormBuilder
  },
  data() {
    return {
      formData: {
        title: "",
        description: ""
      },
      elements: [
        {
          id: "1",
          name: "test"
        }
      ]
    };
  }
};
</script>

<style lang="scss" scoped>
.survey-build {
}
</style>
