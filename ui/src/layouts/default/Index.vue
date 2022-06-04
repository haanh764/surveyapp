<template>
  <v-app class="layout-default">
    <default-bar />
    <div
      class="layout-default__content"
      :class="{'--is-mobile': isMobile, '--is-drawer-open': drawer }"
    >
      <default-drawer />
      <default-view />
    </div>
    <default-footer />
  </v-app>
</template>

<script>
import { sync } from "vuex-pathify";

export default {
  name: "DefaultLayout",
  components: {
    DefaultBar: () =>
      import(
        /* webpackChunkName: "default-app-bar" */
        "./AppBar"
      ),
    DefaultDrawer: () =>
      import(
        /* webpackChunkName: "default-drawer" */
        "./Drawer"
      ),
    DefaultFooter: () =>
      import(
        /* webpackChunkName: "default-footer" */
        "./Footer"
      ),
    DefaultView: () =>
      import(
        /* webpackChunkName: "default-view" */
        "./View"
      )
  },
  computed: {
    ...sync("app", [ "drawer", "mini" ])
  }
};
</script>
<style lang="scss">
.layout-default {
  &__content {
    display: flex;
    height: 100%;

    &.--is-mobile {
      &.--is-drawer-open {
        display: initial;
      }
    }
  }
}
</style>
