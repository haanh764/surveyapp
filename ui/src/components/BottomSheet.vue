<template>
  <v-bottom-sheet
    v-model="show"
    persistent
  >
    <v-sheet
      class="text-center"
      :height="windowHeight-100"
    >
      <v-card class="px-0 py-5">
        <v-card-actions v-if="isCloseButtonShown">
          <v-row
            row
            d-flex
            nowrap
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
          <v-card-title
            v-if="isTitleShown"
            class="justify-center"
          >
            {{ title || "Title" | capitalize }}
          </v-card-title>
          <v-card-text
            v-if="isContentShown"
            class=text-center
          >
            {{ content }}
          </v-card-text>
          <v-card-actions
            v-if="isFooterShown"
            class="justify-center"
          >
            <v-row justify="center">
              <v-col
                cols="auto"
                class="text-center"
              >
                <v-btn
                  text
                  class="text-uppercase v-btn--primary"
                  @click="onPrimaryActionButtonClick"
                >
                  {{ primaryActionButtonText || "OK" }}
                </v-btn>
              </v-col>
            </v-row>
          </v-card-actions>
        </template>
      </v-card>
      <slot name="content" />
    </v-sheet>
  </v-bottom-sheet>
</template>

<script>
export default {
  name: "BottomSheet",
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
      default: true
    }
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
  },
  methods: {
    onPrimaryActionButtonClick() {
      this.$emit("click:primary-action", true);
    }
  }
};
</script>
