<template>
  <v-container fluid>
    <v-row justify="start">
      <v-col cols="12">
        <h3>
          Submission date
        </h3>
        <p class="text-secondary">
          You can set start and end date of submission
        </p>
        <v-text-field
          v-model.trim="formData.startDate"
          placeholder="01/01/2022"
          outlined
          required
          label="Start date"
        />
        <v-text-field
          v-model.trim="formData.endDate"
          placeholder="01/01/2022"
          outlined
          required
          label="End date"
        />
      </v-col>
    </v-row>
    <v-row v-if="isPublic">
      public settings
    </v-row>
    <v-row v-else>
      <v-col cols="12">
        <h3>
          Invite-only
        </h3>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "SurveySettings",
  props: {
    survey: Object,
  },
  data() {
    return {
      formData: {
        startDate: "",
        endDate: "",
      },
      isPublic: false,
    };
  },
  created() {
    // set props data to data
  },
};
</script>

<style>
</style>