import Vue from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store";
import axiosConfig from "./api/config.js";
import { sync } from "vuex-router-sync";
import "./plugins";
import { styleMixin } from "./mixins";
import "./registerServiceWorker";

Vue.config.productionTip = false;
Vue.prototype.$axios = axios.create(axiosConfig);
Vue.mixin(styleMixin);

sync(store, router);

new Vue({
  router,
  vuetify,
  store,
  render: h => h(App)
}).$mount("#app");
