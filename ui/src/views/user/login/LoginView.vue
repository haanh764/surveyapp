<template>
  <v-container
    class="login-view fill-height"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 8">
        <v-card
          class="login-view__card"
          :elevation="isMobile? 0 : 2"
        >
          <v-card-title class="login-view__title">
            Log In
          </v-card-title>
          <v-card-text class="login-view__description">
            Don’t have an account yet? <router-link to="/user/signup">
              Sign up here
            </router-link>
          </v-card-text>
          <ValidationObserver v-slot="{ handleSubmit }">
            <v-form
              v-model="isFormValid"
              class="login-form"
              @keyup.native.enter="handleSubmit(onFormSubmit)"
            >
              <v-container>
                <v-row class="login-view__row">
                  <v-col
                    cols="12"
                    class="pb-0"
                  >
                    <ValidationProvider
                      v-slot="{ errors }"
                      name="E-mail"
                      rules="required|email"
                    >
                      <v-text-field
                        v-model.trim="formData.email"
                        placeholder="email@email.com"
                        outlined
                        required
                        class="login-form__email"
                        :error-messages="errors[0]"
                        label="E-mail"
                      />
                    </ValidationProvider>
                  </v-col>

                  <v-col cols="12">
                    <ValidationProvider
                      v-slot="{ errors }"
                      name="Password"
                      rules="required|min:8"
                    >
                      <v-text-field
                        v-model.trim="formData.password"
                        outlined
                        hint="Minimum 8 characters"
                        persistent-hint
                        class="login-form__password"
                        label="Password"
                        :append-icon="isPasswordShown ? 'mdi-eye' : 'mdi-eye-off'"
                        :type="isPasswordShown ? 'text' : 'password'"
                        :error-messages="errors[0]"
                        @click:append="isPasswordShown = !isPasswordShown"
                      />
                    </ValidationProvider>
                  </v-col>
                  <v-col cols="12">
                    <v-btn
                      class="v-btn--is-elevated v-btn--primary login-form__submit-button"
                      height="53"
                      block
                      :disabled="isLoading"
                      :loading="isLoading"
                      @click="handleSubmit(onFormSubmit)"
                    >
                      LOG IN
                    </v-btn>
                    <!--
                    LOGIN WITH GOOGLE BUTTON
                    <span class="login-form__or"> or </span>
                    <v-btn
                      text
                      class="v-btn--is-elevated v-btn--default login-form__google-button"
                      height="53"
                      block
                    >
                      Connect with Google
                      <v-img
                        class="logo"
                        :src="require('@assets/icons/google.svg')"
                        :max-height="28"
                        max-width="28"
                      />
                    </v-btn>
                    -->
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </ValidationObserver>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { userLogin, userNotActivated, userisBlocked } from "@api";

export default {
  name: "LoginView",
  data() {
    return {
      isFormValid: false,
      isPasswordShown: false,
      isLoading: false,
      formData: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    onFormSubmit() {
      this.isLoading = true;
      userLogin(this.formData)
        .then((response) => {
          const authKey = response["message"].split("Access token is ")[1];
          const userData = {
            accountType: 0,
            email: this.formData.email
          };
          this.$cookies.set("access_token_cookie", authKey, { expires: 7 });
          this.$store.dispatch("user/setToken", authKey);
          this.$store.dispatch("user/setUserData", userData);
          this.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
          this.checkUserIsBlocked();
          this.isLoading = false;
        })
        .catch(() => {
          this.isLoading = false;
        });
    },
    checkUserIsBlocked() {
      userisBlocked()
        .then((userBlockedStatus) => {
          if (userBlockedStatus["message"].includes("is blocked")) {
            this.$store.dispatch("user/setIsBlocked", true);
            this.$router.push({ name: "user-blocked" }).catch(() => {});
          } else {
            this.checkUserIsActivated();
          }
        })
        .catch(() => {
          this.checkUserIsActivated();
        });
    },
    checkUserIsActivated() {
      userNotActivated()
        .then((userActivationStatus) => {
          if (
            userActivationStatus["message"].includes("is not activated")
          ) {
            this.$store.dispatch("user/setHasBeenActivated", false);
            this.$router.push({ name: "user-confirm" }).catch(() => {});
          } else {
            this.$store.dispatch("user/setHasBeenActivated", true);
            this.$router.push({ name: "user-surveys" }).catch(() => {});
          }
        })
        .catch(() => {
          this.$router.push({ name: "user-surveys" }).catch(() => {});
        });
    }
  }
};
</script>

<style lang="scss">
.login-view {
  @include default-container-padding;

  @media only screen and (max-width: map-get($breakpoints, "md")) {
    padding: 0;
  }

  &__card {
    padding: calculate-space(6);
    border-radius: 10px;

    @media only screen and (max-width: map-get($breakpoints, "md")) {
      padding: calculate-space(6) calculate-space(1.5) calculate-space(6);
    }
  }

  &__title {
    @include font-size(2);
  }

  &__description {
    @include font-size(1);

    a {
      color: inherit !important;
    }
  }

  .login-form {
    &__or {
      display: block;
      text-align: center;
      margin: calculate-space(2) calculate-space(2);
    }

    &__google-button {
      text-transform: none;
      background-color: $white;
      border: 1px solid $light-gray;
      font-weight: 400;

      .logo {
        margin-left: 10px;
      }
    }
  }
}
</style>
