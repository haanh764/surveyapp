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
    <v-app-bar-nav-icon
      class="hidden-md-and-up"
      @click="drawer = !drawer"
    />


  </v-app-bar>
</template>

<script>
// Utilities
import { get, sync } from "vuex-pathify";

export default {
  name: "DefaultBar",

  components: {
    DefaultAccount: () => import(
      /* webpackChunkName: "default-account" */
      "./widgets/Account"
    ),
    DefaultDrawerToggle: () => import(
      /* webpackChunkName: "default-drawer-toggle" */
      "./widgets/DrawerToggle"
    ),
    DefaultGoHome: () => import(
      /* webpackChunkName: "default-go-home" */
      "./widgets/GoHome"
    ),
    DefaultNotifications: () => import(
      /* webpackChunkName: "default-notifications" */
      "./widgets/Notifications"
    ),
    DefaultSearch: () => import(
      /* webpackChunkName: "default-search" */
      "./widgets/Search"
    )
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
