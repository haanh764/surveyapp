<template>
  <v-dialog
    v-model="show"
    class="modal"
    max-width="600px"
    persistent
  >
    <v-card class="pa-0">
      <v-card-actions v-if="isCloseButtonShown">
        <v-row
          row
          d-flex
          nowrap
          align="right"
          justify="end"
          class="pa-4"
        >
          <v-btn
            icon
            text
            small
            fab
            @click.stop="show=false"
          >
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-row>
      </v-card-actions>
      <!-- use slot if default slot is given, else use default template -->
      <slot v-if="!!$slots.default" />
      <template v-else>
        <v-card-title v-if="isTitleShown">
          {{ title || "Title" | capitalize }}
        </v-card-title>
        <v-card-text v-if="isContentShown">
          {{ content }}
        </v-card-text>
        <v-card-actions v-if="isFooterShown" :class="isMobile? 'pa-0' : ''">
          <v-row justify="end">
            <v-col
              cols="auto"
              class="text-right"
            >
              <v-btn
                text
                @click.stop="show=false"
              >
                Close
              </v-btn>
              <v-btn
                color="primary"
                text
                class="text-uppercase"
                @click="onPrimaryActionButtonClick"
              >
                {{ primaryActionButtonText || "OK" }}
              </v-btn>
            </v-col>
          </v-row>
        </v-card-actions>
      </template>
    </v-card>
  </v-dialog>
</template>

<script>
export default {
  name: "Modal",
  props: {
    value: Boolean,
    title: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: ""
    },
    primaryActionButtonText: {
      type: String,
      default: ""
    },
    isTitleShown: {
      type: Boolean,
      default: true
    },
    isContentShown: {
      type: Boolean,
      default: true
    },
    isFooterShown: {
      type: Boolean,
      default: true
    },
    isCloseButtonShown: {
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
    onPrimaryActionButtonClick() {
      this.$emit("click:primary-action", true);
    }
  }
};
</script>
<style lang="scss">
.v-dialog {
  overflow: visible;
}
</style>
