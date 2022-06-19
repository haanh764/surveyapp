<template>
  <v-container
    class="conditions-interaction"
    tag="section"
    fluid
  >
    <v-row justify="center">
      <v-col
        cols="12"
        class="pa-0"
      >
        <div class="pa-4 text-left">
          <h1 class="text-capitalize">
            {{ title }}
          </h1>
          <p class="mt-3">
            Please read this software {{ title }} carefully before using the software.
          </p>
        </div>
        <div class="conditions-interaction__content text-secondary text-left">
          <p>
            {{ content || 'No content were given.' }}
          </p>
        </div>
        <p class="pa-4 text-left">
          By accepting the terms and using this software, you are agreeing to be bound by the
          <a :href="link">
            {{ title }}.
          </a>
        </p>
      </v-col>
    </v-row>
    <v-row justify="space-between">
      <v-col
        cols="6"
        class="pa-4"
      >
        <v-btn
          block
          height="53"
          class="v-btn--default conditions-interaction__decline-button"
          @click="confirmConditions(false)"
        >
          DECLINE
        </v-btn>
      </v-col>
      <v-col
        cols="6"
        class="pa-4"
      >
        <v-btn
          block
          height="53"
          class="v-btn--primary conditions-interaction__accept-button"
          @click="confirmConditions(true)"
        >
          ACCEPT
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  name: "ConditionsInteraction",
  props: {
    title: {
      type: String,
      default: ""
    },
    link: {
      type: String,
      default: ""
    },
    content: {
      type: String,
      default: ""
    }
  },
  methods: {
    confirmConditions(isConfirmed) {
      this.$emit("confirm", isConfirmed);
    }
  }
};
</script>
<style lang="scss" scoped>
.conditions-interaction {
  @include font-size(1);

  &__content {
    max-height: 200px;
    padding: 20px 16px;
    overflow-y: scroll;
    border-top: 2px solid $light-gray;
    border-bottom: 2px solid $light-gray;
    margin-bottom: 8px;
  }
}
</style>
