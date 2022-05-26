<template>
  <v-footer
    id="default-footer"
    color="purple"
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

  components: { Links }
};
</script>
