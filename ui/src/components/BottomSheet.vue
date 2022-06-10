<template>
  <v-bottom-sheet
    v-model="show"
    persistent
  >
    <v-sheet
      class="text-center"
      :height="windowHeight-100"
    >
      <v-btn
        class="mt-6"
        text
        color="error"
        @click="show = !show"
      >
        close
      </v-btn>
      <slot name="content" />
    </v-sheet>
  </v-bottom-sheet>
</template>

<script>
export default {
  name: "BottomSheet",
  props: {
     value: Boolean
  },
  computed: {
    show: {
      get () {
        return this.value;
      },
      set (value) {
         this.$emit("input", value);
      }
    }
  }
};
</script>
