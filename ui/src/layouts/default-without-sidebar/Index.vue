<template>
  <v-app>
    <default-bar />

    <default-view />

    <default-footer />
  </v-app>
</template>

<script>
export default {
  name: "DefaultLayout",

  components: {
    DefaultBar: () => import(
      /* webpackChunkName: "default-app-bar" */
      "@layouts/default/AppBar"
    ),
    DefaultFooter: () => import(
      /* webpackChunkName: "default-footer" */
      "@layouts/default/Footer"
    ),
    DefaultView: () => import(
      /* webpackChunkName: "default-view" */
      "@layouts/default/View"
    )
  }
};
</script>
