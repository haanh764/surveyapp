<template>
  <div class="links">
    <v-row align="center">
      <v-col
        v-for="(link, i) in links"
        :key="i"
        class="text-left"
        :cols="isMobile? 6: 4"
        md="auto"
      >
        <router-link
          :to="link.href"
          class="text-decoration-none text-caption font-weight-regular"
        >
          {{ link.text }}
        </router-link>
      </v-col>
    </v-row>
  </div>
</template>

<script>
export default {
  name: "Links",

  data: () => ({
    links: [
      {
        href: "/privacy-policy",
        text: "Privacy Policy"
      },
      {
        href: "/terms-and-conditions",
        text: "Terms and Conditions"
      }
    ]
  })
};
</script>

<style lang="sass" scoped>
a
  color: inherit !important
</style>
