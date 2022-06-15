import config from "./config.js";
import { EventBus } from "@util/event-bus";

const axios = require("axios");

const { timeout, baseURL } = config;
axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;
axios.defaults.headers.common["Accept"] = "application/json";
axios.defaults.headers.common["Content-Type"] = "application/json";

// handle default
axios.interceptors.request.use(
  (config) => {
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
const USER_LOGIN_URL = "authentication/login";
const USER_SIGNUP_URL = "authentication/signup";

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
  return axios.post(USER_LOGIN_URL, data, config);
};
