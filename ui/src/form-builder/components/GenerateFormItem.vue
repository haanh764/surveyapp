<template>
  <v-container
    class="generate-form-item"
    :class="`generate-form-item--widget-${widget.type}`"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        v-if="isWidgetQuestionShown"
        cols="12"
      >
        <h1 class="generate-form-item__question pa-0">
          {{ widget.question || 'No question given' }}
        </h1>
        <p
          v-if="widget.description"
          class="text-secondary generate-form-item__description ma-0"
        >
          {{ widget.description }}
        </p>
      </v-col>

      <v-col
        v-if="widget.type == 'input'"
        cols="12"
        class=""
      >
        <v-text-field
          :ref="`${widget.type}_${widget.key}`"
          v-model.trim="dataModel"
          outlined
          :disabled="disabled"
          :placeholder="widget.options.placeholder"
        />
      </v-col>

      <v-col
        v-if="widget.type == 'radio'"
        cols="12"
        class="py-0"
      >
        <v-radio-group
          :ref="`${widget.type}_${widget.key}`"
          v-model="dataModel"
        >
          <v-radio
            v-for="(item, index) in widget.options.options"
            :key="index"
            :label="item.text"
            :disabled="disabled"
            :value="item.value"
          />
        </v-radio-group>
      </v-col>

      <v-col
        v-if="widget.type == 'checkbox'"
        cols="12"
        class=""
      >
        <v-item-group :ref="`${widget.type}_${widget.key}`">
          <v-checkbox
            v-for="(item, index) in widget.options.options"
            :key="`checkbox_${index}`"
            v-model="dataModel"
            :disabled="disabled"
            multiple
            :label="item.text"
            :value="item.value"
          />
        </v-item-group>
      </v-col>
      <v-col
        v-if="widget.type == 'text'"
        cols="12"
      >
        <h1
          v-if="widget.options.tag == 'h1'"
          :ref="`${widget.type}_${widget.key}`"
          class="generate-form-item__text --h1"
        >
          {{ dataModel }}
        </h1>
        <p
          v-if="widget.options.tag == 'p'"
          :ref="`${widget.type}_${widget.key}`"
          class="generate-form-item__text --p"
        >
          {{ dataModel }}
        </p>
      </v-col>
    </v-row>
    <v-row
      v-if="widget.type=='slider'"
      class=""
    >
      <v-col
        cols="2"
        class="text-center"
      >
        <small>
          {{ widget.options.min }}
        </small>
      </v-col>
      <v-col cols="8">
        <v-slider
          :ref="`${widget.type}_${widget.key}`"
          v-model="dataModel"
          :disabled="disabled"
          :min="widget.options.min"
          :max="widget.options.max"
          :step="widget.options.step"
        />
      </v-col>
      <v-col
        cols="2"
        class="text-center"
      >
        <small>
          {{ widget.options.max }} </small>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "GenerateFormItem",
  props: {
    widget: {
      type: Object,
      default() {
        return {};
      }
    },
    models: {
      type: Object,
      default() {
        return {};
      }
    },
    rules: {
      type: Object,
      default() {
        return {};
      }
    },
    disabled: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      dataModel: this.models[this.widget.model]
    };
  },
  computed: {
    isWidgetQuestionShown() {
      return this.widget.type != "text";
    }
  },
  watch: {
    dataModel: {
      deep: true,
      handler(val) {
        this.models[this.widget.model] = val;
        this.$emit("update:models", {
          ...this.models,
          [this.widget.model]: val
        });
      }
    },
    models: {
      deep: true,
      handler(val) {
        this.dataModel = val[this.widget.model];
      }
    }
  }
};
</script>

<style lang="scss">
.generate-form-item {
  &--widget-text {
  }

  &--widget-input {
  }
  &--widget-slider {
  }

  &--widget-checkbox {
    .v-input--selection-controls {
      margin: 0;
    }
  }
  &--widget-radio {
    .v-input--selection-controls {
      margin-top: 0;
    }
  }

  &__question {
    @include font-size(1.25);
  }

  &__description {
    @include font-size(1);
  }

  &__text {
    &.--p {
      @include font-size(1);
    }

    &.--h1 {
      @include font-size(1.25);
    }
  }
}
</style>
