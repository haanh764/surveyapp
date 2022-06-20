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
        <ValidationProvider
          v-slot="{ errors }"
          name="Title"
          rules="required"
        >
          <v-text-field
            v-model.trim="formData.title"
            class="form__title"
            name="title"
            :error-messages="errors[0]"
            required
            placeholder="Survey title..."
          />
        </ValidationProvider>
        <v-text-field
          v-model.trim="formData.description"
          class="pa-0 form__description"
          name="description"
          placeholder="Survey description..."
        />
      </v-col>
      <v-col
        cols="12"
        class="pa-0"
      >
        <form-builder
          v-model="formData.formBuilder"
          :survey="survey"
        />
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
  props: {
    survey: {
      type: Object,
      default() {
        return {
          data: {
            title: "",
            description: "",
            formBuilder: {
              list: [],
              models: {}
            }
          },
          config: {}
        };
      }
    }
  },
  data() {
    return {
      formData: {
        title: "Survey title",
        description: "",
        formBuilder: {
          list: [],
          models: {}
        }
      }
    };
  },
  watch: {
    formData: {
      deep: true,
      handler(val) {
        this.$emit("input", val);
      }
    }
  },
  created() {
    this.setFormBuilderDataFromSurveyProp();
  },
  methods: {
    setFormBuilderDataFromSurveyProp() {
      this.formData = {
        ...this.formData,
        ...this.survey.data
      };
    },
    getData() {
      return this.formData;
    }
  }
};
</script>

<style lang="scss">
.survey-build {
  &__form {
    .theme--light.v-text-field > .v-input__control > .v-input__slot:before {
      border-color: $light-gray;
    }

    .form__title {
      @include font-size(1.5);
      font-weight: 500;
    }

    .form__description {
      @include font-size(1);
      text-color: $dark-gray;
    }
  }
}
</style>
