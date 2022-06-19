<template>
  <div>
    <v-tabs
      v-model="tab"
      class="survey-tab "
      :centered="isMobile"
      :grow="isMobile"
      @change="$emit('input', tab)"
    >
      <v-tabs-slider color="primary" />
      <v-tab
        v-for="item in items"
        :key="item.title"
      >
        {{ item.title }}
      </v-tab>
    </v-tabs>
    <v-tabs-items v-model="tab">
      <v-tab-item
        v-for="item in items"
        :key="item.title"
      >
        <component
          :is="item.component"
          :ref="item.ref"
          :survey="survey"
          :value="formData"
          @input="setFormData"
        />
      </v-tab-item>
    </v-tabs-items>
  </div>
</template>

<script>
import SurveyBuild from "@views/user/survey-edit/components/SurveyBuild.vue";
import SurveyPreview from "@views/user/survey-edit/components/SurveyPreview.vue";
import { EventBus } from "@/util/event-bus";

export default {
  name: "SurveyEditTabs",
  components: {
    SurveyBuild,
    SurveyPreview
  },
  props: {
    value: {
      type: Number,
      default: 0
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
      tab: 0,
      componentKey: 1,
      formData: {
        title: "",
        description: "",
        formBuilder: {
          list: [],
          models: {}
        }
      },
      items: [
        {
          title: "Build",
          component: SurveyBuild,
          ref: "surveyBuild"
        },
        {
          title: "Preview",
          component: SurveyPreview,
          ref: "surveyPreview"
        }
      ]
    };
  },
  created() {
    this.setFormBuilderDataFromSurveyProp();
  },
  mounted() {
    this.mountListeners();
  },
  beforeDestroy() {
    this.destroyListeners();
  },
  methods: {
    setFormBuilderDataFromSurveyProp() {
      this.formData = {
        ...this.formData,
        ...this.survey.data
      };
    },
    destroyListeners() {
      EventBus.$off("event:getFormBuilderData");
    },
    mountListeners() {
      EventBus.$on("event:getFormBuilderData", () => {
        EventBus.$emit("event:setFormBuilderData", {
          data: this.formData,
          key: "data"
        });
      });
    },
    setFormData(formData) {
      this.formData = { ...this.formData, ...formData };
      this.$nextTick(() => {
        this.componentKey += 1;
      });
    },
    getData() {
      return this.formData;
    }
  }
};
</script>
