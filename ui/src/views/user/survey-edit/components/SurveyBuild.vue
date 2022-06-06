<template>
  <v-container
    fluid
    tag="section"
    class="survey-build"
  >
    <v-row justify="start">
      <v-col cols="12">
        <v-text-field
          name="title"
          placeholder="Survey name..."
          v-model.trim="formData.title"
        />
        <v-text-field
          name="description"
          placeholder="Survey description"
          v-model.trim="formData.description"
        />
      </v-col>
      <v-divider />
      <v-col cols="12">
        <container />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import Container from "@/form-builder/components/Container.vue";
export default {
  name: "SurveyBuild",
  components: {
    Container,
  },
  data() {
    return {
      formData: {
        title: "",
        description: "",
      },
      elements: [
        {
          id: "1",
          name: "test",
        },
      ],
    };
  },
};
</script>

<style lang="scss" scoped>
.survey-build {
}
</style>