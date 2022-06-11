<template>
  <v-container
    id="signup-thankyou-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="auto">
        <content-card
          title="Thanks for registering!"
          description="Please check your inbox or spams to confirm your registration"
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
        >
          <template #actions>
            Haven't received your email?
            <v-btn
              text
              class="text-none pa-0"
            >
              Click here
            </v-btn>
          </template>
        </content-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { name: "SignupThankyouView" };
</script>

<style lang="scss">
</style>
