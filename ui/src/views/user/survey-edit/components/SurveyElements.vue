<template>
  <v-container
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="12">
        <draggable
          tag="ul"
          :list="items"
          v-bind="{group:{ name:'people', pull:'clone',put:false},sort:false, ghostClass: 'ghost'}"
          :move="onMovingElement"
          @end="onMovingElementEnd"
          @start="onMovingElementStart"
        >
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
        </draggable>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { basicComponents } from "@/form-builder/components/components.js";

export default {
  name: "SurveyElements",
  data() {
    return {
      items: [
        {
          title: "Short open answer",
          type: "input",
          options: {
            type: "text"
          },
          asset: require("@assets/icons/short_open_answer.png")
        },
        {
          title: "Long open answer",
          type: "input",
          options: {
            type: "textarea"
          },
          asset: require("@assets/icons/long_open_answer.png")
        },
        {
          title: "Single choice",
          type: "radio",
          asset: require("@assets/icons/radio.png")
        },
        {
          title: "Multiple choices",
          type: "checkbox",
          asset: require("@assets/icons/checkbox.png")
        },
        {
          title: "Slider",
          type: "slider",
          asset: require("@assets/icons/slider.png")
        },
        {
          title: "Headings",
          type: "text",
          options: {
            tag: "h1"
          },
          asset: require("@assets/icons/headings.png")
        },
        {
          title: "Paragraph",
          type: "text",
          options: {
            tag: "p"
          },
          asset: require("@assets/icons/paragraph.png")
        }
      ]
    };
  },
  created() {
    this.items = this.items.map((item) => {
      let basicComponent = basicComponents.find(
        (basicComponent) => basicComponent.type == item.type
      );
      return { ...item, ...basicComponent };
    });
  },
  methods: {
    onMovingElement() {},
    onMovingElementStart() {},
    onMovingElementEnd() {}
  }
};
</script>

<style>
</style>
