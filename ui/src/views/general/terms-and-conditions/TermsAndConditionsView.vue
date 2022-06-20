<template>
  <v-container
    id="terms-and-conditions-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col
        :cols="isMobile? 12 : 10"
        class="text-left"
      >
        <v-card
          :elevation="isMobile? 0 : 2"
          class=""
          :class="{'pa-5': !isMobile}"
        >
          <v-card-title>Terms and Conditions</v-card-title>
          <v-card-text>
            <p>
              Please read this software's terms and conditions carefully before using the software.
            </p>
            <v-divider class="mt-5" />
            <p class="text-secondary mt-5 mb-5">
              {{ tnc.long }}
            </p>
            <v-divider class="mb-5" />
            <p>
              By accepting the terms and using this software, you are agreeing to be bound by the <strong>Terms and Conditions</strong>.
            </p>
          </v-card-text>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import tnc from "@assets/json/tnc.json";

export default {
  name: "TermsAndConditionsView",
  data() {
    return {
      tnc
    };
  }
};
</script>
