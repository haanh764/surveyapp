<template>
  <v-container
    fluid
    tag="section"
  >
    <draggable
      tag="div"
      :list="items"
      v-bind="{group:{ name:'options'}, ghostClass: 'ghost',handle: '.drag-item'}"
      handle=".drag-item"
    >
      <v-list cols="2">
        <v-list-item
          v-for="item in items"
          :key="item.title"
        >
          <v-list-item-content>

            <v-img
              :src="item.asset"
              max-width="20"
              max-height="20"
            />

            {{ item.title | capitalize }}
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </draggable>
  </v-container>
</template>

<script>
export default {
  name: "SurveyElements",
  data() {
    return {
      items: [
        {
          title: "Headings",
          asset: require("@assets/icons/headings.png"),
        },
        {
          title: "Paragraph",
          asset: require("@assets/icons/paragraph.png"),
        },
        {
          title: "Short open answer",
          asset: require("@assets/icons/short_open_answer.png"),
        },
        {
          title: "Long open answer",
          asset: require("@assets/icons/long_open_answer.png"),
        },
        {
          title: "Single choice",
          asset: require("@assets/icons/radio.png"),
        },
        {
          title: "Multiple choices",
          asset: require("@assets/icons/checkbox.png"),
        },
        {
          title: "Slider",
          asset: require("@assets/icons/slider.png"),
        },
        {
          title: "Images",
          asset: require("@assets/icons/images.png"),
        },
      ],
    };
  },
};
</script>

<style>
</style>