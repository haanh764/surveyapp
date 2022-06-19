import Vue from "vue";
import Vuex from "vuex";
import VuexPersistence from "vuex-persist";
import pathify from "@/plugins/vuex-pathify";

// Modules
import * as modules from "./modules";

Vue.use(Vuex);

const vuexLocal = new VuexPersistence({
  storage: window.localStorage,
  reducer: (state) => ({ app: state.app, user: state.user }) // unsafe
});

const store = new Vuex.Store({
  modules,
  plugins: [ pathify.plugin, vuexLocal.plugin ]
});

store.subscribe((mutation) => {
  if (!mutation.type.startsWith("user/")) return;
});

store.dispatch("user/init");

export default store;

export const ROOT_DISPATCH = Object.freeze({ root: true });
