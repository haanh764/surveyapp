<template>
  <v-container
    fluid
    tag="section"
    class="widget-config"
  >
    <v-row
      justify="start"
      class="pb-10"
    >
      <v-col cols="12">
        <v-row v-if="hasSelectedWidget">
          <v-col
            v-if="isWidgetQuestionShown"
            cols="12"
          >
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
          </v-col>
          <v-col
            v-if="isTextInputWidget && hasNestedProperty(selectedWidget, 'options.placeholder')"
            cols="12"
          >
            <v-text-field
              v-model="placeholder"
              dense
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
                dense
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
                dense
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
                dense
                outlined
                label="step"
              />
            </v-col>
          </template>

          <template v-if="isOptionWidget">
            <v-col
              v-if="selectedWidget.type=='radio' "
              cols="12"
            >
              <v-radio-group
                v-model="options.defaultValue"
                class="ma-0"
              >
                <template v-for="(item, index) in selectedWidget.options.options">
                  <v-row
                    :key="`radio-group_${index}`"
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
                        dense
                        outlined
                        label="value"
                      />
                    </v-col>
                    <v-col cols="5">
                      <v-text-field
                        v-model="item.text"
                        dense
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
                        @click="handleOptionsRemove(index)"
                      >
                        <v-icon>
                          mdi-minus
                        </v-icon>
                      </v-btn>
                    </v-col>
                  </v-row>
                </template>
              </v-radio-group>
            </v-col>

            <template v-if="selectedWidget.type=='checkbox'">
              <v-item-group v-model="options.defaultValue">
                <div
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
                </div>
              </v-item-group>
            </template>

            <v-col
              cols="12"
              class="text-right pa-0"
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
            </v-col>
          </template>

          <template v-if="hasTextDefaultValue">
            <v-text-field
              v-model="defaultValue"
              dense
              outlined
              label="Default value"
            />
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
      },
    },
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
      options: [],
    };
  },
  computed: {
    isWidgetQuestionShown() {
      return this.selectedWidget.type && this.selectedWidget.type != "text";
    },
    isOptionWidget() {
      const optionWidgets = ["checkbox", "radio"];
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
      const textDefaultValueWidgets = ["text", "input", "textarea"];
      return (
        this.hasSelectedWidget &&
        textDefaultValueWidgets.includes(this.selectedWidget.type)
      );
    },
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
        options: { ...this.selectedWidget.options, ...{ defaultValue: val } },
      });
    },
    min(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ min: val } },
      });
    },
    max(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ max: val } },
      });
    },
    step(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ step: val } },
      });
    },
    placeholder(val) {
      this.emitChange({
        options: { ...this.selectedWidget.options, ...{ placeholder: val } },
      });
    },
    selectedWidget: {
      deep: true,
      handler(val) {
        if (val && Object.keys(val).length > 0) {
          this.setFormData();
        }
      },
    },
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
        ...updatedValue,
      });
    },
    handleOptionsRemove(index) {
      this.$emit("update:removeOptions", index);
    },
    handleAddOption() {
      this.$emit("update:addOption", { value: "option", text: "option" });
    },
  },
};
</script>
<style lang="scss" scoped>
.widget-config {
  max-height: 300px;
  overflow-y: auto;
}
</style>
