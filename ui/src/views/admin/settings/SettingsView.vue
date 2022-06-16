<template>
  <v-container
    id="admin-settings-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="10">
        <v-card
          class="admin-settings-view__card"
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
                class="admin-settings-form"
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
                          class="my-0 pa-0 admin-settings-form__email"
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
                          class="my-0 pa-0 admin-settings-form__password"
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
                          class="mt-2 mb-5 v-btn--primary"
                          :disabled="!isPasswordLengthOkay"
                          @click="handleSubmit(onFormSubmit)"
                        >
                          SAVE SETTINGS
                        </v-btn>
                      </v-row>
                    </v-col>
                  </v-row>
                </v-container>
              </v-form>
            </ValidationObserver>
          </v-row>
        </v-card>

        <MaterialSnackbar
          v-model="isSucessSnackbarShown"
          type="success"
          timeout="1000"
          bottom
          right
        >
          New settings have been saved!
        </MaterialSnackbar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";
import { adminChangePassword } from "@api";

export default {
  name: "AdminSettingsView",
  data() {
    return {
      isFormValid: false,
      isPasswordShown: false,
      formData: {
        email: "",
        new_password: ""
      }
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
      adminChangePassword({ new_password: this.formData.new_password })
        .then((response) => {
          this.$notify.toast(response["message"]);
        });
    }
  }
};
</script>

<style lang="scss">
</style>
