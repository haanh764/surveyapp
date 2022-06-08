<template>
  <v-container
    id="admin-setting-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 8">
        <v-card
          class="admin-settings-view__card"
          :elevation="isMobile? 0 : 2"
        >
          <v-row justify="center">
            <v-card-title class="user-settings-view__title">
              <h1>Admin Settings</h1>
            </v-card-title>
            <v-col cols="2">
              <v-img
                class="rounded-circle d-inline-block mx-2"
                :src="require('@assets/svg/profile_picture.svg')"
                width="128"
              />
            </v-col>
          </v-row>
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
                <v-col
                  cols="12"
                >
                  <ValidationProvider
                      v-slot="{ errors }"
                      name="Password"
                      rules="required|min:8"
                  >
                    <v-text-field
                      v-model.trim="formData.password"
                      outlined
                      required
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
                <v-col
                  cols="12"
                >
                  <v-row justify="center">
                    <v-btn
                      color="primary"
                      min-width="150"
                      class="mt-2 mb-5"
                      @click="handleSubmit(onFormSubmit)"
                    >
                      Update Admin
                    </v-btn>
                  </v-row>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { 
  name: "AdminSettingsView", 
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
      // to do: post form data to back-end's update user api
      this.$router.push({ name: "admin-settings" });
    },
  },
};
</script>
