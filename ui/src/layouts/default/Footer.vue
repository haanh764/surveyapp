<template>
  <v-footer
    id="default-footer"
    :color="variables.default.primary"
    absolute
    app
  >
    <v-img :src="logo" max-height="48" max-width="48" />
    <span>
      (c) {{ new Date().getFullYear() }} SurveyApp Team
    </span>
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
    },
    logo() {
      return require("@assets/svg/logo.svg");
    }
  }
};
</script>
