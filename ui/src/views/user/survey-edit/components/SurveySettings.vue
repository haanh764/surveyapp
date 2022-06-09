<template>
  <v-container
    fluid
    tag="section"
    class="survey-settings"
  >
    <v-row justify="start">
      <v-col
        cols="12"
        class="text-left"
      >
        <h3 class="mt-5">
          Submission date
        </h3>
        <p class="text-secondary ">
          You can set start and end date of submission
        </p>
      </v-col>
      <v-col
        cols="12"
        class="pb-0"
      >
        <v-menu
          ref="startDateMenu"
          v-model="isStartDateMenuShown"
          :close-on-content-click="false"
          :return-value.sync="formData.startDate"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template #activator="{ on, attrs }">
            <v-text-field
              v-model="formData.startDate"
              outlined
              label="Start Date"
              :min="todayDate"
              v-bind="attrs"
              v-on="on"
            />
          </template>
          <v-date-picker
            v-model="formData.startDate"
            no-title
            scrollable
          >
            <v-spacer />
            <v-btn
              text
              color="primary"
              @click="isStartDateMenuShown = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.startDateMenu.save(formData.startDate)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
      <v-col
        cols="12"
        class="pt-0"
      >
        <v-menu
          ref="endDateMenu"
          v-model="isEndDateMenuShown"
          :close-on-content-click="false"
          :return-value.sync="formData.endDate"
          transition="scale-transition"
          offset-y
          min-width="auto"
        >
          <template #activator="{ on, attrs }">
            <v-text-field
              v-model="formData.endDate"
              outlined
              label="End Date"
              :min="formData.startDate"
              v-bind="attrs"
              v-on="on"
            />
          </template>
          <v-date-picker
            v-model="formData.endDate"
            no-title
            scrollable
          >
            <v-spacer />
            <v-btn
              text
              color="primary"
              @click="isEndDateMenuShown = false"
            >
              Cancel
            </v-btn>
            <v-btn
              text
              color="primary"
              @click="$refs.endDateMenu.save(formData.endDate)"
            >
              OK
            </v-btn>
          </v-date-picker>
        </v-menu>
      </v-col>
    </v-row>
    <v-row v-if="formData.isPublic">
      <v-col
        cols="12"
        class="text-left"
      >
        <h3>
          Public
        </h3>
        <v-row>
          <v-col cols="9">
            <p class="text-secondary">
              Share your survey to public.
            </p>
          </v-col>
          <v-col
            cols="3"
            class="justify-flex--end"
          >
            <v-switch v-model="formData.isPublic" />
          </v-col>
        </v-row>
        <div
          class="survey-link"
          @click="copyLinkToClipboard"
        >
          <a :href="survey.link">
            {{ survey.link || 'An error occured' }}
          </a>
          <v-icon>mdi-content-copy</v-icon>
        </div>
      </v-col>
    </v-row>
    <v-row v-else>
      <v-col
        cols="12"
        class="text-left"
      >
        <h3>
          Invite-only
        </h3>
        <v-row justify="space-between">
          <v-col cols="9">
            <p class="text-secondary">
              Share your survey only to selected participants by their email address. By default all surveys are public
            </p>
          </v-col>
          <v-col
            cols="3"
            class="text-center justify-flex--end"
          >
            <v-switch v-model="formData.isPublic" />
          </v-col>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        class="text-left"
      >
        <v-row justify="space-between">
          <v-col
            cols="9"
            class="align-flex--center"
          >
            <p class="text-secondary ma-0">
              Automatically send surveys to invited participants on start date
            </p>
          </v-col>
          <v-col
            cols="3"
            class="justify-flex--end"
          >
            <v-switch v-model="formData.isSurveySentAutomatically" />
          </v-col>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        class="text-left"
      >
        <ValidationProvider
          v-slot="{ errors }"
          name="E-mail"
          rules="email"
        >
          <v-text-field
            v-model.trim="newEmail"
            outlined
            :disabled="formData.emails.length >= 20"
            label="E-mail"
            placeholder="email@email.com"
            :error-messages="errors[0]"
            @keydown.enter="addNewEmail"
          />
        </ValidationProvider>

        <v-list>
          <v-list-item-group multiple>
            <template v-for="(item, i) in formData.emails">
              <v-list-item
                :key="`item-${i}`"
                :value="item"
                active-class="deep-purple--text text--accent-4"
              >
                <v-list-item-content>
                  <v-list-item-title class="text-left">
                    {{ item }}
                  </v-list-item-title>
                </v-list-item-content>

                <v-list-item-action>
                  <v-btn
                    icon
                    small
                    text
                    @click="removeEmail(i)"
                  >
                    <v-icon>mdi-minus</v-icon>
                  </v-btn>
                </v-list-item-action>
              </v-list-item>

              <v-divider
                v-if="i <= formData.emails.length - 2"
                :key="`divider-${i}`"
              />
            </template>
          </v-list-item-group>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import copyText from "@/util/copy.js";

export default {
  name: "SurveySettings",
  props: {
    survey: {
      type: Object,
      default() {
        return {
          link: "http://www.google.com",
        };
      },
    },
    value: {
      type: Object,
      default() {
        return {};
      },
    },
  },
  data() {
    return {
      isStartDateMenuShown: false,
      isEndDateMenuShown: false,
      // eslint-disable-next-line no-undef
      todayDate: moment().format("YYYY-MM-DD"),
      newEmail: "",
      formData: {
        startDate: "",
        endDate: "",
        isPublic: true,
        emails: [],
        isSurveySentAutomatically: false,
      },
    };
  },
  watch: {
    formData: {
      deep: true,
      handler() {
        this.$emit("input", this.formData);
      },
    },
  },
  mounted() {
    this.$emit("input", this.formData);
  },
  methods: {
    copyLinkToClipboard() {
      let isCopySuccessful = copyText(this.survey.link);
      if (isCopySuccessful) {
        this.$notify.toast("Link has been copied to clipboard");
      }
    },
    addNewEmail() {
      this.formData.emails.push(this.newEmail);
      this.newEmail = "";
    },
    removeEmail(index) {
      this.formData.emails.splice(index, 1);
    },
    getData() {
      return this.formData;
    },
  },
};
</script>

<style lang="scss">
.survey-settings {
  .survey-link {
    background-color: $grayish-white;
    padding: 20px;
    border: 1px solid $light-gray;
    display: flex;
    justify-content: space-between;
    text-align: left;

    &:hover {
      cursor: pointer;
      background-color: transparentize($light-gray, $amount: 0.5);
    }
  }
}
</style>
