<template>
  <v-container id="error-view" class="fill-height text-center" tag="section">
    <v-row justify="center">
      <v-col cols="auto">
        page not found
        <!-- to do: check the log in state, redirect based on the user type -->
        <v-btn depressed large to="/">
          back to home
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default { name: "ErrorView" };
</script>

<style lang="scss">
  #error-view h1.text-h1 {
    font-size: 14rem !important
  }
</style>