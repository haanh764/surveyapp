<template>
  <v-container
    fluid
    tag="section"
    class="widget-config"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class=""
      >
        <v-row v-if="hasSelectedWidget">
          <v-col
            v-if="isWidgetQuestionShown"
            cols="12"
            class="py-0"
          >
            <v-text-field
              v-model="question"
              :dense="isMobile"
              outlined
              label="Question"
              placeholder="Survey question"
            />
            <v-text-field
              v-model="description"
              :dense="isMobile"
              outlined
              label="Description"
              placeholder="Survey description"
            />
          </v-col>
          <v-col
            v-if="isTextInputWidget && hasNestedProperty(selectedWidget, 'options.placeholder')"
            cols="12"
            class="py-0"
          >
            <v-text-field
              v-model="placeholder"
              :dense="isMobile"
              outlined
              label="placeholder"
            />
          </v-col>
          <template v-if="isSliderWidget">
            <v-divider />
            <v-col
              v-if="hasNestedProperty(selectedWidget, 'options.min')"
              cols="4"
            >
              <v-text-field
                v-model.number="min"
                :dense="isMobile"
                outlined
                label="min"
                placeholder="min"
              />
            </v-col>
            <v-col
              v-if="hasNestedProperty(selectedWidget, 'options.max')"
              cols="4"
            >
              <v-text-field
                v-model.number="max"
                :dense="isMobile"
                outlined
                label="max"
              />
            </v-col>
            <v-col
              v-if="hasNestedProperty(selectedWidget, 'options.step')"
              cols="4"
            >
              <v-text-field
                v-model.number="step"
                :dense="isMobile"
                outlined
                label="step"
              />
            </v-col>
          </template>

          <template v-if="isOptionWidget">
            <v-col
              v-if="selectedWidget.type=='radio' || selectedWidget.type=='checkbox' "
              cols="12"
              class="py-0"
            >
              <template v-for="(item, index) in selectedWidget.options.options">
                <v-row
                  :key="`${selectedWidget.type}-group_${index}`"
                  justify="start"
                >
                  <v-col cols="1">
                    <span>
                      {{ index + 1 }}
                    </span>
                  </v-col>
                  <v-col cols="4">
                    <v-text-field
                      v-model="item.value"
                      :dense="isMobile"
                      outlined
                      label="value"
                    />
                  </v-col>
                  <v-col cols="5">
                    <v-text-field
                      v-model="item.text"
                      :dense="isMobile"
                      outlined
                      label="label"
                    />
                  </v-col>
                  <v-col
                    class="text-center"
                    cols="1"
                  >
                    <v-btn
                      small
                      text
                      :disabled="selectedWidget.options.options.length == 1"
                      @click="handleOptionsRemove(index)"
                    >
                      <v-icon>
                        mdi-minus
                      </v-icon>
                    </v-btn>
                  </v-col>
                </v-row>
              </template>
            </v-col>

            <v-col
              cols="12"
              class="text-right py-0"
            >
              <v-btn
                text
                small
                class="text-none text-normal pa-0 "
                :disabled="selectedWidget.options.options.length >= 20"
                @click="handleAddOption"
              >
                <u>Add option</u>
              </v-btn>
              <small
                v-if="selectedWidget.options.options.length >= 20"
                class="d-block text-error mt-2"
              >
                Maximum options (20) reached
              </small>
            </v-col>
          </template>

          <template v-if="hasTextDefaultValue">
            <v-col
              cols="12"
              :class="{'py-0' : selectedWidget.type != 'text'}"
            >
              <v-text-field
                v-model="defaultValue"
                :dense="isMobile"
                outlined
                label="Default value"
              />
            </v-col>
          </template>

          <template v-if="hasNumberDefaultValue">
            <v-col
              cols="12"
              class="py-0"
            >
              <v-text-field
                v-model.number="defaultValue"
                :dense="isMobile"
                outlined
                label="Default value"
              />
            </v-col>
          </template>

          <template v-if="hasOptionDefaultValue">
            <v-col cols="12">
              <v-select
                v-model="defaultValue"
                :dense="isMobile"
                :multiple="selectedWidget.type == 'checkbox'"
                outlined
                :items="selectedWidget.options.options"
                label="Default value"
              />
            </v-col>
          </template>
        </v-row>

        <div v-else>
          <p class="text-secondary">
            No widget is selected
          </p>
        </div>
      </v-col>
    </v-row>
  </v-container>
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
      const textDefaultValueWidgets = [ "text", "input" ];
      return (
        this.hasSelectedWidget &&
        textDefaultValueWidgets.includes(this.selectedWidget.type)
      );
    },
    hasNumberDefaultValue() {
      const textDefaultValueWidgets = [ "slider" ];
      return (
        this.hasSelectedWidget &&
        textDefaultValueWidgets.includes(this.selectedWidget.type)
      );
    },
    hasOptionDefaultValue() {
      const textDefaultValueWidgets = [ "checkbox", "radio" ];
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
          this.setFormData();
        }
      }
    }
  },
  created() {
    this.setFormData();
    if (
      !!this.selectedWidget &&
      this.hasNestedProperty(this.selectedWidget, "options.options")
    ) {
      this.options = { ...this.selectedWidget.options.options };
    }
  },
  methods: {
    setFormData() {
      let { question, description, options } = this.selectedWidget;
      this.question = question;
      this.description = description;

      this.min = options.min;
      this.max = options.max;
      this.step = options.step;
      this.placeholder = options.placeholder;
      this.defaultValue = options.defaultValue;
    },
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
      if (this.selectedWidget.type == "radio") {
        this.defaultValue = "";
      } else if (this.selectedWidget.type == "checkbox") {
        let option = this.selectedWidget.options.options[index];
        this.defaultValue = this.defaultValue.filter(
          (defVal) => defVal != option.value
        );
      }
      this.$emit("update:removeOptions", index);
    },
    handleAddOption() {
      let optionsLength = this.selectedWidget.options.options.length;
      this.$emit("update:addOption", {
        value: `option_${optionsLength + 1}`,
        text: `Option ${optionsLength + 1}`
      });
    }
  }
};
</script>
<style lang="scss" scoped>
.widget-config {
  max-height: 70vh;
  overflow-y: auto;
}
</style>
