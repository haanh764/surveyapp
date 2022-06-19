import {
  USER_LOGIN_URL,
  USER_LOGOUT_URL,
  USER_NOT_ACTIVATED_URL,
  ADMIN_LOGIN_URL,
  ADMIN_LOGOUT_URL
} from "@/api/urls";

const BASE_URL = Cypress.env("VUE_APP_API_BASE_URL");
const customizeUrl = (url) => {
  return `${BASE_URL}${url}`;
};

export const CY_USER_LOGIN_URL = customizeUrl(USER_LOGIN_URL);
export const CY_USER_LOGOUT_URL = customizeUrl(USER_LOGOUT_URL);
export const CY_USER_ACTIVATION_STATUS_URL = customizeUrl(
  USER_NOT_ACTIVATED_URL
);

export const CY_ADMIN_LOGIN_URL = customizeUrl(ADMIN_LOGIN_URL);
export const CY_ADMIN_LOGOUT_URL = customizeUrl(ADMIN_LOGOUT_URL);
