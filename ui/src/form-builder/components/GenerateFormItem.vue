<template>
  <div :prop="widget.model">
    <div
      v-if="widget.type != 'text'"
      class="text-left"
    >
      <h1> {{ widget.question || 'No question given' }} </h1>
      <p class="text-secondary">
        {{ widget.description }}
      </p>
    </div>

    <template v-if="widget.type == 'input'">
      <v-text-field
        :ref="`${widget.type}_${widget.key}`"
        v-model="dataModel"
        outlined
        :placeholder="widget.options.placeholder"
      />
    </template>

    <template v-if="widget.type == 'radio'">
      <v-radio-group
        :ref="`${widget.type}_${widget.key}`"
        v-model="dataModel"
      >
        <v-radio
          v-for="(item, index) in widget.options.options"
          :key="index"
          :label="item.text"
          :value="item.value"
        />
      </v-radio-group>
    </template>

    <template v-if="widget.type == 'checkbox'">
      <v-item-group :ref="`${widget.type}_${widget.key}`">
        <v-checkbox
          v-for="(item, index) in widget.options.options"
          :key="index"
          v-model="dataModel"
          multiple
          :label="item.text"
          :value="item.value"
        >
          {{ item.text }}
        </v-checkbox>
      </v-item-group>
    </template>

    <template v-if="widget.type=='slider'">
      {{ widget.options.min }}
      <v-slider
        :ref="`${widget.type}_${widget.key}`"
        v-model="dataModel"
        :min="widget.options.min"
        :max="widget.options.max"
        :step="widget.options.step"
      />
      {{ widget.options.max }}
    </template>

    <template v-if="widget.type == 'text'">
      {{ widget.options.tag }}
      <h1
        v-if="widget.options.tag == 'h1'"
        :ref="`${widget.type}_${widget.key}`"
      >
        {{ dataModel }}
      </h1>
      <p
        v-if="widget.options.tag == 'p'"
        :ref="`${widget.type}_${widget.key}`"
      >
        {{ dataModel }}
      </p>
    </template>
  </div>
</template>

<script>
export default {
  name: "GenerateFormItem",
  props: {
    widget: {
      type: Object,
      default() {
        return {};
      },
    },
    models: {
      type: Object,
      default() {
        return {};
      },
    },
    rules: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      dataModel: this.models[this.widget.model],
    };
  },
  watch: {
    dataModel: {
      deep: true,
      handler(val) {
        this.models[this.widget.model] = val;
        this.$emit("update:models", {
          ...this.models,
          [this.widget.model]: val,
        });
        this.$emit("input-change", val, this.widget.model);
      },
    },
    models: {
      deep: true,
      handler(val) {
        this.dataModel = val[this.widget.model];
      },
    },
  },
};
</script>
