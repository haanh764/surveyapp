<template>
  <v-main
    class="default-main"
    :class="{'--is-mobile' : isMobile, '--is-purple': hasPurpleBackground }"
  >
    <v-container fluid>
      <router-view :key="$route.path" />
    </v-container>
  </v-main>
</template>

<script>
export default {
  name: "DefaultView", 
  computed: {
    hasPurpleBackground() {
      const routeNames = [ "general-landing", "general-signup", "general-login" ];
      return routeNames.includes(this.$route.name);
    }
  }
};
</script>
<style lang="scss">

.default-main{
  &.--is-mobile {
    background-color: $grayish-white;
    
  }

  &.--is-purple {
    background-color: map-get($theme-colors, 'primary');
  }
}
</style>
