<template>
  <v-container
    id="login-confirm-view"
    class="login-confirm-view fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 10">
        <content-card
          title="Your account hasn't been activated"
          description="Please confirm your registration before using our services."
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
          :max-image-height="isMobile ? 145: 305"
          :max-image-width="isMobile? 200: 400"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { name: "LoginConfirmView" };
</script>

<style lang="scss">
#login-confirm-view {
  @include default-container-padding();
}
</style>
