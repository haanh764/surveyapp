<template>
  <v-btn
    class="ml-3 mr-4"
    elevation="1"
    fab
    small
    @click="mini = !mini"
  >
    <v-icon>
      {{ mini ? 'mdi-chevron-right' : 'mdi-chevron-left' }}
    </v-icon>
  </v-btn>
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
