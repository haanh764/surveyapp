<template>
  <v-bottom-sheet
    v-model="show"
    :persistent="persistent"
    :attach="fullscreen"
    :fullscreen="fullscreen"
    class="bottom-sheet s-bottom-sheet"
  >
    <v-sheet
      class="text-center s-bottom-sheet__content"
      :height="height || windowHeight-distance"
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
              @click="onClickCloseButton"
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
    height: {
      type: Number,
      default: 0
    },
    distance: {
      type: Number,
      default: 100
    },
    persistent: {
      type: Boolean,
      default: true
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
  },
  methods: {
    onClickCloseButton() {
      this.show = !this.show;
      this.$emit("close");
    }
  }
};
</script>
<style lang="scss">
// bottom-sheet
.v-bottom-sheet {
  &:not(.v-dialog--fullscreen) {
    .v-sheet {
      border-top-left-radius: 20px !important;
      border-top-right-radius: 20px !important;
    }
  }
}

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
