<template>
  <v-container fluid>
    <v-row justify="start">
      <v-col
        cols="12"
        class="text-left"
      >
        <h3>
          Submission date
        </h3>
        <p class="text-secondary ">
          You can set start and end date of submission
        </p>
      </v-col>
      <v-col cols="12">
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
      <v-col cols="12">
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
          <v-col cols="8">
            <p class="text-secondary">
              Share your survey to public.
            </p>
          </v-col>
          <v-col cols="4">
            <v-switch v-model="formData.isPublic" />
          </v-col>
        </v-row>
        <div @click="copyLinkToClipboard">
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
        <v-row>
          <v-col cols="8">
            <p class="text-secondary">
              Share your survey only to selected participants by their email address. By default all surveys are public
            </p>
          </v-col>
          <v-col cols="4">
            <v-switch v-model="formData.isPublic" />
          </v-col>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        class="text-left"
      >
        <v-row>
          <v-col cols="8">
            <p>
              Automatically send surveys to invited participants on start date
            </p>
          </v-col>
          <v-col cols="4">
            <v-switch v-model="formData.isSurveySentAutomatically" />
          </v-col>
        </v-row>
      </v-col>
      <v-col
        cols="12"
        class="text-left"
      >
        <v-text-field
          v-model.trim="formData.newEmail"
          outlined
          :disabled="formData.emails.length >= 20"
          label="E-mail"
          @keydown.enter="addNewEmail"
        />
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
          link: "http://www.google.com"
        };
      }
    }
  },
  data() {
    return {
      isStartDateMenuShown: false,
      isEndDateMenuShown: false,
      // eslint-disable-next-line no-undef
      todayDate: moment().format("YYYY-MM-DD"),
      formData: {
        startDate: "",
        endDate: "",
        isPublic: false,
        newEmail: "",
        emails: [],
        isSurveySentAutomatically: false
      }
    };
  },
  methods: {
    copyLinkToClipboard() {
      let isCopySuccessful = copyText(this.survey.link);
      if (isCopySuccessful) {
        // do something
        // alert
        console.log("copy successful");
        console.log(this.$notify);
        this.$notify.toast("Link has been copied to clipboard");
      }
    },
    addNewEmail() {
      this.formData.emails.push(this.formData.newEmail);
      this.formData.newEmail = "";
    },
    removeEmail(index) {
      this.formData.emails.splice(index, 1);
    }
  }
};
</script>

<style>
</style>
