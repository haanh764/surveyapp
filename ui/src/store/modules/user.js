import { make } from "vuex-pathify";

const userMenuItems = [
  {
    title: "My Surveys",
    icon: "mdi-clipboard-outline",
    to: "/user/surveys",
    isLastBeforeSeparation: true
  },
  {
    title: "Settings",
    icon: "mdi-cog",
    to: "/user/settings/"
  }
];

const adminMenuItems = [
  {
    title: "Users",
    icon: "mdi-account",
    to: "/admin/users",
    isLastBeforeSeparation: true
  },
  {
    title: "Settings",
    icon: "mdi-cog",
    to: "/admin/settings/"
  }
];

const generalMenuItems = [
  {
    title: "Logout",
    icon: "mdi-logout",
    to: "/logout/"
  }
];

const state = {
  userData: {
    accountType: null,
    email: null,
    hasAcceptedPrivacyPolicy: false,
    hasAcceptedTnC: false
  },
  token: null,
  drawer: {
    mini: false
  },
  items: generalMenuItems
};

const mutations = {
  ...make.mutations(state),
  setUserData(state, data) {
    state.userData = { ...state.userData, ...data };
  },
  setUserDataPrivacyPolicy(state, data) {
    state.userData.hasAcceptedPrivacyPolicy = data;
  },
  setUserDataTnC(state, data) {
    state.userData.hasAcceptedTnC = data;
  }
};

const actions = {
  ...make.actions(state),
  init: async ({ dispatch }) => {
    // access api
    // put below code in then block

    // set user data in state
    // dispatch('setUserData', userData);

    // set account type, token, has logged in
    // 0 = user
    // 1 = admin
    dispatch("checkAccountTypeAndSetMenuItems");
  },
  checkAccountTypeAndSetMenuItems: ({ state, dispatch }) => {
    if (state.userData.accountType == 0) {
      dispatch("setItems", userMenuItems.concat(generalMenuItems));
    } else if (state.userData.accountType == 1) {
      dispatch("setItems", adminMenuItems.concat(generalMenuItems));
    }
  },
  setUserDataPrivacyPolicy: ({ state, dispatch }, data) => {
    dispatch("setUserData", {
      ...state.userData,
      ...{ hasAcceptedPrivacyPolicy: data }
    });
  },
  setUserDataTnC: ({ state, dispatch }, data) => {
    dispatch("setUserData", {
      ...state.userData,
      ...{ hasAcceptedTnC: data }
    });
  }
};

const getters = {
  hasLoggedIn: (state) => {
    return !!state.token;
  },
  hasAcceptedPrivacyPolicy: (state) => {
    return !!state.userData.hasAcceptedPrivacyPolicy;
  },
  hasAcceptedTnC: (state) => {
    return !!state.userData.hasAcceptedTnC;
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
