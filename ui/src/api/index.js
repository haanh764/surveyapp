import config from "./config.js";

const axios = require("axios");

const { timeout, baseURL } = config;
axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;

// handle default
axios.interceptors.request.use(
  (config) => {
    return config;
  },
  (error) => {
    console.log("API Request Error:", error);
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
    return Promise.reject(new Error(error).message);
  }
);

const GET_SURVEYS_URL = "/user/surveys";
const ADD_SURVEY_URL = "/user/surveys";

export const getSurveys = () => {
  return axios.get(GET_SURVEYS_URL);
};

export const addSurvey = (data) => {
  return axios.post(ADD_SURVEY_URL, data);
};

const USER_SIGNUP_URL = "/authentication/signup";

export const userSignup = (data) => {
  let config = {
    headers: {
      "Accept": "application/json",
      "Content-Type": "application/json"
    }
  }

  return axios.post(USER_SIGNUP_URL, data, config);
}
