<template>
  <v-navigation-drawer
    id="default-drawer"
    v-model="drawer"
    class="default-drawer elevated-6"
    clipped
    :permanent="!isMobile"
    :mini-variant.sync="mini"
    :mini-variant-width="isMobile && !drawer? 0 : 80"
    :width="isMobile && !drawer ? 0 : width"
  >
    <div class="default-drawer__wrapper">
      <default-drawer-header />
      <v-divider class="mx-3 mb-2" />
      <default-list :items="items" />
      <default-drawer-toggle />
    </div>
  </v-navigation-drawer>
</template>

<script>
import { get, sync } from "vuex-pathify";

export default {
  name: "DefaultDrawer",
  components: {
    DefaultDrawerHeader: () =>
      import(
        /* webpackChunkName: "default-drawer-header" */
        "./widgets/DrawerHeader"
      ),
    DefaultList: () =>
      import(
        /* webpackChunkName: "default-list" */
        "./List"
      ),
    DefaultDrawerToggle: () =>
      import(
        /* webpackChunkName: "default-drawer-toggle" */
        "./widgets/DrawerToggle"
      )
  },
  computed: {
    ...get("user", [ "items" ]),
    ...sync("app", [ "drawer", "mini" ]),
    width() {
      return this.isMobile ? (this.drawer ? 260 : 0) : 260;
    }
  },
  watch: {
    isMobile(val) {
      this.drawer = !val;
    }
  }
};
</script>

<style lang="scss">
.default-drawer {
  padding: calculate-space(10) 0;
  box-shadow: $sidebar-box-shadow;

  .v-list {
    padding: 0;

    &--nav {
      .v-list-item {
        border-radius: 0;
      }
    }
  }

  .v-list-item {
    margin-bottom: 8px;
    border-radius: 0;

    &--active {
      color: map-get($theme-colors, "primary") !important;
      background-color: map-get($overlays, "primary") !important;
    }
  }

  .v-list-item::before,
  .v-list-item::after {
    display: none;
  }

  .v-list-group__header__prepend-icon,
  .v-list-item__icon {
    margin-top: 12px;
    margin-bottom: 12px;
    margin-left: 4px;
  }

  .v-navigation-drawer__border {
    background-color: none;
  }
}
</style>
