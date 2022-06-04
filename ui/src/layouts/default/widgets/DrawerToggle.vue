<template>
  <div
    class="drawer-toggle"
    :class="{'--is-mini': mini}"
  >
    <v-btn
      text
      fab
      small
      class="drawer-toggle__button"
      @click="mini = !mini"
    >
      <v-icon>
        {{ mini ? 'mdi-chevron-right' : 'mdi-chevron-left' }}
      </v-icon>
    </v-btn>
  </div>
</template>

<script>
import { sync } from "vuex-pathify";

export default {
  name: "DefaultDrawerToggle",

  computed: {
    mini: sync("app/mini")
  }
};
</script>
<style lang="scss">
.drawer-toggle {
  display: flex;
  justify-content: flex-end;
  align-items: flex-end;
  padding: 0 calculate-space(2);

  &.--is-mini {
    justify-content: center;
  }

  &__button {
  }
}
</style>
