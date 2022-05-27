<template>
  <v-container
    id="landing-view"
    class="fill-height fill-width"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="auto">
        <v-img :src="mainPicture" />
        <p>
          <span>
            Reach your respondents.
          </span>
          <span>
            Expand your reach.
          </span>
        </p>
        <v-btn to="/user/signup">
          SIGN UP FOR FREE
        </v-btn>
        <p>
          Already signed up? <a href="/user/login">Log in</a>
        </p>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default { name: "LandingView",
  computed: {
    mainPicture() {
      return require("@assets/svg/home.svg");
    }
  } };
</script>

<style lang="scss">
  #landing-view  {
  }
</style>
