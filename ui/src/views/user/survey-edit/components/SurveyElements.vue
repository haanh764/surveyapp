<template>
  <v-container
    fluid
    tag="section"
  >
    <v-row justify="center">
      <v-col cols="12">
        <draggable
          class="survey-elements"
          :class="{'--is-mobile': isMobile}"
          :list="items"
          v-bind="{group:{ name:'people', pull:'clone',put:false},sort:false, ghostClass: 'ghost'}"
          :move="onMovingElement"
          @end="onMovingElementEnd"
          @start="onMovingElementStart"
        >
          <v-list-item
            v-for="(item, index) in items"
            :key="item.title"
            class="survey-elements__item"
            :class="{'--is-mobile': isMobile}"
            @dblclick.stop="onElementDoubleClick(item, index)"
            @click.stop="onElementClick(item, index)"
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
import { EventBus } from "@/util/event-bus";
import { genUniqKey } from "@/util/form-builder";

export default {
  name: "SurveyElements",
  data() {
    return {
      items: [
        {
          title: "Open answer",
          type: "input",
          asset: require("@assets/icons/short_open_answer.png")
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
        (basicComponent) =>
          basicComponent.type == item.type &&
          (item.options
            ? basicComponent.options.tag == item.options.tag
            : true) &&
          (item.options
            ? basicComponent.options.type == item.options.type
            : true)
      );
      return { ...item, ...basicComponent };
    });
  },
  methods: {
    onMovingElement() {},
    onMovingElementStart() {},
    onMovingElementEnd() {},
    addNewElement(widget, index) {
      widget.key = genUniqKey();
      widget.model = `${widget.type}_${widget.key}`;

      this.$emit("update:addWidget", { widget, index });
      EventBus.$emit("update:addWidget", { widget, index });
    },
    onElementDoubleClick(widget, index) {
      !this.isMobile && this.addNewElement(widget, index);
    },
    onElementClick(widget, index) {
      this.isMobile && this.addNewElement(widget, index);
    }
  }
};
</script>

<style lang="scss">
.survey-elements {
  display: flex;
  width: 100%;
  flex-direction: row;
  flex-flow: wrap;
  justify-content: space-between;

  &.--is-mobile {
  }

  &__item {
    max-width: 40%;
    height: 80px;
    margin: 0 10px;
    border: 1px solid $light-gray;
    border-radius: 5px;
    margin-bottom: calculate-space(2);
    text-align: center;

    &:hover {
      cursor: grab;
      background-color: $light-gray;
    }

    &.--is-mobile {
      max-width: 30%;
      margin: 5px;

      cursor: pointer;
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
