<template>
  <v-container
    id="delete-thankyou-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="12">
        <content-card 
          title="Thank you for using our services" 
          description="Your account has been successfully deleted. You can make a new account to use our services." 
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
          :max-image-width="240"
          :max-image-height="140"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { name: "DeleteThankyouView" };
</script>

<style lang="scss">
</style>
