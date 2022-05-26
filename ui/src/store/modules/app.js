import { make } from "vuex-pathify";

const state = {
  drawer: null,
  mini: false,
  items: []
};

const mutations = make.mutations(state);

const actions = {
  ...make.actions(state)
};

const getters = {};

export default {
  namespaced: true,
  state,
  mutations,
  actions,
  getters
};
