import Vue from "vue";
import Vuetify from "vuetify/lib/framework";
import ripple from "vuetify/lib/directives/ripple";
import "@mdi/font/css/materialdesignicons.css";
import { style } from "@styles/variables.js";


Vue.use(Vuetify, { directives: { ripple } });


export default new Vuetify({
  breakpoint: { mobileBreakpoint: 960 },
  icons: {
    iconfont: "mdi",
    values: { expand: "mdi-menu-down" }
  },
  theme: {
    themes: {
      dark: style.color,
      light: style.color
    }
  }
});
