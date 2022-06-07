<template>
  <div>
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
    GenerateFormItem
  },
  props: [ "data", "remote", "value", "insite" ],
  data() {
    return {
      models: {},
      rules: {}
    };
  },
  watch: {
    data: {
      deep: true,
      handler(val) {
        this.generateModle(val.list);
      }
    },
    value: {
      deep: true,
      handler(val) {
        console.log(JSON.stringify(val));
        this.models = { ...this.models, ...val };
      }
    }
  },
  created() {
    this.generateModle(this.data.list);
    console.log("=====this.widgetForm======");
    console.log(this.data);
    console.log(this.value);
  },
  mounted() {},
  methods: {
    generateModle(genList) {
      for (let i = 0; i < genList.length; i++) {
        if (
          this.value &&
          Object.keys(this.value).indexOf(genList[i].model) >= 0
        ) {
          this.models[genList[i].model] = this.value[genList[i].model];
        } else {
          this.models[genList[i].model] = genList[i].options.defaultValue;
        }

        if (this.rules[genList[i].model]) {
          this.rules[genList[i].model] = [
            ...this.rules[genList[i].model],
            ...genList[i].rules.map((item) => {
              if (item.pattern) {
                return { ...item, pattern: eval(item.pattern) };
              } else {
                return { ...item };
              }
            })
          ];
        } else {
          this.rules[genList[i].model] = [
            ...genList[i].rules.map((item) => {
              if (item.pattern) {
                return { ...item, pattern: eval(item.pattern) };
              } else {
                return { ...item };
              }
            })
          ];
        }
      }
    },
    getData() {
      return new Promise((resolve, reject) => {
        this.$refs.generateForm.validate((valid) => {
          if (valid) {
            resolve(this.models);
          } else {
            reject(new Error("error").message);
          }
        });
      });
    },
    reset() {
      this.$refs.generateForm.resetFields();
    },
    onInputChange(value, field) {
      this.$emit("on-change", field, value, this.models);
    },
    refresh() {}
  }
};
</script>
