<template>
  <div class="detail-responses">
    <v-container
      fluid
      tag="section"
      class="pa-5"
    >
      <v-row
        justify="start"
        class="mt-2"
      >
        <v-col
          cols="7"
          class="text-left detail-responses__info"
        >
          <h1 class="title">{{ survey.data.title }} </h1>
          <p class="ma-0 description text-secondary">{{ survey.data.description }} </p>
        </v-col>
        <v-col
          cols="5"
          class="text-right"
        >
          <v-btn
            :block="isMobile"
            small
            height="44"
            :disabled="!filteredResponses.length"
            class="v-btn--accent"
            @click="onClickDownloadButton"
          >
            <v-icon class="pr-1">
              mdi-download
            </v-icon>
            DOWNLOAD AS CSV
          </v-btn>
        </v-col>
        <v-col
          cols="12"
          class="mt-10"
        >
          <v-data-table
            :headers="tableHeaders"
            :items="filteredResponses"
            item-key="name"
            class="detail-responses-table"
            :search="keyword"
          >
            <template #top>
              <v-row
                justify="start"
                class="detail-responses-table__top"
              >
                <v-col cols="auto">
                  <v-text-field
                    v-model.trim="keyword"
                    rounded
                    :background-color="style.color.lightBlue"
                    solo
                    dense
                    outlined
                    class="detail-responses-search mb-2"
                    :class="[isMobile? '--is-mobile' : '--is-desktop']"
                    prepend-inner-icon="mdi-magnify"
                    label="Search responses..."
                  />
                </v-col>
              </v-row>
            </template>
            <template #item.submissionDate="{ item }">
              {{ item.submissionDate | standardDate }}
            </template>
          </v-data-table>

        </v-col>

      </v-row>
    </v-container>
  </div>
</template>

<script>
import surveyDataSample from "@/assets/json/survey-data-sample.json";

export default {
  name: "DetailResponses",
  data() {
    return {
      surveyDataSample,
      keyword: "",
      responses: [],
      survey: {
        data: {
          title: "",
          description: "",
          formBuilder: {
            list: [],
            models: {},
          },
        },
        config: {},
      },
    };
  },
  created() {
    this.survey = { ...this.survey, ...surveyDataSample };
    this.createMockResponses();
  },
  computed: {
    filteredResponses() {
      let responses = this.keyword
        ? this.responses.filter((response) => {
            return JSON.stringify(response)
              .toLowerCase()
              .includes(this.keyword);
          })
        : this.responses;
      return responses;
    },
    tableHeaders() {
      const headers = [
        { text: "Submission date", value: "submissionDate", width: 150 },
      ];
      const questions = this.survey.data.formBuilder.list.map(
        (widget, index) => {
          let question = `Q${index + 1}: ${
            widget.question || "No question given"
          }`;
          return {
            text: question,
            value: widget.model,
            width: 200,
          };
        }
      );

      return headers.concat(questions);
    },
  },
  methods: {
    onClickDownloadButton() {
      // do something
      // fetch the api
      this.$notify.toast("File has been downloaded");
    },
    createMockResponses() {
      let responses = [];
      let models = _.cloneDeep(this.survey.data.formBuilder.models);
      for (let i = 0; i < 10; i++) {
        models["submissionDate"] = "2022-06-11 00:00:00.123456+00:00";
        responses.push(models);
      }
      responses.forEach((response) => {
        Object.keys(response).forEach((model) => {
          const widget = this.survey.data.formBuilder.list.find(
            (formWidget) => formWidget.model === model
          );
          if (model.includes("radio")) {
            let option = widget.options.options.find(
              (option) => option.value === response[model]
            );
            response[model] = option ? option.text : response[model];
          }
        });
      });

      this.responses = _.cloneDeep(responses);
      console.log(JSON.stringify(this.responses));
    },
  },
};
</script>
<style lang="scss">
.detail-responses-table {
  &__top {
    background-color: $light-blue;
    margin: 0;
    overflow: hidden;
  }

  .v-data-table-header {
    background-color: $light-blue;

    th[role="columnheader"] {
      text-transform: uppercase;
      vertical-align: top;

      > span {
        font-weight: 600;
      }
    }
  }
}

.detail-responses-search {
  &.--is-desktop {
    .v-input__slot {
      box-shadow: none !important;
      border: 1px solid $light-gray;
    }
  }

  .v-text-field__details {
    display: none;
  }
}

.detail-responses {
  &__info {
    .title {
      @include font-size(1.5);
    }

    .description {
      @include font-size(1);
    }
  }
}
</style>
