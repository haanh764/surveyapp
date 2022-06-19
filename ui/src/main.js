import Vue from "vue";
import axios from "axios";
import App from "./App.vue";
import router from "./router";
import vuetify from "./plugins/vuetify";
import store from "./store";
import axiosConfig from "./api/config.js";
import { sync } from "vuex-router-sync";
import "./plugins";
import "./mixins";
import "./filters";
import "./registerServiceWorker";
import { makeServer } from "./mocks/server";

Vue.config.productionTip = false;
Vue.prototype.$axios = axios.create(axiosConfig);

sync(store, router);

if (NODE_ENV == "development" && IS_API_MOCKED === "true") {
  makeServer();
}

new Vue({
  router,
  vuetify,
  store,
  render: (h) => h(App)
}).$mount("#app");

if (window.Cypress) {
  window.store = store;
  window.router = router;
  window.cookies = Vue.prototype.$cookies;
}
