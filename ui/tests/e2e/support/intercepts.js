import {
  CY_USER_LOGIN_URL,
  CY_USER_LOGOUT_URL,
  CY_ADMIN_LOGIN_URL,
  CY_ADMIN_LOGOUT_URL,
  CY_USER_ACTIVATION_STATUS_URL
} from "~e2e/support/api";

export const interceptApis = function () {
  if (Cypress.env("IS_API_MOCKED") == "true") {
    cy.intercept(CY_USER_LOGIN_URL, {
      message: "Access token is 1234567890"
    });

    cy.intercept(CY_USER_LOGOUT_URL, {
      message: "Success"
    });

    cy.intercept(CY_USER_ACTIVATION_STATUS_URL, {
      message: "User is activated"
    });

    cy.intercept(CY_ADMIN_LOGIN_URL, {
      message: "Access token is 1234567890"
    });

    cy.intercept(CY_ADMIN_LOGOUT_URL, {
      message: "Success"
    });
  }
};
