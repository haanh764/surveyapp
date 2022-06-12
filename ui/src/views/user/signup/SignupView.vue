<template>
  <v-container
    class="signup-view fill-height"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 8">
        <v-card
          class="signup-view__card"
          :elevation="isMobile? 0 : 2"
        >
          <v-card-title class="signup-view__title">
            Sign Up
          </v-card-title>
          <v-card-text class="signup-view__description">
            Have an account already? <router-link to="/user/login">
              Log in here
            </router-link>
          </v-card-text>
          <ValidationObserver v-slot="{ handleSubmit }">
            <v-form
              v-model="isFormValid"
              class="signup-form"
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
                        v-model.trim="formData.email"
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
                      rules="required|min:8"
                    >
                      <v-text-field
                        v-model.trim="formData.password"
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
                      SIGN UP
                    </v-btn>
                    <span class="signup-form__or"> or </span>
                    <v-btn
                      text
                      class="v-btn--is-elevated v-btn--default signup-form__google-button"
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
//import { userSignup } from "@api";

export default {
  name: "SignupView",
  data() {
    return {
      isFormValid: false,
      isPasswordShown: false,
      formData: {
        email: "",
        password: ""
      }
    };
  },
  methods: {
    onFormSubmit() {
      // post form data to back-end's registration api
      /*
      userSignup(this.formData)
        .then((response) => {
          console.log(response);
          // do something with the response
          console.log("registration should be successful?");
          this.$router
            .push({ name: "general-user-signup-thankyou" })
            .catch(() => {});
        })
        .catch((error) => {
          console.log(error);
        });
      */
     fetch("http://localhost:8000/api/authentication/signup", {
        method: "POST",
        headers: [],
        body: {
          mode: "raw",
          raw: "{\n    \"email\": \"" + this.formData.email + "\",\n    \"password\": \"" + this.formData.password + "\"\n}",
          options: {
            raw: {
              language: "json"
            }
          }
        }
      }).then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
      /*
      fetch("http://localhost:8000/api/authentication/signup")
        .then((response) => response.json())
        .then((data) => {
          console.log(data);
        })
        .catch((error) => {
          console.log(error);
        });
      */
    }
  }
};
</script>

<style lang="scss">
.signup-view {
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

  .signup-form {
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
