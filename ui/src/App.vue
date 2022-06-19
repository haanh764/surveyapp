<template>
  <v-fade-transition mode="out-in">
    <div id="app">
      <router-view />
    </div>
  </v-fade-transition>
</template>

<script>
import "@/styles/overrides.scss";
import { EventBus } from "@util/event-bus";

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
  },
  mounted() {
    EventBus.$on("event:apiError", () => {
      this.$notify.toast("Something went wrong. Please try again later.");
    });
  },
  beforeDestroy() {
    EventBus.$off("event:apiError");
  }
};
</script>
