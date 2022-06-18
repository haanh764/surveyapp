<template>
  <v-container
    class="fill-height text-center survey-fill-view"
    tag="section"
  >
    <v-row justify="center">
      <v-col
        v-if="survey.data.isPublished"
        cols="12"
      >
        <content-card
          title="Sorry, this survey is not yet published"
          description="Check your invite link or make sure you are granted the right
 to fill in the survey"
          :image="require('@assets/svg/man-woman-holding-mail.svg')"
        />
      </v-col>
      <v-col
        v-else
        :cols="isMobile ? 12: 10"
      >
        <template v-if="hasSubmitted">
          <content-card
            title="Thank you!"
            description="Your submission has been received"
            primary-button-text="Download as PDF"
            :on-primary-button-click-callback="onPrimaryButtonClickCallback"
            :image="require('@assets/svg/man-woman-holding-mail.svg')"
          >
            <template #actions>
              <div class="mt-5 text-center">
                <p class="text-secondary">
                  or share to
                </p>
                <div class="survey-fill-view__social-media">
                  <ul class="social-media-list">
                    <li
                      v-for="(socialMedia, index) in socialMedias"
                      :key="'socialMedia_'+index"
                      class="social-media-list__item"
                    >
                      <v-icon
                        class="icon"
                        @click="onClickSocialMediaIcon(socialMedia)"
                      >
                        {{ socialMedia.icon }}
                      </v-icon>
                      <span class="text">{{ socialMedia.text }}</span>
                    </li>
                  </ul>
                </div>
                <div
                  class="survey-fill-view__link"
                  @click="onClickSurveyLink"
                >
                  <a :href="surveyLink">
                    {{ surveyLink }}
                  </a>
                  <v-icon>mdi-content-copy </v-icon>
                </div>
              </div>
            </template>
          </content-card>
        </template>
        <template v-else>
          <template v-if="canSubmit">
            <v-card
              :elevation="isMobile ? 0 : 2"
              class="pa-5"
            >
              <generate-form
                ref="generateForm"
                :form-data="survey.data"
                :value="survey.data.formBuilder.models"
                :can-submit="canSubmit"
                @submit="onClickSubmitButton"
              />
            </v-card>
          </template>
          <template v-else>
            <template v-if="isWithinDate && !survey.config.isPublic">
              <content-card
                title="Sorry, this survey is invite-only"
                description="Check your invite link or make sure you are granted the right
 to fill in the survey"
                :image="require('@assets/svg/man-woman-holding-mail.svg')"
              />
            </template>
            <template v-else>
              <content-card
                title="Sorry, this survey is already closed"
                description="Check your link or contact the  survey owner for more info"
                :image="require('@assets/svg/man-woman-holding-mail.svg')"
              />
            </template>
          </template>
        </template>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import surveyDataSample from "@/assets/json/survey-data-sample.json";
import GenerateForm from "@/form-builder/components/GenerateForm.vue";
import { isTodayBeforeGivenDate } from "@util/dates";
import copyText from "@util/copy";
import { userGetSurvey, responderSubmitResponse } from "@api";

export default {
  name: "SurveyFillView",
  components: { GenerateForm },
  data() {
    return {
      token: this.$route.query.token,
      todayDate: moment().format("DD MMM YYYY"),
      hasPermission: false,
      hasSubmitted: false,
      baseUrl: window.location.origin,
      socialMedias: [
        {
          icon: "mdi-facebook",
          text: "Facebook"
        },
        {
          icon: "mdi-twitter",
          text: "Twitter"
        },
        {
          icon: "mdi-reddit",
          text: "Reddit"
        },
        {
          icon: "mdi-whatsapp",
          text: "WhatsApp"
        }
      ],
      survey: {
        data: {
          title: "",
          description: "",
          link: "",
          isPublished: false,
          formBuilder: {
            list: [],
            models: {}
          }
        },
        config: {
          startDate: "",
          endDate: "",
          isPublic: false,
          emails: []
        }
      }
    };
  },
  computed: {
    surveyId() {
      return this.$route.params.id;
    },
    surveyLink() {
      return `${this.baseUrl}/survey/${this.surveyId}`;
    },
    isWithinDate() {
      return isTodayBeforeGivenDate(this.survey.config.endDate);
    },
    canSubmit() {
      return this.survey.config.isPublic
        ? this.isWithinDate
        : this.token && this.hasPermission && this.isWithinDate;
    }
  },
  created() {
    // this.survey = { ...this.survey, ...surveyDataSample }; // delete this line later
    // get survey data
    this.getSurveyApi();
    // check if the user has permission if the survey is private
  },
  methods: {
    getSurveyApi() {
      userGetSurvey()
      .then((response) => {
        console.log(response);
        // map json to this.survey
        this.survey = { ...this.survey, ...response };
        /*
        // DESIRED STRUCTURE:
        survey: {
          data: {
            title: "",
            description: "",
            link: "",
            isPublished: false,
            formBuilder: {
              list: [],
              models: {}
            }
          },
          config: {
            startDate: "",
            endDate: "",
            isPublic: false,
            emails: []
          }
        }
        */
      });
    },
    onClickSocialMediaIcon(socialMedia) {
      console.log(socialMedia);
      // do something
    },
    onClickSubmitButton({ models, list }) {
      console.log(models, list);
      responderSubmitResponse({ models, list }).then(() => {
        this.$notify.toast("Response has been submitted!");
      });
      this.hasSubmitted = true;
    },
    onPrimaryButtonClickCallback() {
      // download as pdf
    },
    onClickSurveyLink() {
      const isCopySuccess = copyText(this.surveyLink);
      isCopySuccess && this.$notify.toast("Link has been copied to clipboard");
    }
  }
};
</script>

<style lang="scss">
.survey-fill-view {
  padding: 40px 0 80px;

  &__social-media {
    .social-media-list {
      display: flex;
      flex-direction: row;
      list-style: none;
      justify-content: space-between;

      &__item {
        .icon {
          border-radius: 50%;
          background-color: $light-gray;
          padding: 10px;
        }

        .text {
          margin-top: 5px;
          display: block;
          text-align: center;
        }
      }
    }
  }

  &__link {
    display: flex;
    width: 100%;
    justify-content: space-between;
    align-items: center;
    border: 1px solid $dark-gray;
    color: $dark-gray;
    padding: 0 10px;
    border-radius: 2px;
    min-height: 53px;
    margin-top: 30px;

    a {
      color: inherit;
    }

    &:hover {
      background-color: $light-gray;
      cursor: pointer;
    }
  }
}
</style>
