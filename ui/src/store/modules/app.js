// Pathify
import { make } from "vuex-pathify";

const userMenuItems = [
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
  }];

const adminMenuItems = [
  {
    title: "Surveys",
    icon: "mdi-account",
    to: "/admin/surveys"
  },
  {
    title: "Users",
    icon: "mdi-account",
    to: "/admin/users"
  },
  {
    title: "Settings",
    icon: "mdi-clipboard-outline",
    to: "/admin/settings/"
  },
  {
    title: "Logout",
    icon: "mdi-format-font",
    to: "/admin/logout/"
  },
];

const state = {
  drawer: null,
  mini: false,
  userType: 2,
  items: []
};

const mutations = make.mutations(state);

const actions = {
  ...make.actions(state),
  init: async ({ dispatch }) => {
    dispatch('setItems', userMenuItems)
    console.log(state);
    if (state.userType == 1) {
      dispatch('setItems', userMenuItems)
    } else if (state.userType == 2) {
      dispatch('setItems', adminMenuItems)
    }
  }
};

const getters = {};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
