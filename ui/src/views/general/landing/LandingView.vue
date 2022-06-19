<template>
  <v-container
    id="landing-view"
    class="fill-height fill-width"
    :class="{'--is-mobile': isMobile }"
    tag="section"
  >
    <v-row justify="center">
      <v-col
        :cols="isMobile? 10: 6"
        class="txt-col"
      >
        <v-img
          v-show="isMobile"
          class="txt-col__img"
          :src="mainPicture"
        />
        <p class="tagline--wrapper">
          <span class="tagline">
            Reach your respondents.
          </span>
          <span class="slogan">
            Expand your reach.
          </span>
        </p>
        <v-btn
          to="/user/signup"
          class="signup-button v-btn--accent "
          height="53"
          block
        >
          SIGN UP FOR FREE
        </v-btn>
        <p class="tagline-login">
          Already signed up? <router-link
            class="login-link"
            to="/user/login"
          >
            Log in
          </router-link>
        </p>
      </v-col>
      <v-col
        v-show="!isMobile"
        cols="5"
        class="img-col"
      >
        <v-img :src="mainPicture" />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "LandingView",
  computed: {
    mainPicture() {
      return require("@assets/svg/home.svg");
    }
  }
};
</script>

<style lang="scss">
#landing-view {
  .txt-col {
    padding-right: calculate-space(10, "px");

    &__img {
      display: block;
    }
  }

  .tagline--wrapper {
    margin-top: calculate-space(12, "px");

    @media only screen and (max-width: map-get($breakpoints, "md")) {
      margin-top: calculate-space(6, "px");
    }
  }

  .tagline {
    display: block;
    font-weight: 500;
    letter-spacing: 0.4px;
    color: $white;
    margin-bottom: calculate-space(1, "px");
    @include font-size(1.75);

    @media only screen and (max-width: map-get($breakpoints, "md")) {
      @include font-size(1.5);
    }
  }

  .slogan {
    display: block;
    font-weight: 900;
    letter-spacing: 0.4px;
    color: $white;
    margin-bottom: calculate-space(4, "px");
    @include font-size(3);

    @media only screen and (max-width: map-get($breakpoints, "md")) {
      @include font-size(2.5);
    }
  }

  .tagline-login {
    display: block;
    margin-top: calculate-space(2, "px");
    @include font-size(1);
    text-align: center;
    color: $grayish-white;

    .login-link {
      color: $grayish-white;
    }
  }

  &.--is-mobile {
    padding: 100px 0;

    .txt-col {
      padding-right: 0;
      padding-top: calculate-space(2, "px");
    }
  }
}
</style>
