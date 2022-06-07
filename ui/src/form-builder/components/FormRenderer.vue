<template>
  <div>
    <div ref="test" />
    <index />
  </div>
</template>

<script>
import Vue from "vue";
import Index from "@/Index.vue";
import vuetify from "@/plugins/vuetify";
// import genFormCode from "../generator/generateFormCode";

export default {
  name: "FormRenderer",
  components: { Index },
  props: {
    code: {
      type: String,
      default: ""
    }
  },
  watch: {
    code() {
      // const code = genFormCode(this.data, this.value); // prev props were data & value
      // this.code = encodeURIComponent(code);

      const vm = new Vue({
        vuetify,
        template: "<div><v-text-field label='ngantuk' /></div>"
      });

      vm.$mount(this.$refs.test);
    }
  }
};
</script>
