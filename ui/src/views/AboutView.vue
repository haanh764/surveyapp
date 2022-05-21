<template>
  <div class="about">
    <h1>This is an about page</h1>
    <p>{{ message }}</p>
  </div>
</template>

<script>
export default {
  name: 'AboutView',
  data: () => ({
    message: String
  }),
  created() {
    fetch("http://localhost:5000")
      .then (response => response.json())
      .then (data => {
        this.message = data.message
      })
      .catch(error => {
        console.log(error)
      })
  }
};
</script>
