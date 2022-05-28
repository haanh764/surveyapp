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
          <v-img v-if="isMobile()" :src="mainPicture" :width="imageWidthMobile" contain />
          <v-img v-else :src="mainPicture" :width="imageWidth" contain />
        </center>
        <!-- to do: check the log in state, redirect based on the user type -->
        <v-btn
          v-if="isMobile()"
          depressed
          large
          to="/"
          :color="variables.default.primary"
          :width="imageWidthMobile"
          class="white--text"
        >
          back to home
        </v-btn>
        <v-btn
          v-else
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
      imageWidth: "30vw",
      imageWidthMobile: "55vw"
    }
  },
  computed: {
    variables() {
      return require("@styles/variables.js");
    },
    mainPicture() {
      return require("@assets/svg/404.png");
    }
  },
  methods: {
    isMobile() {
      if( screen.width <= 760 ) {
        return true;
      }
      else {
        return false;
      }
    }
  } };
</script>

<style lang="scss">
</style>
