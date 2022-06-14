<template>
  <v-card
    v-bind="$attrs"
    class="content-card text-center"
    :class="{'--is-mobile': isMobile, 'elevated-2': !isMobile}"
    v-on="$listeners"
  >
    <v-container>
      <v-row justify="center">
        <v-col :cols="isMobile? 12: 8">
          <v-card-title class="content-card__title text-center">
            {{ title }}
          </v-card-title>
          <v-card-text class="content-card__description">
            {{ description }}
          </v-card-text>
          <v-img
            v-if="image"
            class="mx-auto"
            :src="image"
            :max-width="maxImageWidth"
            :max-height="maxImageHeight"
          />
          <v-btn
            v-if="showPrimaryButton"
            class="v-btn--primary content-card__home-button"
            height="53"
            block
            @click="onPrimaryButtonClick"
          >
            {{ primaryButtonText }}
          </v-btn>

          <template v-if="$slots.actions">
            <slot name="actions" />
          </template>
        </v-col>
      </v-row>
    </v-container>
  </v-card>
</template>

<script>
import router from "@/router";

export default {
  name: "ContentCard",
  props: {
    title: {
      type: String,
      default: ""
    },
    description: {
      type: String,
      default: ""
    },
    image: {
      type: String,
      default: null
    },
    maxImageWidth: {
      type: Number,
      default: 419
    },
    maxImageHeight: {
      type: Number,
      default: 305
    },
    showPrimaryButton: {
      type: Boolean,
      default: true
    },
    primaryButtonText: {
      type: String,
      default: "Back to home"
    },
    onPrimaryButtonClickCallback: {
      type: Function,
      default() {
        return router.push("/");
      }
    }
  },
  methods: {
    onPrimaryButtonClick() {
      this.$emit("click:primary");
      this.onPrimaryButtonClickCallback.call();
    }
  }
};
</script>

<style lang="scss">
.content-card {
  border: 1px solid $light-gray;
  padding: calculate-space(5) 0;

  @media only screen and (max-width: map-get($breakpoints, "md")) {
    padding: 0;
  }

  &.--is-mobile {
    border: none;
    box-shadow: none !important;
  }

  &__title {
    justify-content: center;
    @include font-size(1.5, "!important");
    font-weight: 600;

    @media only screen and (max-width: map-get($breakpoints, "md")) {
      @include font-size(1.25, "!important");
    }

    @media only screen and (max-width: map-get($breakpoints, "xxs")) {
      font-size: 1rem !important;
    }
  }

  &__description {
    color: $secondary-text-color;
    @include font-size(1, "!important");

    @media only screen and (max-width: map-get($breakpoints, "xxs")) {
      font-size: 0.8rem !important;
    }
  }

  &__home-button {
    margin-top: 30px;
  }
}
</style>
