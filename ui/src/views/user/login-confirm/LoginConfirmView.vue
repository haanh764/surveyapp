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
          description="Please confirm your registration before using our services. After clicking the activation link, please logout and then re-login."
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
          :max-image-height="isMobile ? 145: 305"
          :max-image-width="isMobile? 200: 400"
          :show-primary-button="false"
        >
          <template #actions>
            <div class="mt-5 text-secondary">
              Haven't received your activation email?
              <v-btn
                text
                class="text-none pa-0 text-secondary "
                @click="onClickResendActivation"
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
import { userResendActivation } from "@api";

export default {
  name: "LoginConfirmView",
  methods: {
    onClickResendActivation() {
      userResendActivation().then((response) => {
        this.$notify.toast(response["message"]);
      });
    }
  }
};
</script>

<style lang="scss">
#login-confirm-view {
  @include default-container-padding();
}
</style>
