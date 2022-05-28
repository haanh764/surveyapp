import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";
import pathify from "@/plugins/vuex-pathify";
import Cookies from "js-cookie";


// Modules
import * as modules from "./modules";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  reducer: (state) => ({ app: state.app })
});

const vuexCookie = new VuexPersistence({
  restoreState: (key) => Cookies.get(key) ? JSON.parse(Cookies.get(key)) : {},
  saveState: (key, state) =>
    Cookies.set(key, JSON.stringify(state), {
      expires: 3
    }),
  modules: [ "user" ] //only save user module
});

const store = new Vuex.Store({
  modules,
  plugins: [
    pathify.plugin,
    vuexLocal.plugin,
    vuexCookie.plugin
  ]
});

store.subscribe(mutation => {
  if (!mutation.type.startsWith("user/")) return;
});

store.dispatch("user/init");

export default store;

export const ROOT_DISPATCH = Object.freeze({ root: true });
