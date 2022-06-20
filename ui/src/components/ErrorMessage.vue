<template>
  <span class="error-message" v-if="text" v-bind="$attrs" v-on="$listeners">
    {{ text }}
  </span>
</template>

<script>
export default {
  name: "ErrorMessage",
  props: {
    text: {
      type: String,
      default: "This field has errors",
    },
  },
};
</script>
<style lang="scss">
.error-message {
  color: red;
  display: block;
  @include font-size(0.875);
}
</style>
