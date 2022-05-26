<template>
  <v-footer
    id="default-footer"
    :color="variables.default.primary"
    absolute
    app
  >
    survey app meong
    <links />
  </v-footer>
</template>

<script>
// Components
import Links from "@/components/Links";

export default {
  name: "DefaultFooter",
  components: { Links },
  computed: {
    variables() {
      return require("@styles/variables.js");
    }
  }
};
</script>
