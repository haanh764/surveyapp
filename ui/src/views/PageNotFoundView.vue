<template>
  <v-container
    id="error-view"
    class="fill-height text-center"
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="auto">
        <content-card 
          title="Page not found" 
          description="The page either doesn't exist or you don't have access to this page" 
          :image="require('@assets/svg/404.png')"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
  export default { name: "PageNotFoundView" };
</script>

<style lang="scss">
</style>
