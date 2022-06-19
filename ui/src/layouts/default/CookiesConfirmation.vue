<template>
  <v-bottom-sheet
    v-model="show"
    persistent
    attach
    class="cookies-confirmation"
  >
    <v-card
      class="text-center cookies-confirmation__card"
      elevation="2"
    >
      <v-container>
        <v-row
          class="mt-6 text-center"
          justify="center"
          align="center"
        >
          <v-col
            cols="12"
            class="py-0"
          >
            <h2>Cookie Policy</h2>
          </v-col>
          <v-col
            cols="12"
            class="mb-5"
          >
            <p>Please accept the usage of cookies to continue using our website.</p>
            <v-btn
              text
              outlined
              @click="onClickAcceptButton"
            >
              Accept
            </v-btn>
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-bottom-sheet>
</template>

<script>
export default {
  name: "CookiesConfirmation",
  props: {
    value: Boolean
  },
  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      }
    }
  },
  methods: {
    onClickAcceptButton() {
      this.show = false;
      this.$emit("accept", true);
    }
  }
};
</script>
