<template>
  <v-container
    fluid
    tag="section"
    class="survey-build"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class="pa-3 survey-build__form"
      >
        <v-text-field
          v-model.trim="formData.title"
          name="title"
          required
          placeholder="Survey name..."
        />
        <v-text-field
          v-model.trim="formData.description"
          class="pa-0"
          name="description"
          placeholder="Survey description"
        />
      </v-col>
      <v-col
        cols="12"
        class="pa-0"
      >
        <form-builder v-model="formData.formBuilder" />
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
        title: "Survey name",
        description: "",
        formBuilder: {
          list: [],
          models: {},
        },
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

<style lang="scss">
.survey-build {
  &__form {
    border-bottom: 1px solid $light-gray;

    .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
      border-color: $light-gray;
    }
  }
}
</style>
