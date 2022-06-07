<template>
  <v-container
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="12">
        <draggable
          class="survey-elements"
          :list="items"
          v-bind="{group:{ name:'people', pull:'clone',put:false},sort:false, ghostClass: 'ghost'}"
          :move="onMovingElement"
          @end="onMovingElementEnd"
          @start="onMovingElementStart"
        >
          <v-list-item
            v-for="item in items"
            :key="item.title"
            class="survey-elements__item"
          >
            <v-list-item-content class="text-center">
              <center>
                <v-img
                  class="item__img mb-2"
                  :src="item.asset"
                  max-width="25"
                  max-height="25"
                />
              </center>
              <p class="ma-0 pa-0 item__text">
                {{ item.title | capitalize }}
              </p>
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
            type: "text",
          },
          asset: require("@assets/icons/short_open_answer.png"),
        },
        {
          title: "Long open answer",
          type: "input",
          options: {
            type: "textarea",
          },
          asset: require("@assets/icons/long_open_answer.png"),
        },
        {
          title: "Single choice",
          type: "radio",
          asset: require("@assets/icons/radio.png"),
        },
        {
          title: "Multiple choices",
          type: "checkbox",
          asset: require("@assets/icons/checkbox.png"),
        },
        {
          title: "Slider",
          type: "slider",
          asset: require("@assets/icons/slider.png"),
        },
        {
          title: "Headings",
          type: "text",
          options: {
            tag: "h1",
          },
          asset: require("@assets/icons/headings.png"),
        },
        {
          title: "Paragraph",
          type: "text",
          options: {
            tag: "p",
          },
          asset: require("@assets/icons/paragraph.png"),
        },
      ],
    };
  },
  created() {
    this.items = this.items.map((item) => {
      let basicComponent = basicComponents.find(
        (basicComponent) =>
          basicComponent.type == item.type &&
          (item.options ? basicComponent.options.tag == item.options.tag : true)
      );
      return { ...item, ...basicComponent };
    });
  },
  methods: {
    onMovingElement() {},
    onMovingElementStart() {},
    onMovingElementEnd() {},
  },
};
</script>

<style lang="scss">
.survey-elements {
  display: flex;
  width: 100%;
  flex-direction: row;
  flex-flow: wrap;

  &__item {
    max-width: 40%;
    margin: 0 5%;
    border: 1px solid $light-gray;
    border-radius: 5px;
    margin-bottom: calculate-space(2);
    text-align: center;

    &:hover {
      cursor: grab;
      background-color: $light-gray;
    }

    .item__img {
    }

    .item__text {
      word-break: break-all;
      @include font-size(0.75);
    }
  }
}
</style>
