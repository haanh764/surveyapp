<template>
  <div>
    <div v-if="hasSelectedWidget">
      <template v-if="isWidgetQuestionShown">
        <v-text-field
          v-model="question"
          dense
          outlined
          label="Question"
          placeholder="Survey question"
        />
        <v-text-field
          v-model="description"
          dense
          outlined
          label="Description"
          placeholder="Survey description"
        />
      </template>

      <template v-if="isTextInputWidget && hasNestedProperty(selectedWidget, 'options.placeholder')">
        <v-text-field
          v-model="placeholder"
          dense
          outlined
          label="placeholder"
        />
      </template>

      <template v-if="isSliderWidget">
        <div v-if="hasNestedProperty(selectedWidget, 'options.min')">
          <v-text-field
            v-model.number="min"
            dense
            outlined
            label="min"
            placeholder="min"
          />
        </div>
        <div v-if="hasNestedProperty(selectedWidget, 'options.max')">
          <v-text-field
            v-model.number="max"
            dense
            outlined
            label="max"
          />
        </div>
        <div v-if="hasNestedProperty(selectedWidget, 'options.step')">
          <v-text-field
            v-model.number="step"
            dense
            outlined
            label="step"
          />
        </div>
      </template>

      <template v-if="isOptionWidget">
        <template v-if="selectedWidget.type=='radio' ">
          <v-radio-group v-model="options.defaultValue">
            <li
              v-for="(item, index) in selectedWidget.options.options"
              :key="index"
            >
              {{ index + 1 }}

              <v-text-field
                v-model="item.value"
                dense
                outlined
                label="value"
              />
              <v-text-field
                v-model="item.text"
                dense
                outlined
                label="label"
              />
              <v-btn
                small
                fab
                text
                @click="handleOptionsRemove(index)"
              >
                <v-icon>
                  mdi-minus
                </v-icon>
              </v-btn>
            </li>
          </v-radio-group>
        </template>

        <template v-if="selectedWidget.type=='checkbox'">
          <v-item-group v-model="options.defaultValue">
            <li
              v-for="(item, index) in selectedWidget.options.options"
              :key="index"
            >
              {{ index + 1 }}

              <v-text-field
                v-model="item.value"
                dense
                outlined
                label="value"
              />
              <v-text-field
                v-model="item.text"
                dense
                outlined
                label="label"
              />
              <v-btn
                circle
                plain
                type="danger"
                size="mini"
                style="padding: 4px;margin-left: 5px;"
                @click="handleOptionsRemove(index)"
              >
                <v-icon>
                  mdi-minus
                </v-icon>
              </v-btn>
            </li>
          </v-item-group>
        </template>

        <div>
          <v-btn
            text
            small
            @click="handleAddOption"
          >
            add option
          </v-btn>
        </div>
      </template>

      <template v-if="hasTextDefaultValue">
        <v-text-field
          v-model="defaultValue"
          dense
          outlined
          label="Default value"
        />
      </template>
    </div>
    <div v-else>
      No widget selected
    </div>
  </div>
</template>

<script>
export default {
  name: "WidgetConfig",
  props: {
    selectedWidget: {
      type: Object,
      default() {
        return {};
      }
    }
  },
  // very dirty, but nothing can be done
  // should be refactored sometime
  // somehow vue is buggy on this component only
  // deep watching the options data wont work
  // and v-model doesnt work on object property
  data() {
    return {
      question: "",
      description: "",
      placeholder: "",
      step: "",
      min: "",
      defaultValue: "",
      max: "",
      options: []
    };
  },
  computed: {
    isWidgetQuestionShown() {
      return this.selectedWidget.type && this.selectedWidget.type != "text";
    },
    isOptionWidget() {
      const optionWidgets = [ "checkbox", "radio" ];
      return (
        !!this.selectedWidget &&
        optionWidgets.includes(this.selectedWidget.type)
      );
    },
    isTextInputWidget() {
      return !!this.selectedWidget && this.selectedWidget.type == "input";
    },
    isSliderWidget() {
      return !!this.selectedWidget && this.selectedWidget.type == "slider";
    },
    hasSelectedWidget() {
      return this.selectedWidget && Object.keys(this.selectedWidget).length > 0;
    },
    hasTextDefaultValue() {
      const textDefaultValueWidgets = [ "text", "input", "textarea" ];
      return (
        this.hasSelectedWidget &&
        textDefaultValueWidgets.includes(this.selectedWidget.type)
      );
    }
  },
  watch: {
    question(val) {
      this.emitChange({ question: val });
    },
    description(val) {
      this.emitChange({ description: val });
    },
    defaultValue(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ defaultValue: val } }
      });
    },
    min(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ min: val } }
      });
    },
    max(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ max: val } }
      });
    },
    step(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ step: val } }
      });
    },
    placeholder(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ placeholder: val } }
      });
    },
    selectedWidget: {
      deep: true,
      handler(val) {
        if (val && Object.keys(val).length > 0) {
          let { question, description, options } = val;
          this.question = question;
          this.description = description;
          this.min = options.min;
          this.max = options.max;
          this.step = options.step;
          this.placeholder = options.placeholder;
          this.defaultValue = options.defaultValue;
        }
      }
    }
  },
  created() {
    if (
      !!this.selectedWidget &&
      this.hasNestedProperty(this.selectedWidget, "options.options")
    ) {
      this.options = { ...this.selectedWidget.options.options };
    }
  },
  methods: {
    hasNestedProperty(obj, propertyPath) {
      if (!propertyPath) return false;
      var properties = propertyPath.split(".");
      for (var i = 0; i < properties.length; i++) {
        var prop = properties[i];

        // eslint-disable-next-line no-prototype-builtins
        if (!obj || !obj.hasOwnProperty(prop)) {
          return false;
        } else {
          obj = obj[prop];
        }
      }

      return true;
    },
    emitChange(updatedValue) {
      this.$emit("update:selectedWidget", {
        ...this.selectedWidget,
        ...updatedValue
      });
    },
    handleOptionsRemove(index) {
      this.$emit("update:removeOptions", index);
    },
    handleAddOption() {
      this.$emit("update:addOption", { value: "option", text: "option" });
    }
  }
};
</script>
