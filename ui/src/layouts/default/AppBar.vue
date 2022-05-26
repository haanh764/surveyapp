<template>
  <v-app-bar
    id="default-app-bar"
    app
    class="v-bar--underline"
    color="purple"
    :fixed="true"
    :clipped-left="true"
    :floating="true"
    :elevate-on-scroll="true"
    height="70"
    flat
  >

  SurveyApp
    <v-app-bar-nav-icon
      class="hidden-md-and-up"
      @click="drawer = !drawer"
    />


  </v-app-bar>
</template>

<script>
import { get, sync } from "vuex-pathify";

export default {
  name: "DefaultBar",

  components: {
  },

  computed: {
    ...sync("app", [
      "drawer",
      "mini"
    ]),
    name: get("route/name")
  }
};
</script>
