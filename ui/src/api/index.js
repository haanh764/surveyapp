import config from "./config.js";
import { EventBus } from "@util/event-bus";
import Cookies from "js-cookie";

const axios = require("axios");
const { timeout, baseURL } = config;

axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;
axios.defaults.headers.common["Accept"] = "application/json";
axios.defaults.headers.common["Content-Type"] = "application/json";

// handle default
axios.interceptors.request.use(
  (config) => {
    const userToken = Cookies.get("access_token_cookie");
    console.log("userToken in interceptors:");
    console.log(userToken);
    if (userToken) {
      config.headers.Authorization = `Bearer ${userToken}`;
    }
    return config;
  },
  (error) => {
    console.log("API Request Error:", error);
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
    console.log("API Response Error:", error);
    EventBus.$emit("event:apiError", error);
    return Promise.reject(new Error(error).message);
  }
);

const GET_SURVEYS_URL = "user/surveys";
const ADD_SURVEY_URL = "user/surveys";
const USER_SIGNUP_URL = "authentication/signup";
const USER_LOGIN_URL = "authentication/login";
const USER_LOGOUT_URL = "authentication/logout";
const USER_NOT_ACTIVATED_URL = "authentication/notactivated";
const USER_RESEND_ACTIVATION_URL = "authentication/resend";
const USER_CHANGE_PASSWORD_URL = "user/changepassword";
const USER_DELETE_ACCOUNT_URL = "user/delete";

export const getSurveys = () => {
  return axios.get(GET_SURVEYS_URL);
};

export const addSurvey = (data) => {
  return axios.post(ADD_SURVEY_URL, data);
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
}

export const userResendActivation = () => {
  return axios.post(USER_RESEND_ACTIVATION_URL);
}

export const userChangePassword = (data) => {
  return axios.post(USER_CHANGE_PASSWORD_URL, data);
}

export const userDeleteAccount = () => {
  return axios.delete(USER_DELETE_ACCOUNT_URL);
}
