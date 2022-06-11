<template>
  <v-bottom-sheet
    v-model="show"
    persistent
    :attach="fullscreen"
    :fullscreen="fullscreen"
    class="bottom-sheet s-bottom-sheet"
  >
    <v-sheet
      class="text-center s-bottom-sheet__content"
      :height="windowHeight-distance"
    >
      <v-container>
        <v-row
          class="mt-6"
          justify="center"
          align="center"
          :class="`text-${alignTitle}`"
        >
          <v-col cols="10">
            <h2>{{ title }}</h2>
          </v-col>
          <v-col cols="2">
            <v-btn
              small
              fab
              outlined
              elevation="2"
              class="s-bottom-sheet__close-button"
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
    alignTitle: {
      type: String,
      default: "left"
    },
    title: {
      type: String,
      default: ""
    },
    distance: {
      type: Number,
      default: 100
    },
    fullscreen: {
      type: Boolean,
      default: false
    }
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
  }
};
</script>
<style lang="scss">
.s-bottom-sheet {
  &__content {
    height: 100vh !important;
    overflow-y: auto;
  }

  &__close-button {
    background-color: $light-gray;
    color: $white !important;
    border: none !important;
  }
}
</style>
