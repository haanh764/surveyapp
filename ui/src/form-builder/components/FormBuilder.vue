<template>
  <v-container class="form-builder">
    <v-row justify="center">
      <v-col
        class="fm2-main"
        cols="12"
      >
        <v-container>
          <v-row justify="center">
            <v-col cols="12">
              <v-btn
                text
                @click="onClearButtonClick"
              >
                <v-icon>mdi-delete</v-icon>
                clear
              </v-btn>
              <v-btn @click="onCopyButtonClick(true)">
                <v-icon>mdi-copy</v-icon>
                copy
              </v-btn>
              <v-btn @click="onCopyJsonButtonClick">
                <v-icon>mdi-ticket</v-icon>
                get json
              </v-btn>
            </v-col>

            <v-col
              cols="12"
              :class="{'widget-empty': widgetForm.list.length == 0}"
            >
              <widget-form
                ref="widgetForm"
                :data="widgetForm"
                :select.sync="selectedWidget"
                @update:addWidget="onAddNewWidget"
                @click:settings="onWidgetItemSettingsClick"
                @click:delete="onWidgetItemDeleteClick"
              />
            </v-col>
          </v-row>
        </v-container>
      </v-col>
    </v-row>
    <modal
      v-model="isWidgetSettingModalShown"
      :is-close-button-shown="true"
    >
      <v-card elevation="0">
        <widget-config
          :selected-widget.sync="selectedWidget"
          @update:selectedWidget="updateSelectedWidgetInList"
          @update:removeOptions="onRemoveOptionsFromSelectedWidget"
          @update:addOption="onAddOptionToSelectedWidget"
        />
      </v-card>
    </modal>
  </v-container>
</template>

<script>
import WidgetConfig from "./WidgetConfig";
import WidgetForm from "./WidgetForm";
import GenerateForm from "./GenerateForm";
import { basicComponents } from "./components.js";
import genFormCode from "@/form-builder/generator/generateFormCode";
import copyText from "@/util/copy";

export default {
  name: "FormBuilder",
  components: {
    WidgetConfig,
    WidgetForm,
    GenerateForm
  },
  data() {
    return {
      isWidgetSettingModalShown: false,
      basicComponents,
      widgetForm: {
        list: []
      },
      copiedHtml: "",
      configTab: "widget",
      selectedWidget: null,
      widgetModels: {},
      jsonTemplate: "",
      jsonCopyValue: ""
    };
  },
  mounted() {
    this._loadComponents();
  },
  methods: {
    onWidgetItemDeleteClick(index) {
      if (this.widgetForm.list[index]) {
        this.widgetForm.list.splice(index, 1);
      }
    },
    onWidgetItemSettingsClick(index) {
      this.selectedWidget = this.widgetForm.list[index];
      this.$nextTick(() => {
        this.isWidgetSettingModalShown = true;
      });
    },
    onAddNewWidget({ widget, oldIndex }) {
      widget.order = oldIndex;
      this.widgetForm.list.splice(oldIndex, 0, widget);
    },
    onAddOptionToSelectedWidget() {
      this.selectedWidget.options.options.push({
        value: "option",
        text: "option"
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
    _loadComponents() {
      this.basicComponents = this.basicComponents.map((item) => {
        return {
          ...item,
          name: item.type
        };
      });
    },
    handleMoveEnd(evt) {
      console.log("end", evt);
    },
    handleMoveStart({ oldIndex }) {
      console.log("start", oldIndex, this.basicComponents);
    },
    handleMove() {
      return true;
    },
    handlePreview() {
      try {
        new RegExp(this.data.options.pattern);
      } catch (e) {
        console.error("preview error");
      }
    },
    handleTest() {
      this.$refs.generateForm
        .getData()
        .then((data) => {
          console.log(data);
          this.$refs.widgetPreview.end();
        })
        .catch((e) => {
          console.error(e);
          this.$refs.widgetPreview.end();
        });
    },
    handleReset() {
      this.$refs.generateForm.reset();
    },
    onCopyJsonButtonClick() {
      this.jsonTemplate = this.widgetForm;
      const widgets = this.widgetForm.list.map(
        // eslint-disable-next-line no-unused-vars
        ({ asset, ...widget }) => widget
      );
      console.log("form builder json", JSON.stringify(widgets));

      return widgets;
    },
    copyJsonDataHandler() {
      const cpSuccess = copyText(this.jsonCopyValue);
      if (cpSuccess) {
        console.log("copy successful");
      }
    },
    onClearButtonClick() {
      this.widgetForm = {
        list: []
      };
      this.selectedWidget = null;
    },
    getJSON() {
      return this.widgetForm;
    },
    setJSON(json) {
      this.widgetForm = json;

      if (json.list.length > 0) {
        this.selectedWidget = json.list[0];
      }
    },
    updateSelectedWidgetInList(val) {
      if (val) {
        this.selectedWidget = { ...val };
        let widgetIndex = this.widgetForm.list.findIndex(
          (widget) => widget.key == val.key
        );
        this.widgetForm.list[widgetIndex] = { ...val };
      }
    },
    onCopyButtonClick(flag) {
      let code = "";
      if (flag) {
        code = genFormCode(this.widgetForm, this.widgetModels);
      } else {
        code = decodeURIComponent(this.$refs.codeRunRef.code);
      }
      const cpSuccess = copyText(code);
      this.copiedHtml = code;

      if (cpSuccess) {
        console.log("copy successful");
      }
    }
  }
};
</script>

<style lang="scss">
</style>
