<template>
  <div id="user-surveys">
    user surveys
  </div>
</template>

<script>
export default {
  name: "AboutView",
  data: () => ({
    message: String
  }),
  created() {
    fetch("http://localhost:8000")
      .then (response => response.json())
      .then (data => {
        this.message = data.message;
      })
      .catch(error => {
        console.log(error);
      });
  }
};
</script>
