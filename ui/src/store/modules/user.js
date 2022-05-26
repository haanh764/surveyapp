import { make } from "vuex-pathify";
import { IN_BROWSER } from "@/util/globals";


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
    to: "/logout/"
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
    to: "/logout/"
  },
];

const state = {
  dark: true,
  userData: {
    accountType: 0,
    email: ""
  },
  token: "lapar",
  drawer: {
    gradient: 0,
    mini: false
  },
  items: [],
};

const mutations = {
  ...make.mutations(state),
  setUserData(state, data) {
    state.userData = { ...state.userData, ...data };
  }
};

const actions = {
  ...make.actions(state),
  fetch: ({ commit }) => {
    const local = localStorage.getItem("user") || "{}";
    const user = JSON.parse(local);

    for (const key in user) {
      commit(key, user[key]);
    }
  },
  update: ({ state }) => {
    if (!IN_BROWSER) return;

    localStorage.setItem("user", JSON.stringify(state));
  },
  init: async ({ dispatch }) => {
    // access api 
    // put below code in then block

    // set user data in state
    // dispatch('setUserData', userData);

    // set account type, token, has logged in
    // 0 = user
    // 1 = admin
    if (state.userData.accountType == 0) {
      dispatch('setItems', userMenuItems)
    } else if (state.userData.accountType == 1) {
      dispatch('setItems', adminMenuItems)
    }


  }
};

const getters = {
  dark: (state, getters) => {
    return (
      state.dark
    );
  },
  hasLoggedIn: (state) => {
    return !!state.token;
  },
  userData: (state) => {
    return state.userData || {};
  },
  accountType: (state) => {
    return state.userData.accountType || 0;
  }
};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
