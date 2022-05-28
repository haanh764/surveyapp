<template>
  <v-container
    id="error-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="auto">
        <h1>Page not found</h1>
        <p>The page either doesn't exist or you don't have access to this page</p>
        <center>
          <v-img :src="mainPicture" :width="imageWidth" contain />
        </center>
        <!-- to do: check the log in state, redirect based on the user type -->
        <v-btn
          depressed
          large
          to="/"
          :color="variables.default.primary"
          :width="imageWidth"
          class="white--text"
        >
          back to home
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default { name: "ErrorView",
  data: function() {
    return {
      imageWidth: "35vw"
    }
  },
  computed: {
    variables() {
      return require("@styles/variables.js");
    },
    mainPicture() {
      return require("@assets/svg/404.png");
    }
  } };
</script>

<style lang="scss">
</style>
