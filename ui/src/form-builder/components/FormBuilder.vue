<template>
  <v-container
    fluid
    tag="section"
    class="form-builder"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        class="pa-0"
      >
        <v-container>
          <v-row justify="center">
            <v-col
              cols="12"
              class="pb-10 text-right"
            >
              <v-btn
                text
                small
                @click="onClearButtonClick"
              >
                <v-icon>mdi-delete</v-icon>
                clear
              </v-btn>
              <v-btn
                text
                small
                @click="onCopyJsonButtonClick"
              >
                <v-icon>mdi-ticket</v-icon>
                get json
              </v-btn>
            </v-col>

            <v-col
              cols="12"
              class="pa-0 widget-form-col"
              :class="{'--is-empty': widgetForm.list.length == 0}"
            >
              <widget-form
                ref="widgetForm"
                :key="widgetFormComponentKey"
                :data="widgetForm"
                :select.sync="selectedWidget"
                @update:addWidget="onAddNewWidget"
                @click:moveTop="onWidgetItemMoveTopClick"
                @click:moveBottom="onWidgetItemMoveBottomClick"
                @click:settings="onWidgetItemSettingsClick"
                @click:delete="onWidgetItemDeleteClick"
              />
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>

    <modal
      ref="widgetSettingModal"
      v-model="isWidgetSettingModalShown"
      :is-close-button-shown="true"
    >
      <v-card elevation="0">
        <v-card-title>
          Survey item configuration
        </v-card-title>
        <v-card-text>
          <widget-config
            :key="widgetConfigKey"
            :selected-widget.sync="selectedWidget"
            @update:selectedWidget="updateSelectedWidgetInList"
            @update:removeOptions="onRemoveOptionsFromSelectedWidget"
            @update:addOption="onAddOptionToSelectedWidget"
          />
        </v-card-text>
      </v-card>
    </modal>
  </v-container>
</template>

<script>
import WidgetConfig from "./WidgetConfig";
import WidgetForm from "./WidgetForm";
import GenerateForm from "./GenerateForm";
import genFormCode from "@/form-builder/generator/generateFormCode";
import copyText from "@/util/copy";

export default {
  name: "FormBuilder",
  components: {
    WidgetConfig,
    WidgetForm,
    GenerateForm,
  },
  props: {
    value: {
      type: Array,
      default() {
        return [];
      },
    },
    survey: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      isWidgetSettingModalShown: false,
      widgetForm: {
        list: [],
      },
      copiedHtml: "",
      selectedWidget: null,
      widgetModels: {},
      widgetFormComponentKey: 1,
      widgetConfigKey: 1,
      jsonTemplate: "",
      jsonCopyValue: "",
    };
  },
  watch: {
    "widgetForm.list": {
      deep: true,
      handler(val) {
        this.$emit("input", val);
      },
    },
  },
  methods: {
    onWidgetItemMoveBottomClick(index) {
      const prevBottomWidget = this.widgetForm.list[index + 1];
      this.widgetForm.list[index + 1] = this.widgetForm.list[index];
      this.widgetForm.list[index] = prevBottomWidget;
      this.widgetFormComponentKey += 1;
    },
    onWidgetItemMoveTopClick(index) {
      const prevTopWidget = this.widgetForm.list[index - 1];
      this.widgetForm.list[index - 1] = this.widgetForm.list[index];
      this.widgetForm.list[index] = prevTopWidget;
      this.widgetFormComponentKey += 1;
    },
    onWidgetItemDeleteClick(index) {
      if (this.widgetForm.list[index]) {
        this.widgetForm.list.splice(index, 1);
        this.widgetFormComponentKey += 1;
      }
    },
    onWidgetItemSettingsClick(index) {
      this.selectedWidget = this.widgetForm.list[index];
      this.widgetConfigKey += 1;
      this.$nextTick(() => {
        this.isWidgetSettingModalShown = true;
      });
    },
    onAddNewWidget({ widget, index }) {
      // still buggy
      // somehow some widgets are added twice
      this.widgetForm.list.splice(index, 0, widget);
    },
    onAddOptionToSelectedWidget() {
      this.selectedWidget.options.options.push({
        value: "option",
        text: "option",
      });
      this.$nextTick(() => {
        this.updateSelectedWidgetInList(this.selectedWidget);
      });
    },
    onRemoveOptionsFromSelectedWidget(optionIndex) {
      this.selectedWidget.options.options.splice(optionIndex, 1);
      this.$nextTick(() => {
        this.updateSelectedWidgetInList(this.selectedWidget);
      });
    },
    onCopyJsonButtonClick() {
      this.jsonTemplate = this.widgetForm;
      const widgets = this.widgetForm.list
        .map(
          // eslint-disable-next-line no-unused-vars
          ({ asset, ...widget }) => widget
        )
        .filter((widget) => !!widget.key)
        .map((widget, index) => {
          return {
            ...widget,
            order: index,
            model: widget.model ? widget.model : `${widget.type}_${widget.key}`,
          };
        });
      copyText(JSON.stringify(widgets));
      console.log("form builder json", JSON.stringify(widgets));
      return widgets;
    },
    onClearButtonClick() {
      this.widgetForm = {
        list: [],
      };
      this.selectedWidget = null;
    },
    updateSelectedWidgetInList(val) {
      if (val) {
        this.selectedWidget = { ...val };
        let widgetIndex = this.widgetForm.list.findIndex(
          (widget) => widget.key == val.key
        );

        this.widgetForm.list[widgetIndex] = { ...val };
        this.$nextTick(() => {
          this.widgetFormComponentKey += 1;
        });
      }
    },
    onCopyButtonClick() {
      let code = genFormCode(this.widgetForm, this.widgetModels);
      this.copiedHtml = code;

      const cpSuccess = copyText(code);
      if (cpSuccess) {
        console.log("copy successful", code);
      }
    },
  },
};
</script>

<style lang="scss">
.form-builder {
}
</style>
