<template>
  <v-container
    fluid
    tag="section"
    class="detail-questions fill-height"
  >
    <v-row
      justify="start"
      align="center"
    >
      <v-col
        cols="12"
        class="detail-questions__info"
      >
        <v-row
          justify="start"
          class="pa-5"
        >
          <!--start of mobile template -->
          <template v-if="isMobile">
            <v-col
              cols="12"
              class="text-right pb-5 pt-0"
            >
              <strong class="d-block primary--text">
                <v-icon
                  small
                  class="mr-2 primary--text"
                >mdi-clock</v-icon>
                {{ timeDifferenceBeforePublication }}
              </strong>
            </v-col>
            <v-col
              cols="12"
              class="text-left py-0"
            >
              <p class="ma-0 text-left">
                <v-icon
                  small
                  class="mr-1"
                >mdi-calendar</v-icon>
                {{ survey.config.startDate | standardDate }} - {{ survey.config.endDate | standardDate }}
              </p>
            </v-col>
            <v-col
              cols="12"
              class="text-left"
            >
              <v-icon small>
                mdi-account-outline
              </v-icon>
              <template v-if="survey.config.isPublic">
                Public
                <v-btn
                  text
                  small
                  outlined
                  rounded
                  class="text-secondary text-none ml-2"
                  @click="onClickCopyLinkButton"
                >
                  <v-icon
                    class="pr-2"
                    small
                  >mdi-content-copy</v-icon>
                  Copy link
                </v-btn>
              </template>
              <template v-else>
                Invite-only to {{ survey.config.emails.length }} participants
                <v-btn
                  text
                  small
                  outlined
                  rounded
                  class="text-secondary text-none ml-2"
                  @click="onClickViewParticipantsButton"
                >
                  <v-icon
                    class="pr-2"
                    small
                  >mdi-account-outline</v-icon>
                  View participants
                </v-btn>
              </template>
            </v-col>
            <v-col
              cols="12"
              class="text-left "
            >
              <v-btn
                v-if="survey.data.isPublished"
                text
                small
                outlined
                rounded
                @click="onClickSetSurveyPrivacyButton"
                class="mr-2 text-secondary text-none"
              >
                <v-icon
                  small
                  class="mr-2"
                >mdi-lock</v-icon>
                Set survey privacy
              </v-btn>
              <v-btn
                text
                small
                outlined
                rounded
                class="mr-2 text-secondary text-none"
                v-else
                @click="onClickEditSurveyButton"
              >
                <v-icon
                  small
                  class="pr-2"
                >mdi-pencil</v-icon>
                Edit survey
              </v-btn>
              <v-btn
                text
                small
                class="text-secondary text-none"
                @click="onClickDeleteSurveyButton"
              >
                <v-icon
                  small
                  class="pr-2"
                  rounded
                >mdi-delete</v-icon>
                <u>Delete survey</u>
              </v-btn>
            </v-col>
          </template>
          <!--end of mobile template -->
          <!-- start of desktop info card-->
          <template v-else>
            <v-col cols="4">
              <p class="ma-0 text-left">
                <v-icon
                  small
                  class="mr-1"
                >mdi-calendar</v-icon>
                {{ survey.config.startDate | standardDate }} - {{ survey.config.endDate | standardDate }}
              </p>
            </v-col>
            <v-col
              cols="4"
              class="text-left"
            >
              <v-icon small>
                mdi-account-outline
              </v-icon>
              <template v-if="survey.config.isPublic">
                Public
                <v-btn
                  text
                  small
                  outlined
                  rounded
                  class="text-secondary text-none ml-2"
                  @click="onClickCopyLinkButton"
                >
                  <v-icon
                    class="pr-2"
                    small
                  >mdi-content-copy</v-icon>
                  Copy link
                </v-btn>
              </template>
              <template v-else>
                Invite-only to {{ survey.config.emails.length }} participants

                <v-btn
                  text
                  small
                  outlined
                  rounded
                  class="text-secondary text-none ml-2"
                  @click="onClickViewParticipantsButton"
                >
                  <v-icon
                    class="pr-2"
                    small
                  >mdi-account-outline</v-icon>
                  View participants
                </v-btn>
              </template>
            </v-col>
            <v-col
              cols="4"
              class="text-right"
            >
              <strong class="d-block primary--text mb-10">
                <v-icon
                  small
                  class="mr-2 primary--text"
                >mdi-clock</v-icon>
                {{ timeDifferenceBeforePublication }}
              </strong>
              <v-btn
                v-if="survey.data.isPublished"
                text
                small
                outlined
                rounded
                class="text-secondary text-none mr-2"
                @click="onClickSetSurveyPrivacyButton"
              >
                <v-icon small>mdi-share</v-icon>
                Set survey privacy
              </v-btn>
              <v-btn
                text
                small
                outlined
                rounded
                class="mr-2 text-secondary text-none"
                v-else
                @click="onClickEditSurveyButton"
              >
                <v-icon
                  small
                  class="pr-2"
                >mdi-pencil</v-icon>
                Edit survey
              </v-btn>
              <v-btn
                text
                small
                class="text-secondary text-none pa-0"
                @click="onClickDeleteSurveyButton"
              >
                <v-icon
                  small
                  class="pr-2"
                  rounded
                >mdi-delete</v-icon>
                <u>Delete survey</u>
              </v-btn>
            </v-col>
          </template>
          <!--end of desktop info card -->
        </v-row>
      </v-col>
      <v-col cols="12">
        <generate-form
          ref="generateForm"
          :disabled="true"
          :form-data="survey.data"
          :value="survey.data.formBuilder.models"
          :is-submit-button-shown="false"
        />
      </v-col>
    </v-row>

    <modal
      v-model="isViewParticipantsModalShown"
      name="view-participants-modal"
      :title="`Survey Participants (${survey.config.emails.length})`"
    >
      <v-card
        elevation="0"
        class="pa-5"
      >
        <v-list>
          <v-list-item-group multiple>
            <template v-for="(item, i) in survey.config.emails">
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
              </v-list-item>
              <v-divider
                v-if="i <= survey.config.emails.length - 2"
                :key="`divider-${i}`"
              />
            </template>
          </v-list-item-group>
        </v-list>

      </v-card>
    </modal>

    <modal
      v-model="isSurveySettingsModalShown"
      title="Survey settings"
      primary-action-button-text="save"
      @click:primary-action="onSubmitSurveySettings"
    >
      <div class="pa-5">
        <survey-settings
          :can-set-date="false"
          v-model="formData.config"
        />
      </div>
    </modal>

    <bottom-sheet
      v-model="isSurveySettingsBottomSheetShown"
      title="Set survey privacy"
      :fullscreen="true"
      align-title="center"
      @close="onSubmitSurveySettings"
    >
      <template #content>
        <div class="pa-5">
          <survey-settings
            :can-set-date="false"
            v-model="formData.config"
          />
        </div>
      </template>
    </bottom-sheet>

    <modal
      v-model="isDeleteModalShown"
      name="delete-modal"
      title="Warning"
      content="Are you sure you want to delete this survey? This action cannot be undone."
      primary-action-button-text="OK"
      @click:primary-action="onDeleteConfirmation"
    />
  </v-container>
