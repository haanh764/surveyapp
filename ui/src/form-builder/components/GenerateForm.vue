<template>
  <div>
    <h1> {{ data.title || 'Survey name' }}</h1>
    <p> {{ data.description || 'Survey description' }}</p>
    <template v-for="item in data.list">
      <generate-form-item
        :key="item.key"
        :models.sync="models"
        :rules="rules"
        :widget="item"
        @input-change="onInputChange"
      />
    </template>
  </div>
</template>

<script>
import GenerateFormItem from "./GenerateFormItem";

export default {
  name: "GenerateForm",
  components: {
    GenerateFormItem,
  },
  props: {
    data: {
      type: Object,
      default() {
        return {
          list: [],
        };
      },
    },
    value: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      models: {},
      rules: {},
    };
  },
  watch: {
    data: {
      deep: true,
      handler(val) {
        this.generateModel(val.list);
      },
    },
    value: {
      deep: true,
      handler(val) {
        this.models = { ...this.models, ...val };
      },
    },
  },
  created() {
    this.generateModel(this.data.list);
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
    onInputChange(value, field) {
      this.$emit("on-change", field, value, this.models);
    },
  },
};
</script>
