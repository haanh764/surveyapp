import config from "./config.js";

const axios = require("axios");

const { timeout, baseURL } = config;
axios.defaults.baseURL = baseURL;
axios.defaults.timeout = timeout;

const GET_SURVEYS_URL = "/user/surveys";
const ADD_SURVEY_URL = "/user/surveys";


export const getSurveys = () => {
  return axios.get(GET_SURVEYS_URL);
};

export const addSurvey = (data) => {
  return axios.post(ADD_SURVEY_URL, data);
};
