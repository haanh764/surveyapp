<template>
  <v-fade-transition mode="out-in">
    <router-view />
  </v-fade-transition>
</template>

<script>
import "@/styles/overrides.scss";

export default {
  name: "App",
  metaInfo: {
    title: "SurveyApp",
    titleTemplate: "%s | Your Survey Website",
    htmlAttrs: { lang: "en" },
    meta: [
      { charset: "utf-8" },
      { name: "viewport", content: "width=device-width, initial-scale=1" }
    ]
  }
};
</script>
