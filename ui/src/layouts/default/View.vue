<template>
  <v-main
    class="default-main"
    :class="{'--is-mobile' : isMobile, '--is-purple': hasPurpleBackground }"
  >
    <v-container
      fluid
      class="default-main__container"
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
      const routeNames = [ "general-landing", "general-user-signup", "general-user-login", "general-admin-login" ];
      return routeNames.includes(this.$route.name);
    }
  }, 
  mounted() {
    console.log(this.isMobile);
  }
};
</script>
<style lang="scss">

.default-main{
  &.--is-mobile {
    background-color: $grayish-white;
    min-height: 100vh;
  }

  &.--is-purple {
    background-color: map-get($theme-colors, 'primary');
  }

  &__container {
    min-height: 100vh;
  }
}
</style>
