<template>
  <v-main
    class="default-main"
    :class="{'--is-mobile' : isMobile, '--is-purple': hasPurpleBackground }"
  >
    <v-container
      fluid
      class="default-main__container"
      :class="{'--is-mobile' : isMobile }"
    >
      <router-view :key="$route.path" />
    </v-container>
  </v-main>
</template>


<script>
export default {
  name: "DefaultView",
  computed: {
    hasPurpleBackground() {
      const allRouteNames = [ "general-landing" ];
      const desktopOnlyRouteNames = [
        "general-user-signup",
        "general-user-login",
        "general-admin-login"
      ];
      return this.isMobile
        ? allRouteNames.includes(this.$route.name)
        : allRouteNames
            .concat(desktopOnlyRouteNames)
            .includes(this.$route.name);
    }
  }
};
</script>
<style lang="scss">
.default-main {
  background-color: $grayish-white;

  &.--is-mobile {
    background-color: $white;
  }

  &.--is-purple {
    background-color: map-get($theme-colors, "primary");
  }

  &__container {
    min-height: 100vh;
  }
}
</style>
