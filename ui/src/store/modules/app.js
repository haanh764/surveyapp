// Pathify
import { make } from "vuex-pathify";

// Data
const state = {
  drawer: null,
  drawerImage: true,
  mini: false,
  items: [
    {
      title: "My Surveys",
      icon: "mdi-account",
      to: "/user/surveys"
    },
    {
      title: "Settings",
      icon: "mdi-clipboard-outline",
      to: "/user/settings/"
    },
    {
      title: "Logout",
      icon: "mdi-format-font",
      to: "/user/logout/"
    },
  ]
};

const mutations = make.mutations(state);

const actions = {
  ...make.actions(state)
  // init: async ({ dispatch }) => {
  //   //
  // }
};

const getters = {};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
