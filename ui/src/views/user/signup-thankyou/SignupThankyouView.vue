<template>
  <v-container
    id="signup-thankyou-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile ? 12 : 10">
        <content-card
          title="Thanks for registering!"
          description="Please check your inbox or spams to confirm your registration"
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { name: "SignupThankyouView" };
</script>

<style lang="scss">
</style>
