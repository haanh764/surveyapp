<template>
  <v-container
    fluid
    tag="section"
    class="generate-form"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class="text-left py-0"
      >
        <h1 class="generate-form__title">
          {{ formData.title || 'Survey title' }}
        </h1>
      </v-col>
      <v-col
        v-if="formData.description"
        cols="12"
        class="text-left py-0"
      >
        <p class="generate-form__description text-secondary">
          {{ formData.description }}
        </p>
      </v-col>
      <v-col
        v-if="formData.formBuilder.list.length"
        cols="12"
      >
        <v-divider />
      </v-col>
      <v-col
        cols="12"
        class="text-left px-0 mt-5"
      >
        <template v-for="(item, index) in formData.formBuilder.list">
          <generate-form-item
            :key="`${item.key}_${index}`"
            :disabled="disabled"
            :models.sync="models"
            :widget="item"
            @input-change="onInputChange"
          />
        </template>
      </v-col>
      <v-col
        v-if="formData.formBuilder.list.length"
        cols="12"
      >
        <v-divider />
      </v-col>
      <v-col
        v-if="formData.formBuilder.list.length && isSubmitButtonShown"
        cols="12"
        class="justify-flex--end"
      >
        <v-btn
          height="53"
          width="50%"
          class="v-btn--primary"
          :disabled="!canSubmit"
          @click="onSubmitButtonClick"
        >
          SUBMIT
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import GenerateFormItem from "./GenerateFormItem";

export default {
  name: "GenerateForm",
  components: {
    GenerateFormItem
  },
  props: {
    value: {
      type: Object,
      default() {
        return {};
      }
    },
    formData: {
      type: Object,
      default() {
        return {};
      }
    },
    disabled: {
      type: Boolean,
      default: false
    },
    isSubmitButtonShown: {
      type: Boolean,
      default: true
    },
    canSubmit: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      models: {}
    };
  },
  watch: {
    "formData.formBuilder": {
      deep: true,
      handler(val) {
        this.generateModel(val.list);
        this.models = { ...this.value };
        this.$nextTick(() => {
          this.$forceUpdate();
        });
      }
    },
    value: {
      deep: true,
      handler(val) {
        this.models = { ...this.models, ...val };
      }
    }
  },
  created() {
    this.generateModel(this.formData.formBuilder.list);
    this.models = { ...this.value };
  },
  methods: {
    generateModel(genList) {
      for (let i = 0; i < genList.length; i++) {
        if (
          this.value &&
          Object.keys(this.value).indexOf(genList[i].model) >= 0
        ) {
          this.models[genList[i].model] = this.value[genList[i].model];
        } else {
          this.models[genList[i].model] = genList[i].options.defaultValue;
        }
      }
    },
    onSubmitButtonClick() {
      this.$emit("submit", {
        models: this.models,
        list: this.formData.formBuilder.list
      });
    },
    onInputChange(value, field) {
      this.$emit("on-change", field, value, this.models);
    }
  }
};
</script>
<style lang="scss">
.generate-form {
  margin: calculate-space(5) 0;
  @include font-size(1);

  &__title {
    @include font-size(2);
  }

  &__description {
    @include font-size(1.25);
  }
}
</style>
