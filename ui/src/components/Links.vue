<template>
  <v-container>
    <v-row align="center">
      <v-col
        v-for="(link, i) in links"
        :key="i"
        class="text-center"
        cols="6"
        md="auto"
      >
        <a
          :href="link.href"
          class="text-decoration-none text-uppercase text-caption font-weight-regular"
          rel="noopener"
          target="_blank"
          v-text="link.text"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default {
    name: "Links",

    data: () => ({
      links: [
        {
          href: "/terms-and-conditions",
          text: "Terms and Conditions"
        },
        {
          href: "/privacy-policy",
          text: "Privacy Policy"
        }
      ]
    })
  };
</script>

<style lang="sass" scoped>
  a
    color: inherit !important
</style>
