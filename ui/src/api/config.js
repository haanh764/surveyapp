export default {
  baseURL: VUE_APP_API_BASE_URL + "api/",
  timeout: 30000,
  headers: {
    common: {
      Accept: "application/json",
      "Content-Type": "application/json"
    }
  }
};
