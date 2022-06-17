import config from "./config.js";
import { EventBus } from "@util/event-bus";
import Cookies from "js-cookie";
import store from "@store/";

const axios = require("axios");
const { timeout, baseURL } = config;

axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;
axios.defaults.headers.common["Accept"] = "application/json";
axios.defaults.headers.common["Content-Type"] = "application/json";

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
    console.log("API Request Error:", JSON.stringify(error));
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
    console.log("API Response Error:", JSON.stringify(error));
    EventBus.$emit("event:apiError", error);
    return Promise.reject(new Error(error).message);
  }
);

const USER_SIGNUP_URL = "authentication/signup";
const USER_LOGIN_URL = "authentication/login";
const USER_LOGOUT_URL = "authentication/logout";
const USER_NOT_ACTIVATED_URL = "authentication/notactivated";
const USER_RESEND_ACTIVATION_URL = "authentication/resend";
const USER_CHANGE_PASSWORD_URL = "user/changepassword";
const USER_DELETE_ACCOUNT_URL = "user/delete";

const ADMIN_LOGIN_URL = "admin/login";
const ADMIN_LOGOUT_URL = "admin/logout";
const ADMIN_CHANGE_PASSWORD_URL = "admin/changepassword";
//const ADMIN_LIST_SURVEYS_URL = "";
const ADMIN_DELETE_SURVEY_URL = "admin/deletesurvey";
const ADMIN_LIST_USERS_URL = "admin/listusers";
const ADMIN_SEARCH_USER_URL = "admin/searchuser";
const ADMIN_RESET_USER_PASSWORD_URL = "admin/resetuserpassword";
const ADMIN_ACTIVATE_USER_URL = "admin/activateuser";
const ADMIN_BLOCK_USER_URL = "admin/blockuser";
const ADMIN_UNBLOCK_USER_URL = "admin/unblockeduser";
const ADMIN_DELETE_USER_URL = "admin/deleteuser";

const USER_LIST_SURVEYS_URL = "user/surveys";
const USER_DELETE_SURVEY_URL = "user/survey/delete";
const USER_ADD_SURVEY_URL = "survey/add";
const USER_EDIT_SURVEY_URL = "";
const USER_GET_SURVEY_URL = "survey/";
//const USER_SURVEY_DATATABLE_URL = "analysis/generatedatatable/<string:survey_id>";
//const USER_SURVEY_SUMMARY_URL = "analysis/getsummary/<string:survey_id>";



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
  return axios.post(USER_EDIT_SURVEY_URL, data);
};

export const userGetSurvey = (survey_id) => {
  return axios.get(USER_GET_SURVEY_URL + survey_id);
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
