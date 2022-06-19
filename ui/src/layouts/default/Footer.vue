<template>
  <div>
    <cookies-confirmation
      v-model="isCookiesBottomSheetShown"
      @accept="hasAcceptedCookies = true"
    />
    <v-footer
      id="default-footer"
      class="default-footer"
      :color="style.color.primary"
    >
      <div class="default-footer__copyright">
        <v-img
          :src="logo"
          max-height="48"
          max-width="48"
        />
        <span class="copyright">
          (c) {{ new Date().getFullYear() }} SurveyApp Team
        </span>
      </div>
      <links class="default-footer__links" />
    </v-footer>
  </div>
</template>

<script>
import Links from "@/components/Links";
import CookiesConfirmation from "./CookiesConfirmation.vue";

export default {
  name: "DefaultFooter",
  components: { Links, CookiesConfirmation },
  data() {
    return {
      isCookiesBottomSheetShown: false
    };
  },
  computed: {
    logo() {
      return require("@assets/svg/logo.svg");
    },
    hasAcceptedCookies: {
      get() {
        return this.$store.getters["user/hasAcceptedCookies"];
      },
      set(val) {
        this.$store.dispatch("user/setHasAcceptedCookies", val);
      }
    }
  },
  mounted() {
    if (!this.hasAcceptedCookies) {
      this.isCookiesBottomSheetShown = true;
    }
  }
};
</script>

<style lang="scss">
.default-footer {
  z-index: 4;
  padding: 0 !important;

  &__copyright {
    display: block;
    color: transparentize($white, 0.2);
    background-color: map-get($theme-colors, "primary-dark");
    display: flex;
    width: 100%;
    padding: 20px 10px;
    align-items: center;
  }

  &__links {
    background-color: map-get($theme-colors, "primary-dark-2");
    color: transparentize($white, 0.4);
    padding: 10px 20px 50px;
    margin: 0;
    width: 100%;
  }
}
</style>
