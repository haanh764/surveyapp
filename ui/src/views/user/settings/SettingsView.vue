<template>
  <v-container
    id="user-settings-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col :cols="isMobile? 12 : 8">
        <v-card
          class="user-settings-view__card"
          :elevation="isMobile? 0 : 2"
        >
          <v-row justify="center">
            <v-col cols="4">
              <v-img
                class="rounded-circle d-inline-block mx-2 mb-5"
                :src="require('@assets/svg/profile_picture.svg')"
                width="128"
              />
            </v-col>
          </v-row>
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
                    class="my-0 py-0"
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
                        class="my-0 py-0"
                      />
                    </ValidationProvider>
                  </v-col>
                  <v-col
                    cols="12"
                    class="my-0 py-0"
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
                        class="my-0 py-0"
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
                        v-bind:disabled='!isDisabled'
                        @click="handleSubmit(onFormSubmit)"
                      >
                        SAVE SETTINGS
                      </v-btn>
                    </v-row>
                    <v-row justify="center">
                      <v-btn
                        text
                        min-width="150"
                        class="text-none pa-0 mt-2 mb-5"
                        @click="onDeleteAccount()"
                      >
                        DELETE ACCOUNT
                      </v-btn>
                    </v-row>
                  </v-col>
                </v-row>
              </v-container>
            </v-form>
          </ValidationObserver>
        </v-card>

        <modal
          v-if="!isMobile"
          v-model="isDeleteItemModalShown"
          name="delete-modal"
          title="We are sorry to see you go!"
          content="By deleting your account, you will lose all of your surveys and survey responses. If you are sure what you are doing, click the delete button below to continue."
          primary-action-button-text="YES, I WANT TO DELETE MY ACCOUNT"
          @click:primary-action="onDeleteConfirmation"
        />
        <BottomSheet
          v-else
          v-model="isDeleteItemModalShown"
          name="delete-bottomsheet"
          title="We are sorry to see you go!"
          content="By deleting your account, you will lose all of your surveys and survey responses. If you are sure what you are doing, click the delete button below to continue."
          primary-action-button-text="YES, I WANT TO DELETE MY ACCOUNT"
          @click:primary-action="onDeleteConfirmation"
        />

        <MaterialSnackbar
          v-model="isSucessSnackbarShown"
          type="success"
          timeout="500"
        >
          New settings have been saved!
        </MaterialSnackbar>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { mapGetters } from "vuex";

export default {
  name: "UserSettingsView",
  data() {
    return {
        isFormValid: false,
        isPasswordShown: false,
        formData: {
            email: "",
            password: ""
        },
        isDeleteItemModalShown: false,
        isSucessSnackbarShown: false,
    };
  },
  computed: {
    ...mapGetters("user", ["userData"]),
    userEmail() {
        return this.userData.email;
    },
    isDisabled() {
        return this.formData.password.length > 7;
    },
  },
  methods: {
    onFormSubmit() {
        // to do: post form data to back-end's update user api
        this.isSucessSnackbarShown = true;
        setTimeout( () => this.$router.push({ name: "user-surveys" }), 1000);
    },
    onDeleteAccount() {
        this.isDeleteItemModalShown = true;
    },
    onDeleteConfirmation() {
        // to do: call delete api
        this.isDeleteItemModalShown = false;
        this.$router.push({ name: "general-user-delete-thankyou" });
    },
  },
};
</script>

<style lang="scss">
:not(.v-select).v-text-field input[disabled="disabled"] {
    background-color: $light-gray;
}
</style>
