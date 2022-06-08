<template>
  <v-container
    fluid
    class="widget-form-container"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        class="pa-0"
      >
        <draggable
          :list="filteredList"
          v-bind="{group:{ name:'people',},sort:true, ghostClass: 'ghost', animation: 200, handle: '.drag-widget'}"
          :move="onWidgetMove"
          @end="onWidgetMoveEnd"
          @add="onWidgetAdd"
        >
          <transition-group
            name="fade"
            tag="div"
            class="widget-form-list"
          >
            <template v-for="(element, index) in filteredList">
              <widget-form-item
                v-if="element && element.key"
                :key="element.key"
                :element="element"
                :select.sync="selectedWidget"
                :index="index"
                :data="data"
                @click:moveTop="onWidgetItemMoveTopClick"
                @click:moveBottom="onWidgetItemMoveBottomClick"
                @click:clone="onWidgetItemCloneClick"
                @click:settings="onWidgetItemSettingsClick"
                @click:delete="onWidgetItemDeleteClick"
              />
            </template>
          </transition-group>
        </draggable>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { basicComponents } from "./components.js";
import WidgetFormItem from "./WidgetFormItem";
import { genUniqKey } from "@/util/form-builder";

export default {
  components: {
    WidgetFormItem,
  },
  props: {
    data: {
      type: Object,
      default() {
        return {
          list: [],
        };
      },
    },
    select: {
      type: Object,
      default() {
        return null;
      },
    },
  },
  data() {
    return {
      selectedWidget: this.select,
      widgets: [],
    };
  },
  computed: {
    filteredList: {
      get() {
        return this.data.list.filter((widget) => !!widget.key);
      },
      set(val) {
        this.data.list = val;
      },
    },
  },
  watch: {
    select(val) {
      this.selectedWidget = val;
    },
    selectedWidget: {
      deep: true,
      handler(val) {
        this.$emit("update:select", val);
      },
    },
  },
  mounted() {
    document.body.ondrop = function (event) {
      let isFirefox = navigator.userAgent.toLowerCase().indexOf("firefox") > -1;
      if (isFirefox) {
        event.preventDefault();
        event.stopPropagation();
      }
    };
  },
  methods: {
    onWidgetItemMoveTopClick(index) {
      this.$emit("click:moveTop", index);
    },
    onWidgetItemMoveBottomClick(index) {
      this.$emit("click:moveBottom", index);
    },
    onWidgetItemDeleteClick(index) {
      this.$emit("click:delete", index);
    },
    onWidgetItemSettingsClick(index) {
      this.$emit("click:settings", index);
    },
    onWidgetMove({ newIndex, oldIndex }) {
      console.log("index", newIndex, oldIndex);
    },
    onWidgetMoveEnd({ newIndex, oldIndex }) {
      console.log("index", newIndex, oldIndex);
    },
    onWidgetItemCloneClick({ widget, index }) {
      this.$emit("update:addWidget", { widget, index });
    },
    onWidgetAdd(event) {
      const to = event.to;

      console.log("add", event);
      console.log("end", event);
      console.log("to", to);

      const newIndex = event.newIndex;
      const key = genUniqKey();

      this.$emit("update:addWidget", {
        widget: {
          ...basicComponents[event.oldIndex],
          key,
          model: `${basicComponents[event.oldIndex].type}_${key}`,
          order: event.newIndex,
        },
        index: event.newIndex,
      });

      this.selectedWidget = this.data.list[newIndex];
    },
  },
};
</script>
