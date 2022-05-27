<template>
  <v-app class="layout-default">
    <default-bar />
    <div style="content-wrapper">
      <default-drawer />
      <default-view />
    </div>

    <default-footer />
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",

  components: {
    DefaultBar: () => import(
      /* webpackChunkName: "default-app-bar" */
      "./AppBar"
    ),
    DefaultDrawer: () => import(
      /* webpackChunkName: "default-drawer" */
      "./Drawer"
    ),
    DefaultFooter: () => import(
      /* webpackChunkName: "default-footer" */
      "./Footer"
    ),
    DefaultView: () => import(
      /* webpackChunkName: "default-view" */
      "./View"
    )
  }
};
</script>
<style lang="scss">
.layout-default {
  .content-wrapper {
    display: flex; 
    height: 100%; 
  }
}
</style>
