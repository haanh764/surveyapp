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
          <ValidationObserver v-slot="{ handleSubmit }">
            <v-form
              v-model="isFormValid"
              class="login-form"
              @keyup.native.enter="handleSubmit(onFormSubmit)"
              @submit.prevent="handleSubmit(onFormSubmit)"
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
                      LOG IN
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
import { adminLogin } from "@api";

export default {
  name: "AdminLoginView",
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
      adminLogin(this.formData).then((response) => {
        const authKey = response["message"].split("Access token is ")[1];
        const userData = {
          accountType: 1,
          email: this.formData.email
        };
        this.$cookies.set("access_token_cookie", authKey);
        this.$store.dispatch("user/setToken", authKey);
        this.$store.dispatch("user/setUserData", userData);
        this.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
        this.$router.push({ name: "admin-users" });
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

  &__row {
    > .col {
      &:not:first-of-type {
        &:not:last-of-type {
          padding-bottom: 0;
        }
      }
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
  }
}
</style>
