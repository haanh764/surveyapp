<template>
  <v-dialog
    v-model="show"
    class="modal"
    :class="{'--overflow-hidden': isPrompt}"
    :max-width="maxWidth"
    persistent
  >
    <v-card class="pa-0 modal__card">
      <v-card-actions v-if="isCloseButtonShown">
        <v-row
          row
          d-flex
          nowrap
          justify="end"
        >
          <v-col
            cols="9"
            class="text-left pa-0"
          >
            <v-card-title class="">
              {{ title }}
            </v-card-title>
            <v-card-subtitle class="d-block text-secondary">
              {{ subtitle }}
            </v-card-subtitle>
          </v-col>
          <v-col
            cols="3"
            class="align-flex--center justify-flex--end pa-0"
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
          </v-col>
        </v-row>
      </v-card-actions>
      <v-card-text
        v-if="content"
        class="pa-5"
      >
        {{ content }}
      </v-card-text>
      <slot name="default" />
      <v-card-actions v-if="isFooterShown">
        <v-row justify="end">
          <v-col
            cols="auto"
            class="text-right"
          >
            <v-btn
              text
              class="mr-2 close-button"
              @click.stop="show=false"
            >
              Close
            </v-btn>
            <slot name="actions" />
            <v-btn
              v-if="isActionButtonShown"
              color="primary"
              text
              class="text-uppercase primary-action-button"
              @click="onPrimaryActionButtonClick"
            >
              {{ primaryActionButtonText || "OK" }}
            </v-btn>
          </v-col>
        </v-row>
      </v-card-actions>
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
    subtitle: {
      type: String,
      default: ""
    },
    maxWidth: {
      type: Number,
      default: 600
    },
    content: {
      type: String,
      default: ""
    },
    primaryActionButtonText: {
      type: String,
      default: "OK"
    },
    isActionButtonShown: {
      type: Boolean,
      default: true
    },
    isFooterShown: {
      type: Boolean,
      default: true
    },
    isPrompt: {
      type: Boolean,
      default: true
    },
    isCloseButtonShown: {
      type: Boolean,
      default: true
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
.modal {
  &.--overflow-hidden {
    overflow: hidden;
  }
}
</style>
