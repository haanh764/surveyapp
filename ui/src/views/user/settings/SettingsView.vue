<template>
  <v-container
    class="user-settings-view"
    :class="{'--is-desktop': !isMobile}"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="10">
        <v-card
          class="user-settings-view__card"
          :class="{'pa-10': !isMobile}"
          :elevation="isMobile? 0 : 2"
        >
          <v-row justify="center">
            <v-col :cols="isMobile ? 12 : 8">
              <center>
                <v-img
                  class="mx-2 mb-10"
                  :src="require('@assets/svg/profile_picture.svg')"
                  width="200"
                />
              </center>
            </v-col>
            <ValidationObserver v-slot="{ handleSubmit }">
              <v-form
                v-model="isFormValid"
                class="user-settings-form"
                @keyup.native.enter="handleSubmit(onFormSubmit)"
                @submit.prevent="handleSubmit(onFormSubmit)"
              >
                <v-container class="py-0">
                  <v-row>
                    <v-col
                      cols="12"
                      class="my-0 pa-0"
                    >
                      <ValidationProvider
                        v-slot="{ errors }"
                        name="E-mail"
                        rules="required|email"
                      >
                        <v-text-field
                          v-model.trim="userEmail"
                          outlined
                          required
                          disabled
                          :error-messages="errors[0]"
                          label="E-mail"
                          class="my-0 pa-0 user-settings-form__email"
                          :background-color="style.color.disabled"
                        />
                      </ValidationProvider>
                    </v-col>
                    <v-col
                      cols="12"
                      class="my-0 pa-0"
                    >
                      <ValidationProvider
                        v-slot="{ errors }"
                        name="Password"
                        rules="required|min:8"
                      >
                        <v-text-field
                          v-model.trim="formData.new_password"
                          outlined
                          required
                          hint="Minimum 8 characters"
                          persistent-hint
                          label="Password"
                          class="my-0 pa-0 user-settings-form__password"
                          :append-icon="isPasswordShown ? 'mdi-eye' : 'mdi-eye-off'"
                          :type="isPasswordShown ? 'text' : 'password'"
                          :error-messages="errors[0]"
                          @click:append="isPasswordShown = !isPasswordShown"
                        />
                      </ValidationProvider>
                    </v-col>
                    <v-col
                      cols="12"
                      class="mt-10"
                    >
                      <v-row justify="center">
                        <v-btn
                          block
                          height="53"
                          min-width="150"
                          class="mt-2 mb-5 v-btn--primary user-settings-form__submit-button"
                          :loading="isLoading"
                          :disabled="!isPasswordLengthOkay || isLoading"
                          @click="handleSubmit(onFormSubmit)"
                        >
                          SAVE SETTINGS
                        </v-btn>
                      </v-row>
                      <v-row justify="center">
                        <v-btn
                          text
                          min-width="150"
                          class="text-none pa-0 mt-2 mb-5 user-settings-form__delete-button"
                          @click="onDeleteAccount()"
                        >
                          Delete Account
                        </v-btn>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
            </ValidationObserver>
          </v-row>
        </v-card>

        <modal
          v-model="isDeleteItemModalShown"
          name="delete-modal"
          title="We are sorry to see you go!"
          content="By deleting your account, you will lose all of your surveys and survey responses. If you are sure what you are doing, click the delete button below to continue."
          primary-action-button-text="YES, I WANT TO DELETE MY ACCOUNT"
          @click:primary-action="onDeleteConfirmation"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { userChangePassword, userDeleteAccount, userLogout } from "@api";

export default {
  name: "UserSettingsView",
  data() {
    return {
      isFormValid: false,
      isPasswordShown: false,
      isLoading: false,
      formData: {
        email: "",
        new_password: ""
      },
      isDeleteItemModalShown: false,
      isSucessSnackbarShown: false
    };
  },
  computed: {
    ...mapGetters("user", [ "userData" ]),
    userEmail() {
      return this.userData.email;
    },
    isPasswordLengthOkay() {
      return this.formData.new_password.length >= 8;
    }
  },
  methods: {
    onFormSubmit() {
      this.isLoading = true;
      userChangePassword({ new_password: this.formData.new_password })
        .then((response) => {
          this.$notify.toast(response["message"]);
          this.isLoading = false;
        })
        .catch(() => {
          this.isLoading = false;
        });
    },
    unsetClientData() {
      this.$store.dispatch("user/setToken", "");
      this.$store.dispatch("user/setUserData", {});
      this.$store.dispatch("user/setItems", []);
      this.$cookies.remove("access_token_cookie");
    },
    onDeleteAccount() {
      this.isDeleteItemModalShown = true;
    },
    onDeleteConfirmation() {
      userDeleteAccount().then((response) => {
        this.$notify.toast(response["message"]);
        userLogout()
          .then(() => {
            this.isDeleteItemModalShown = false;
            this.unsetClientData();
            this.$router
              .push({ name: "general-user-delete-thankyou" })
              .catch(() => {});
          })
          .catch(() => {
            this.isDeleteItemModalShown = false;
            this.unsetClientData();
            this.$router
              .push({ name: "general-user-delete-thankyou" })
              .catch(() => {});
          });
      });
    }
  }
};
</script>

<style lang="scss">
.user-settings-view {
  &.--is-desktop {
    margin: 20px 0;
  }
}

.user-settings-form {
  &__delete-button {
    letter-spacing: 0;
    font-weight: 400;
    text-transform: none;
    text-decoration: underline;
  }
}
</style>
