export default function (data) {
  const blankList = [];

  let blankTemplate = "";

  for (let i = 0; i < blankList.length; i++) {
    blankTemplate += `
        <template slot="${blankList[i].name}" slot-scope="scope">
          <!-- ${blankList[i].label} -->
          <!-- use v-model="scope.model.${blankList[i].name}" to bind data -->
        </template>
    `;
  }

  return `<template>
  <div>
    <generate-form :data="jsonData" :value="editData" ref="generateForm">
      ${blankTemplate}
    </generate-form>
    <v-btn primary @click="handleSubmit">Submit</v-btn>
  </div>
</template>

<script>
  export default {
    data () {
      return {
        jsonData: ${data},
        editData: {},
      }
    },
    methods: {
      handleSubmit () {
        this.$refs.generateForm.getData().then(data => {
          // data check success
          // data - form data
        }).catch(e => {
          // data check failed
        })
      }
    }
  }
</script>`;
}
