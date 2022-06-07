import Vue from "vue";
import vuetify from "./vuetify";
import VuetifyNotify from "vuetify-notify";

Vue.use(VuetifyNotify, {
  vuetify,
  options: {
    toast: {
      x: "right",
      y: "bottom",
      color: "black"
    },
    dialog: {
      width: 200
    }
  }
});
