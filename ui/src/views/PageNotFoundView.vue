<template>
  <v-container
    id="error-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col id="error-view-content">
        <h1>Page not found</h1>
        <p>The page either doesn't exist or you don't have access to this page</p>
        <v-img id="error-view-img" :src="mainPicture" contain />
        <!-- to do: check the log in state, redirect based on the user type -->
        <v-btn
          id="error-view-btn"
          depressed
          large
          to="/"
          :color="style.color.primary"
          class="white--text"
        >
          back to home
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default { name: "PageNotFoundView",
  computed: {
    mainPicture() {
      return require("@assets/svg/404.png");
    }
  } };
</script>

<style lang="scss">
  #error-view-content {
    max-height: 45vh;
  }
  #error-view-img {
    max-height: 100%;
    margin-left: auto;
    margin-right: auto;
  }
  #error-view-img, #error-view-btn {
    width: 33vw;
  }
  @media only screen and (max-width: map-get($breakpoints, "xl")) {
    #error-view-content {
      max-height: 38vh;
    }
  }
  @media only screen and (max-width: map-get($breakpoints, "lg")) {
    #error-view-img, #error-view-btn {
      width: 38vw;
    }
  }
  @media only screen and (max-width: map-get($breakpoints, "sm")) {
    #error-view-img, #error-view-btn {
      width: 40vw;
    }
  }
  @media only screen and (max-width: map-get($breakpoints, "xxs")) {
    #error-view-img, #error-view-btn {
      width: 45vw;
    }
  }
</style>
