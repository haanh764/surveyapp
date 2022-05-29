<template>
  <v-app-bar
    id="default-app-bar"
    app
    class="v-bar--underline"
    :color="style.color.primary"
    :fixed="true"
    :clipped-left="true"
    height="70"
    flat
  >
    <v-app-bar-nav-icon
      v-if="isDrawerShown"
      class="hidden-md-and-up"
      @click="drawer = !drawer"
    />
    <v-btn
      class="logo test"
      text
      plain
      to="/"
    >
      SurveyApp
    </v-btn>
  </v-app-bar>
</template>

<script>
import { get, sync } from "vuex-pathify";
import { mapGetters } from "vuex";

export default {
  name: "DefaultBar",
  computed: {
    ...sync("app", [
      "drawer",
      "mini"
    ]),
    ...mapGetters("user", [
      "hasLoggedIn"
    ]),
    name: get("route/name"),
    isDrawerShown() {
      return this.hasLoggedIn;
    }
  }
};
</script>
<style lang="scss">
#default-app-bar {
  .logo {
    background-color: transparent; 
    color: $white;
    text-transform: none;
  }
}

</style>
