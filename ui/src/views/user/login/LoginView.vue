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
              @submit.prevent="handleSubmit(onFormSubmit)"
            >
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <ValidationProvider
                      v-slot="{ errors }"
                      name="E-mail"
                      rules="required|email"
                    >
                      <v-text-field
                        v-model="formData.email"
                        :rules="[() => !!formData.email || 'This field is required']"
                        placeholder="email@email.com"
                        outlined
                        required
                        :error-messages="errors[0]"
                        label="E-mail"
                      />
                    </ValidationProvider>
                  </v-col>

                  <v-col cols="12">
                    <ValidationProvider
                      v-slot="{ errors }"
                      name="Password"
                      rules="required|alpha|min:8"
                    >
                      <v-text-field
                        v-model="formData.password"
                        outlined
                        hint="Minimum 8 characters"
                        persistent-hint
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
                      class="v-btn--is-elevated v-btn--primary"
                      height="53"
                      block
                      @click="handleSubmit(onFormSubmit)"
                    >
                      LOG IN
                    </v-btn>
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
export default {
  name: "LoginView",
  data() {
    return {
      isFormValid: false,
      isPasswordShown: false,
      formData: {
        email: "",
        password: "",
      },
    };
  },
  methods: {
    onFormSubmit() {
      // get submission with this.formData
      // submit form
      // get auth key
      // save to vuex
      const userData = {
        accountType: 0,
        email: "",
      };
      this.$store.dispatch("user/setToken", "test");
      this.$store.dispatch("user/setUserData", userData);
      this.$store.dispatch("user/checkAccountTypeAndSetMenuItems");

      this.$router.push({ name: "user-surveys" });
    },
  },
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