</template>


<script>
import surveyDataSample from "@/assets/json/survey-data-sample.json";
import GenerateForm from "@/form-builder/components/GenerateForm";
import SurveySettings from "@/views/user/survey-edit/components/SurveySettings";
import {
  isTodayBeforeGivenDate,
  convertToStandardDate,
  getDurationFromTodayToGivenDate,
} from "@/util/dates";
import copyText from "@util/copy";

export default {
  name: "DetailQuestions",
  components: {
    GenerateForm,
    SurveySettings,
  },
  data() {
    return {
      isDeleteModalShown: false,
      isSurveySettingsModalShown: false,
      isViewParticipantsModalShown: false,
      isSurveySettingsBottomSheetShown: false,
      formData: {
        config: {},
      },
      survey: {
        data: {
          link: "",
          isPublished: false,
        },
        config: {},
      },
    };
  },
  created() {
    this.survey = { ...this.survey, ...surveyDataSample };
  },
  computed: {
    isStartDateBeforeToday() {
      return isTodayBeforeGivenDate(this.survey.config.startDate);
    },
    timeDifferenceBeforePublication() {
      const { hours, days } = getDurationFromTodayToGivenDate(
        this.survey.config.startDate
      );
      const time =
        hours < 24 ? `${hours.toFixed(0)} hours` : `${days.toFixed(0)} days`;
      return this.isStartDateBeforeToday
        ? `To be published in ${time}`
        : `Published on ${convertToStandardDate(this.survey.config.startDate)}`;
    },
    surveyId() {
      return this.$route.params.id;
    },
  },
  methods: {
    onSubmitSurveySettings() {
      // get data from survey settings
      // submit
      // show notif
      // reload
      this.isSurveySettingsModalShown = false;
      this.$notify.toast("Survey has been successfully saved");
    },
    onClickSetSurveyPrivacyButton() {
      if (this.isMobile) {
        this.isSurveySettingsBottomSheetShown = true;
      } else {
        this.isSurveySettingsModalShown = true;
      }
    },
    onClickViewParticipantsButton() {
      this.isViewParticipantsModalShown = true;
    },
    onDeleteConfirmation() {
      // fetch delete api
      // if ok, show notif, redirect to user/surveys page
      // else stays
      this.$notify.toast("Survey has been successfully deleted");
      this.$router.push("/user/surveys");
    },
    onClickCopyLinkButton() {
      const isSuccess = copyText(this.survey.data.link);

      isSuccess &&
        this.$notify.toast("Link has been succesfully copied to clipboard");
    },
    onClickDeleteSurveyButton() {
      this.isDeleteModalShown = true;
    },
    onClickEditSurveyButton() {
      this.$router.push(`/user/surveys/${this.surveyId}/edit`);
    },
  },
};
</script>
<style lang="scss">
.detail-questions {
  &__info {
    background-color: $grayish-white;
  }
}
</style>
