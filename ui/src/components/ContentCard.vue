<template>
  <v-card
    v-bind="$attrs"
    v-on="$listeners"
    class="content-card"
    :class="{'--is-mobile': isMobile, 'elevated-2': !isMobile}"
  >
    >
    <v-container>
      <v-row>
        <v-col cols="10">
          <v-card-title>
            {{ title }}
          </v-card-title>
          <v-card-text>
            {{ description }}
          </v-card-text>
          <v-img
            v-if="image"
            :src="image"
            :max-height="maxImageHeight"
          />
          <v-btn
            flat
            v-if="showBackToHomeButton"
            class="v-btn--primary"
          >
            BACK TO HOME
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
export default {
  name: "ContentCard",
  props: {
    title: {
      type: String,
      default: "",
    },
    description: {
      type: String,
      default: "",
    },
    image: {
      type: Object,
      default: null,
    },
    maxImageHeight: {
      type: int,
      default: 100,
    },
    showBackToHomeButton: {
      type: boolean,
      default: true,
    },
  },
};
</script>

<style lang="scss">
.content-card {
  border: 1px solid $light-gray;

  &.--is-mobile {
    border: none;
  }
}
</style>
