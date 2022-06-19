<template>
  <v-container
    fluid
    tag="section"
    class="form-builder"
  >
    <v-row justify="center">
      <v-col
        cols="12"
        class="pa-0 mb-10"
      >
        <v-container>
          <v-row justify="center">
            <v-col
              cols="12"
              class="pa-3 text-right"
            >
              <v-btn
                text
                small
                class="text-none"
                @click="onClearButtonClick"
              >
                <v-icon small>
                  mdi-delete
                </v-icon>
                <span class="">Clear form</span>
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
                @update:moveWidget="onMoveNewWidget"
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
      :title="widgetSettingModalTitle"
      primary-action-button-text="save"
      subtitle="All changes are immediately applied"
      @click:primary-action="isWidgetSettingModalShown = false"
    >
      <v-container
        fluid
        tag="section"
      >
        <v-row justify="center">
          <v-col
            cols="10"
            class="pa-0"
          >
            <v-card elevation="0">
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
          </v-col>
        </v-row>
      </v-container>
    </modal>

    <bottom-sheet
      ref="widgetSettingBottomSheet"
      v-model="isWidgetSettingBottomSheetShown"
      :title="widgetSettingModalTitle"
      :fullscreen="true"
      align-title="center"
    >
      <template #content>
        <widget-config
          :key="widgetConfigKey"
          :selected-widget.sync="selectedWidget"
          @update:selectedWidget="updateSelectedWidgetInList"
          @update:removeOptions="onRemoveOptionsFromSelectedWidget"
          @update:addOption="onAddOptionToSelectedWidget"
        />
      </template>
    </bottom-sheet>
  </v-container>
</template>

<script>
import WidgetConfig from "./WidgetConfig";
import WidgetForm from "./WidgetForm";
import { EventBus } from "@/util/event-bus";

export default {
  name: "FormBuilder",
  components: {
    WidgetConfig,
    WidgetForm
  },
  props: {
    value: {
      type: Object,
      default() {
        return {};
      }
    },
    survey: {
      type: Object,
      default() {
        return {
          data: {
            title: "",
            description: "",
            formBuilder: {
              list: [],
              models: {}
            }
          },
          config: {}
        };
      }
    }
  },
  data() {
    return {
      isWidgetSettingBottomSheetShown: false,
      isWidgetSettingModalShown: false,
      widgetForm: {
        list: [],
        models: {}
      },
      copiedHtml: "",
      selectedWidget: null,
      widgetFormComponentKey: 1,
      widgetConfigKey: 1,
      jsonTemplate: "",
      jsonCopyValue: ""
    };
  },
  computed: {
    filteredWidgets() {
      return this.widgetForm.list.filter((widget) => !!widget.key);
    },
    widgetSettingModalTitle() {
      return this.selectedWidget
        ? `${this.selectedWidget.label} question settings`
        : "Title";
    }
  },
  watch: {
    "widgetForm.list": {
      deep: true,
      handler() {
        this.setModels();
        this.$nextTick(() => {
          this.$emit("input", this.widgetForm);
        });
      }
    }
  },
  created() {
    this.setFormBuilderDataFromSurveyProp();
  },
  mounted() {
    this.startListeningToEventBus();
  },
  beforeDestroy() {
    this.stopListeningToEventBus();
  },
  methods: {
    setModels() {
      let models = {};
      this.widgetForm.list.forEach((widget) => {
        models[widget.model] = widget.options.defaultValue || "";
      });
      this.widgetForm.models = { ...models };
    },
    setFormBuilderDataFromSurveyProp() {
      this.widgetForm = {
        ...this.widgetForm,
        ...this.survey.data.formBuilder
      };
      this.selectedWidget =
        this.selectedWidget ||
        (this.widgetForm.list.length
          ? this.widgetForm.list[0]
          : null);
      this.widgetFormComponentKey += 1;
      // should I increment widgetConfigKey as well?
    },
    startListeningToEventBus() {
      EventBus.$on("update:addWidget", this.onAddNewWidget);
      EventBus.$on("event:setFormBuilderDataFromProp", () => {
        this.setFormBuilderDataFromSurveyProp();
      });
    },
    stopListeningToEventBus() {
      EventBus.$off("update:addWidget");
      EventBus.$off("event:setFormBuilderDataFromProp");
    },
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
        if (this.isMobile) {
          this.isWidgetSettingBottomSheetShown = true;
        } else {
          this.isWidgetSettingModalShown = true;
        }
      });
    },
    onAddNewWidget({ widget, index }) {
      if (this.filteredWidgets.length >= 100) {
        this.$notify.toast("Maximum 100 elements reached");
      } else {
        this.widgetForm.list.splice(index, 0, widget);
        this.selectedWidget = widget;
        this.widgetFormComponentKey += 1;
      }
    },
    onMoveNewWidget({ oldIndex, newIndex }) {
      const oldIndexWidget = this.widgetForm.list[oldIndex];
      const newIndexWidget = this.widgetForm.list[newIndex];

      this.widgetForm.list[oldIndex] = { ...newIndexWidget };
      this.widgetForm.list[newIndex] = { ...oldIndexWidget };

      this.selectedWidget = oldIndexWidget;

      this.widgetFormComponentKey += 1;
    },
    onAddOptionToSelectedWidget(newOption) {
      this.selectedWidget.options.options.push(newOption);
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
    onClearButtonClick() {
      this.widgetForm = {
        list: [],
        models: {}
      };
      this.selectedWidget = null;
      this.widgetFormComponentKey += 1;
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
          this.setModels();
        });
      }
    }
  }
};
</script>

<style lang="scss">
.form-builder {
  margin-bottom: calculate-space(10);
}
</style>
