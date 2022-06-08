<template>
  <v-container
    v-if="hasElement && hasSelectedWidget"
    class="widget-view"
    :class="{'active': selectedWidget.key == element.key}"
    :label="element.name"
    @click.stop="onWidgetItemClick(index)"
  >
    <template v-if="element.type != 'text'">
      <v-text-field
        v-model="element.question"
        label="Question"
        disabled
        placeholder="Survey question"
      />

      <v-text-field
        v-model="element.description"
        label="Description"
        disabled
        placeholder="Survey description"
      />
    </template>

    <template v-if="element.type == 'input'">
      <v-text-field
        v-model="element.options.defaultValue"
        :placeholder="element.options.placeholder"
        disabled
        outlined
      />
    </template>

    <template v-if="element.type == 'radio'">
      <v-radio-group v-model="element.options.defaultValue">
        <v-radio
          v-for="(item, index) in element.options.options"
          :key="item.value + index"
          disabled
          :label="item.text"
          :value="item.value"
        />
      </v-radio-group>
    </template>

    <template v-if="element.type == 'checkbox'">
      <v-item-group>
        <v-checkbox
          v-for="(item, index) in element.options.options"
          :key="item.value + index"
          v-model="element.options.defaultValue"
          disabled
          :label="item.text"
          :value="item.value"
        >
          {{ item }}
        </v-checkbox>
      </v-item-group>
    </template>

    <template v-if="element.type=='slider'">
      {{ element.options.min }}
      <v-slider
        v-model="element.options.defaultValue"
        :min="element.options.min"
        :max="element.options.max"
        disabled
        :step="element.options.step"
      />
      {{ element.options.max }}
    </template>

    <template v-if="element.type == 'text'">
      <h1 v-if="element.options.tag == 'h1'">
        {{ element.options.defaultValue }}
      </h1>
      <p v-if="element.options.tag == 'p'">
        {{ element.options.defaultValue }}
      </p>
    </template>

    <div
      v-if="selectedWidget.key == element.key"
      class="widget-view-action"
    >
      <v-btn
        small
        text
        @click.stop="onWidgetItemClone(index)"
      >
        <v-icon>
          mdi-content-copy
        </v-icon>
      </v-btn>
      <v-btn
        small
        text
        :disabled="index == 0"
        @click.stop="onWidgetMoveToTopClick(index)"
      >
        <v-icon>
          mdi-chevron-up
        </v-icon>
      </v-btn>
      <v-btn
        small
        text
        :disabled="index == data.list.length - 1"
        @click.stop="onWidgetMoveToBottomClick(index)"
      >
        <v-icon>
          mdi-chevron-down
        </v-icon>
      </v-btn>
      <v-btn
        small
        text
        @click.stop="onWidgetItemDelete(index)"
      >
        <v-icon>
          mdi-delete
        </v-icon>
      </v-btn>

      <v-btn
        small
        text
        @click.stop="onWidgetItemSettingsClick(index)"
      >
        <v-icon>
          mdi-cog
        </v-icon>
      </v-btn>
    </div>

    <div
      v-if="selectedWidget.key == element.key"
      class="widget-view-drag"
    >
      <v-icon>mdi-drag</v-icon>
    </div>
  </v-container>
</template>

<script>
import { genUniqKey } from "@/util/form-builder";

export default {
  props: ["element", "select", "index", "data"],
  data() {
    return {
      selectedWidget: this.select,
    };
  },
  computed: {
    hasSelectedWidget() {
      return (
        !!this.selectedWidget && Object.keys(this.selectedWidget).length > 0
      );
    },
    hasElement() {
      return !!this.element;
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
  methods: {
    onWidgetMoveToTopClick(index) {
      this.$emit("click:moveTop", index);
    },
    onWidgetMoveToBottomClick(index) {
      this.$emit("click:moveBottom", index);
    },
    onWidgetItemClick(index) {
      this.selectedWidget = { ...this.data.list[index] };
    },
    onWidgetItemDelete(index) {
      this.selectedWidget = null;
      this.$emit("click:delete", index);
    },
    onWidgetItemSettingsClick(index) {
      this.$emit("click:settings", index);
    },
    onWidgetItemClone(index) {
      let cloneData = {
        ...this.data.list[index],
        options: { ...this.data.list[index].options },
        key: genUniqKey(),
        order: index + 1,
      };
      this.$emit("click:clone", { widget: cloneData, index: index });
      this.$nextTick(() => {
        this.selectedWidget = this.data.list[index + 1];
      });
    },
  },
};
</script>

<style lang="scss" scoped>
.widget-view {
  &.active {
    background-color: $light-gray;
  }

  &:hover {
    background-color: $light-gray;
  }
}
</style>
