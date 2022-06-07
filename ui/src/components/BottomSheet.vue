<template>
  <v-bottom-sheet
    v-model="show"
    persistent
  >
    <v-sheet
      class="text-center"
      :height="windowHeight-100"
    >
      <v-container>
        <v-row>
          <v-col
            cols="12"
            class="text-right"
          >
            <v-btn
              class="mt-6"
              text
              @click="show = !show"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>
          </v-col>
          <v-col cols="12">
            <slot name="content" />
          </v-col>
        </v-row>
      </v-container>
    </v-sheet>
  </v-bottom-sheet>
</template>

<script>
export default {
  name: "BottomSheet",
  props: {
    value: Boolean,
  },
  computed: {
    show: {
      get() {
        return this.value;
      },
      set(value) {
        this.$emit("input", value);
      },
    },
  },
};
</script>
