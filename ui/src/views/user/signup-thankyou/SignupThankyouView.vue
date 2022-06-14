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
        >
          <template #actions>
            <div class="mt-5 text-secondary">
              Haven't received your email?
              <v-btn
                text
                class="text-none pa-0 text-secondary "
              >
                <u class="d-inline-block ">Click here</u>
              </v-btn>
            </div>
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
