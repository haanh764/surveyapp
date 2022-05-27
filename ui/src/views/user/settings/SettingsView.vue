<template>
  <v-container
    id="user-settings-view"
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col
        cols="8"
        md="8"
      >
        <material-card
          color="primary"
        >
          <v-img
            class="rounded-circle mt-n12 d-inline-block"
            :src="profilePicture"
            width="128"
          />
          <v-form>
            <v-container class="py-0">
              <v-row>
                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="formData.email"
                    disabled
                    label="E-mail address"
                  />
                </v-col>

                <v-col
                  cols="12"
                  md="12"
                >
                  <v-text-field
                    v-model="formData.password"
                    color="purple"
                    label="Password"
                  />
                </v-col>


                <v-col
                  cols="12"
                >
                  <v-btn
                    color="primary"
                    min-width="150"
                  >
                    Update Profile
                  </v-btn>
                </v-col>
              </v-row>
            </v-container>
          </v-form>
        </material-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default { 
  name: "UserSettingsView", 
  data() {
    return {
      formData: {
        email: "",
        password: ""
      }
    };
  },
  computed: {
    profilePicture() {
      return require("@assets/svg/profile_picture.svg");
    }
  } 
};
</script>
