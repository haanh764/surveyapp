<template>
  <v-navigation-drawer
    id="default-drawer"
    v-model="drawer"
    class="elevated-6"
    clipped
    :floating="isMobile"
    :mini-variant.sync="mini"
    mini-variant-width="80"
    :width="width"
  >
    <div class="px-2">
      <default-drawer-header />
      <v-divider class="mx-3 mb-2" />
      <default-list :items="items" />
      <v-divider class="mx-3 mb-2" />
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
      ),
  },
  computed: {
    ...get("user", ["items"]),
    ...sync("app", ["drawer", "mini"]),
    width() {
      return this.isMobile ? (this.drawer ? 260 : 0) : 260;
    },
  },
  watch: {
    isMobile(val) {
      this.drawer = !val;
    },
  },
};
</script>

<style lang="scss">
#default-drawer {
  .v-list-item {
    margin-bottom: 8px;
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

  &.v-navigation-drawer--mini-variant {
    .v-list-item {
      justify-content: flex-start !important;
    }
  }
}
</style>
