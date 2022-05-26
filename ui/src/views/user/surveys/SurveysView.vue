<template>
  <div id="user-surveys">
    user surveys
  </div>
</template>

<script>
import {getSurveys} from "@api";

export default {
  name: "AboutView",
  data: () => ({
    message: String
  }),
  created() {
    // example of fetching api directly with fetch 
    fetch("http://localhost:8000")
      .then (response => response.json())
      .then (data => {
        this.message = data.message;
      })
      .catch(error => {
        console.log(error);
      });

     // example 1 with axios
    this.$axios.get("https://api.coindesk.com/v1/bpi/currentprice.json")
      .then((response)=> {
        if(response.status == 200) {
          // do something
        } else {
          // error
          // do something
        }
      }).catch((error)=> {
        // do something on error
        console.error(error);
      });

    // example 2
    // recommended because this way the api is centered in one place/file
    // dont forget to handle errors
    getSurveys().then((response)=> {
      console.log(response);
    }).catch((error)=> {
      console.log(error);
    });


  }
};
</script>
