<template>
  <v-navigation-drawer
    id="default-drawer"
    v-model="drawer"
    :clipped="true"
    :mini-variant.sync="mini"
    mini-variant-width="80"
    app
    width="260"
  >

    <div class="px-2">
      <default-drawer-header />

      <v-divider class="mx-3 mb-2" />

      <default-list :items="items" />
      <v-divider class="mx-3 mb-2" />
      <default-drawer-toggle />
    </div>

    <div class="pt-12" />
  </v-navigation-drawer>
</template>

<script>
// Utilities
import { get, sync } from "vuex-pathify";

export default {
  name: "DefaultDrawer",

  components: {
    DefaultDrawerHeader: () => import(
      /* webpackChunkName: "default-drawer-header" */
      "./widgets/DrawerHeader"
    ),
    DefaultList: () => import(
      /* webpackChunkName: "default-list" */
      "./List"
    ),
    DefaultDrawerToggle: () => import(
      /* webpackChunkName: "default-drawer-toggle" */
      "./widgets/DrawerToggle"
    )
  },

  computed: {
    ...get("user", [
      "dark",
      "gradient",
      "image"
    ]),
    ...get("app", [
      "items",
      "version"
    ]),
    ...sync("app", [
      "drawer",
      "drawerImage",
      "mini"
    ])
  }
};
</script>

<style lang="sass">
#default-drawer
  .v-list-item
    margin-bottom: 8px

  .v-list-item::before,
  .v-list-item::after
    display: none

  .v-list-group__header__prepend-icon,
  .v-list-item__icon
    margin-top: 12px
    margin-bottom: 12px
    margin-left: 4px

  &.v-navigation-drawer--mini-variant
    .v-list-item
      justify-content: flex-start !important
</style>
