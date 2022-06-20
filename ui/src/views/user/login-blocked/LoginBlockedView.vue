<template>
  <v-container
    id="login-blocked-view"
    class="login-blocked-view fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 10">
        <content-card
          title="Your account has been blocked"
          description="Sorry, but you are not allowed to use our service because of potential misuse. Please contact our customer service if this is a mistake."
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
          :max-image-height="isMobile ? 145: 305"
          :max-image-width="isMobile? 200: 400"
          :show-primary-button="false"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { name: "LoginBlockedView" };
</script>

<style lang="scss">
#login-blocked-view {
  @include default-container-padding();
}
</style>
