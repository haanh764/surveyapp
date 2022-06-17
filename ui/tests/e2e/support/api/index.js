const BASE_URL = Cypress.env("VUE_APP_API_BASE_URL");

const customizeUrl = (url) => {
  return `${BASE_URL}${url}`;
};

export const USER_LOGIN_URL = customizeUrl("authentication/login");
export const USER_LOGOUT_URL = customizeUrl("authentication/logout");
export const USER_ACTIVATION_STATUS_URL = customizeUrl(
  "authentication/notactivated"
);

export const ADMIN_LOGIN_URL = customizeUrl("admin/login");
export const ADMIN_LOGOUT_URL = customizeUrl("admin/logout");
