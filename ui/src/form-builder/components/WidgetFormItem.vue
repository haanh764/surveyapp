<template>
  <v-container
    v-if="hasElement && hasSelectedWidget"
    class="widget-form-item"
    :class="[ selectedWidget.key == element.key && 'active', `widget--${element.type}` ]"
    :label="element.name"
    @click.stop="onWidgetItemClick(index)"
  >
    <v-row
      justify="start"
      class="widget-form-item__content"
    >
      <v-col cols="11">
        <div
          v-if="element.type != 'text'"
          class="text-left mb-5"
        >
          <h1
            class="mb-2 widget-form-item__question"
            :class="{'text-italic': !element.question}"
          >
            {{ element.question || 'Type a question...' }}
          </h1>
          <p
            class="text-secondary"
            :class="{'text-italic': !element.question}"
          >
            {{ element.description || 'Type a question description...' }}
          </p>
        </div>

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
              v-for="(item, optionIndex) in element.options.options"
              :key="item.value + optionIndex"
              disabled
              :label="item.text"
              :value="item.value"
            />
          </v-radio-group>
        </template>

        <template v-if="element.type == 'checkbox'">
          <v-item-group class="content__checkbox">
            <v-checkbox
              v-for="(item, optionIndex) in element.options.options"
              :key="item.value + optionIndex"
              v-model="element.options.defaultValue"
              disabled
              class="ma-0"
              :label="item.text"
              :value="item.value"
            >
              {{ item }}
            </v-checkbox>
          </v-item-group>
        </template>

        <template v-if="element.type=='slider'">
          <v-row
            justify="center"
            align="start"
            class="mt-5"
          >
            <v-col
              cols="2"
              class="text-center"
            >
              <small> {{ element.options.min }} </small>
            </v-col>
            <v-col cols="8">
              <v-slider
                v-model="element.options.defaultValue"
                :min="element.options.min"
                :max="element.options.max"
                disabled
                :step="element.options.step"
              />
            </v-col>
            <v-col
              cols="2"
              class="text-center"
            >
              <small>{{ element.options.max }}</small>
            </v-col>
          </v-row>
        </template>

        <template v-if="element.type == 'text'">
          <div class="text-left content__text">
            <h1 v-if="element.options.tag == 'h1'">
              {{ element.options.defaultValue }}
            </h1>
            <p
              v-if="element.options.tag == 'p'"
              class="text-secondary"
            >
              {{ element.options.defaultValue }}
            </p>
          </div>
        </template>
      </v-col>
      <v-col
        cols="1"
        class="drag-icon"
      >
        <v-icon>mdi-dots-vertical</v-icon>
      </v-col>
    </v-row>
    <v-row
      v-if="selectedWidget.key == element.key"
      justify="space-between"
      class="widget-form-item__actions"
    >
      <v-col
        cols="3"
        class="text-left action-button-group --left"
      >
        <v-btn
          small
          text
          class="settings-button"
          @click.stop="onWidgetItemSettingsClick(index)"
        >
          <v-icon
            small
            class="mr-2"
          >
            mdi-cog
          </v-icon>
          Settings
        </v-btn>
      </v-col>
      <v-col
        cols="9"
        class="pa-0 text-right action-button-group --right"
      >
        <v-btn
          small
          fab
          text
          outlined
          @click.stop="onWidgetItemClone(index)"
        >
          <v-icon small>
            mdi-content-copy
          </v-icon>
        </v-btn>
        <v-btn
          small
          text
          fab
          outlined
          :disabled="index == 0"
          @click.stop="onWidgetMoveToTopClick(index)"
        >
          <v-icon small>
            mdi-chevron-up
          </v-icon>
        </v-btn>
        <v-btn
          small
          fab
          outlined
          text
          :disabled="index == data.list.length - 1"
          @click.stop="onWidgetMoveToBottomClick(index)"
        >
          <v-icon small>
            mdi-chevron-down
          </v-icon>
        </v-btn>
        <v-btn
          small
          text
          fab
          outlined
          @click.stop="onWidgetItemDelete(index)"
        >
          <v-icon small>
            mdi-delete
          </v-icon>
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import { genUniqKey } from "@/util/form-builder";

export default {
  props: {
    element: {
      type: Object,
      default() {
        return {};
      }
    },
    select: {
      type: Object,
      default() {
        return {};
      }
    },
    index: {
      type: Number,
      default: 0
    },
    data: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  data() {
    return {
      selectedWidget: this.select
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
    }
  },
  watch: {
    select(val) {
      this.selectedWidget = val;
    },
    selectedWidget: {
      deep: true,
      handler(val) {
        this.$emit("update:select", val);
      }
    }
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
        order: index + 1
      };
      this.$emit("click:clone", { widget: cloneData, index: index });
      this.$nextTick(() => {
        this.selectedWidget = this.data.list[index + 1];
      });
    }
  }
};
</script>

<style lang="scss" scoped>
.widget-form-item {
  padding: 20px;

  &.active {
    border-top: 1px solid $light-gray;
    border-bottom: 1px solid $light-gray;
    background-color: transparentize($light-gray, 0.8);
    box-shadow: 0px 4px 4px rgba(0, 0, 0, 0.25);
  }

  &:hover {
    background-color: transparentize($light-gray, 0.5);
    cursor: grab;
  }

  &__question {
    @include font-size(1.5);
  }

  &__content {
    .drag-icon {
      align-self: center;
    }

    .content__checkbox {
      .v-input--checkbox .v-input__slot {
        margin: 0;
      }
    }

    .content__text {
      > h1 {
        @include font-size(1.5);
      }

      > p {
        @include font-size(1);
      }
    }
  }

  &__actions {
    .action-button-group {
      &.--left {
        .settings-button {
          font-weight: 400;
          text-transform: capitalize;
          letter-spacing: 0;
          border: 1px solid $light-gray;
          color: $dark-gray;
          @include font-size(0.875);
          border-radius: 15px;
        }
      }

      &.--right {
        display: flex;
        justify-content: flex-end;

        > * {
          // dirty // to be removed
          margin-right: 5px;

          &:last-child {
            margin-right: 10px;
          }
        }
      }
    }
  }

  &.widget {
    &--text {
    }

    &--input {
    }

    &--slider {
    }

    &--checkbox {
    }

    &--radio {
    }
  }
}
</style>
