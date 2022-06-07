<template>
  <div :prop="widget.model">
    <template v-if="widget.type == 'input'">
      <v-text-field
        v-model="dataModel"
        :type="widget.options.dataType"
        :placeholder="widget.options.placeholder"
      />
    </template>

    <template v-if="widget.type == 'radio'">
      <v-radio-group v-model="dataModel">
        <v-radio
          v-for="(item, index) in widget.options.options"
          :key="index"
          :label="item.text"
          :value="item.value"
        />
      </v-radio-group>
    </template>

    <template v-if="widget.type == 'checkbox'">
      <v-item-group v-model="dataModel">
        <v-checkbox
          v-for="(item, index) in widget.options.options"
          :key="index"
          multiple
          :label="item.value"
        >
          {{ item.label }}
        </v-checkbox>
      </v-item-group>
    </template>

    <template v-if="widget.type=='slider'">
      <v-slider
        v-model="dataModel"
        :min="widget.options.min"
        :max="widget.options.max"
        :step="widget.options.step"
      />
    </template>

    <template v-if="widget.type == 'text'">
      <span>{{ dataModel }}</span>
    </template>
  </div>
</template>

<script>
export default {
  name: "GenerateFormItem",
  props: [ "widget", "models", "rules", "remote" ],
  data() {
    return {
      dataModel: this.models[this.widget.model]
    };
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
        this.$emit("input-change", val, this.widget.model);
      }
    },
    models: {
      deep: true,
      handler(val) {
        this.dataModel = val[this.widget.model];
      }
    }
  },
  created() {
    console.log("=======GenerateFormItem========");
    console.log("widget=", this.widget);
    console.log("models=", this.models);
    console.log("remote=", this.remote);
    console.log("dataModel=", this.dataModel);
  }
};
</script>
