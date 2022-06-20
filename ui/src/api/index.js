import config from "./config.js";
import { EventBus } from "@util/event-bus";
import Cookies from "js-cookie";
import store from "@store/";

import {
  USER_SIGNUP_URL,
  USER_LOGIN_URL,
  USER_LOGOUT_URL,
  USER_NOT_ACTIVATED_URL,
  USER_IS_BLOCKED_URL,
  USER_RESEND_ACTIVATION_URL,
  USER_CHANGE_PASSWORD_URL,
  USER_DELETE_ACCOUNT_URL,
  USER_LIST_SURVEYS_URL,
  USER_DELETE_SURVEY_URL,
  USER_ADD_SURVEY_URL,
  USER_GET_SURVEY_URL,
  USER_SURVEY_DATATABLE_URL,
  USER_SURVEY_SUMMARY_URL,
  RESPONDER_SUBMIT_RESPONSE_URL,
  ADMIN_LOGIN_URL,
  ADMIN_LOGOUT_URL,
  ADMIN_ACTIVATE_USER_URL,
  ADMIN_BLOCK_USER_URL,
  ADMIN_CHANGE_PASSWORD_URL,
  ADMIN_LIST_SURVEYS_URL,
  ADMIN_DELETE_SURVEY_URL,
  ADMIN_LIST_USERS_URL,
  ADMIN_RESET_USER_PASSWORD_URL,
  ADMIN_SEARCH_USER_URL,
  ADMIN_UNBLOCK_USER_URL,
  ADMIN_DELETE_USER_URL
} from "./urls";

const axios = require("axios");
const { timeout, baseURL, headers } = config;

axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;
axios.defaults.headers = { ...axios.defaults.headers, ...headers };

// handle default
axios.interceptors.request.use(
  (config) => {
    const userToken =
      Cookies.get("access_token_cookie") || store.getters["user/token"];
    if (userToken) {
      config.headers.Authorization = `Bearer ${userToken}`;
    }
    return config;
  },
  (error) => {
    console.error("API Request Error:", JSON.stringify(error));
    EventBus.$emit("event:apiError", error);
    return Promise.reject(new Error(error).message);
  }
);

axios.interceptors.response.use(
  (response) => {
    console.log(".....", response);
    return response.data;
  },
  (error) => {
    console.error("API Response Error:", JSON.stringify(error));
    EventBus.$emit("event:apiError", error);
    return Promise.reject(new Error(error).message);
  }
);

export const responderSubmitResponse = (surveyId, data) => {
  return axios.post(RESPONDER_SUBMIT_RESPONSE_URL + surveyId, data);
};

export const userListSurveys = () => {
  return axios.get(USER_LIST_SURVEYS_URL);
};

export const userDeleteSurvey = (data) => {
  return axios.post(USER_DELETE_SURVEY_URL, data);
};

export const userAddSurvey = (data) => {
  return axios.post(USER_ADD_SURVEY_URL, data);
};

export const userEditSurvey = (data) => {
  return axios.post(USER_ADD_SURVEY_URL, data);
};

export const userGetSurvey = (survey_id) => {
  return axios.get(USER_GET_SURVEY_URL + survey_id);
};

export const userGetSurveyDatatable = (survey_id) => {
  return axios.get(USER_SURVEY_DATATABLE_URL + survey_id);
};

export const userGetSurveySummary = (survey_id) => {
  return axios.get(USER_SURVEY_SUMMARY_URL + survey_id);
};

export const userSignup = (data) => {
  return axios.post(USER_SIGNUP_URL, data);
};

export const userLogin = (data) => {
  return axios.post(USER_LOGIN_URL, data);
};

export const userLogout = () => {
  return axios.post(USER_LOGOUT_URL);
};

export const userNotActivated = () => {
  return axios.get(USER_NOT_ACTIVATED_URL);
};

export const userisBlocked = () => {
  return axios.get(USER_IS_BLOCKED_URL);
};

export const userResendActivation = () => {
  return axios.post(USER_RESEND_ACTIVATION_URL);
};

export const userChangePassword = (data) => {
  return axios.post(USER_CHANGE_PASSWORD_URL, data);
};

export const userDeleteAccount = () => {
  return axios.delete(USER_DELETE_ACCOUNT_URL);
};

export const adminLogin = (data) => {
  return axios.post(ADMIN_LOGIN_URL, data);
};

export const adminLogout = () => {
  return axios.post(ADMIN_LOGOUT_URL);
};

export const adminChangePassword = (data) => {
  return axios.post(ADMIN_CHANGE_PASSWORD_URL, data);
};

export const adminListSurveys = () => {
  return axios.get(ADMIN_LIST_SURVEYS_URL);
};

export const adminDeleteSurvey = (data) => {
  return axios.post(ADMIN_DELETE_SURVEY_URL, data);
};

export const adminListUsers = () => {
  return axios.get(ADMIN_LIST_USERS_URL);
};

export const adminSearchUser = (data) => {
  return axios.post(ADMIN_SEARCH_USER_URL, data);
};

export const adminResetUserPassword = (data) => {
  return axios.post(ADMIN_RESET_USER_PASSWORD_URL, data);
};

export const adminActivateUser = (data) => {
  return axios.post(ADMIN_ACTIVATE_USER_URL, data);
};

export const adminBlockUser = (data) => {
  return axios.post(ADMIN_BLOCK_USER_URL, data);
};

export const adminUnblockUser = (data) => {
  return axios.post(ADMIN_UNBLOCK_USER_URL, data);
};

export const adminDeleteUser = (data) => {
  return axios.post(ADMIN_DELETE_USER_URL, data);
};
