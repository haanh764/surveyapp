/* global VUE_APP_API_BASE_URL */

export default {
  baseURL: VUE_APP_API_BASE_URL + "api/",
  timeout: 30000,
  common: {
    Accept: "application/json",
    "Content-Type": "application/json"
  }
};
