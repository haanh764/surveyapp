import Cookies from "js-cookie";
import loginInfo from "~e2e/support/data/login-info";
import {
  CY_USER_LOGIN_URL,
  CY_USER_LOGOUT_URL,
  CY_ADMIN_LOGIN_URL,
  CY_ADMIN_LOGOUT_URL,
  CY_USER_ACTIVATION_STATUS_URL
} from "~e2e/support/api";

const { user, admin } = loginInfo;

Cypress.Commands.add("initPlugins", () => {
  cy.window().then((win) => {
    cy.wrap(Cookies).as("$cookies");
    cy.wrap(win.router).as("$router");
    cy.wrap(win.store).as("$store");
  });
});

Cypress.Commands.add(
  "loginAsUser",
  (email = user.email, password = user.password, self) => {
    cy.request({
      method: "POST",
      url: CY_USER_LOGIN_URL,
      headers: {
        "content-type": "application/json"
      },
      body: {
        email,
        password
      }
    }).then((response) => {
      const authKey = response.body.message.split("Access token is ")[1];
      Cookies.set("access_token_cookie", authKey, { expires: 7 });
      const userData = {
        accountType: 0,
        email
      };
      self.$cookies.set("access_token_cookie", authKey, { expires: 7 });
      self.$store.dispatch("user/setToken", authKey);
      self.$store.dispatch("user/setUserData", userData);
      self.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
    });
  }
);

Cypress.Commands.add(
  "loginAsUserFromBrowser",
  (email = user.email, password = user.password) => {
    cy.visit("/user/login/");
    cy.initPlugins();
    cy.acceptCookiePolicy();
    cy.get(".login-form__email").type(email);
    cy.get(".login-form__password").type(password);
    cy.get(".login-form__submit-button").click();
  }
);

Cypress.Commands.add("loginAsAdmin", (self) => {
  cy.request({
    method: "POST",
    url: CY_ADMIN_LOGIN_URL,
    headers: {
      "content-type": "application/json"
    },
    body: {
      ...loginInfo.admin
    }
  }).then((response) => {
    const authKey = response.body.message.split("Access token is ")[1];
    Cookies.set("access_token_cookie", authKey, { expires: 7 });
    const userData = {
      accountType: 1,
      email: loginInfo.admin.email
    };
    self.$cookies.set("access_token_cookie", authKey, { expires: 7 });
    self.$store.dispatch("user/setToken", authKey);
    self.$store.dispatch("user/setUserData", userData);
    self.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
  });
});

Cypress.Commands.add(
  "loginAsAdminFromBrowser",
  (email = admin.email, password = admin.password) => {
    cy.visit("/admin/login/");
    cy.initPlugins();
    cy.acceptCookiePolicy();
    cy.get(".login-form__email").type(email);
    cy.get(".login-form__password").type(password);
    cy.get(".login-form__submit-button").click();
  }
);

Cypress.Commands.add("checkUserActivationStatus", (self) => {
  cy.request({
    method: "GET",
    url: CY_USER_ACTIVATION_STATUS_URL
  }).then((response) => {
    if (self) {
      const hasBeenActivated =
        response.body.message.includes(" is not activated");
      const path = hasBeenActivated
        ? { name: "user-surveys" }
        : { name: "user-confirm" };

      self.$store.dispatch("user/setHasBeenActivated", hasBeenActivated);
      self.$router.push(path).catch(() => {});
    }
  });
});

Cypress.Commands.add("logoutAsUser", (self) => {
  cy.request({
    method: "POST",
    url: CY_USER_LOGOUT_URL,
    headers: {
      Authentication: `Bearer ${Cookies.get("access_token_cookie")}`
    }
  }).then((response) => {
    if (response.status == 200 && self) {
      self.$store.dispatch("user/setUserData", {});
      self.$store.dispatch("user/setToken", "");
      self.$store.dispatch("user/setItems", []);
      self.$cookies.remove("access_token_cookie");
      self.$router.push("/");
    }
  });
});

Cypress.Commands.add("logoutFromBrowser", () => {
  cy.visit("/logout");
});

Cypress.Commands.add("logoutAsAdmin", (self) => {
  cy.request({
    method: "POST",
    url: CY_ADMIN_LOGOUT_URL,
    headers: {
      Authentication: `Bearer ${Cookies.get("access_token_cookie")}`
    }
  }).then((response) => {
    if (response.status == 200 && self) {
      self.$store.dispatch("user/setUserData", {});
      self.$store.dispatch("user/setToken", "");
      self.$store.dispatch("user/setItems", []);
      self.$cookies.remove("access_token_cookie");
      self.$router.push("/");
    }
  });
});

Cypress.Commands.add("acceptPrivacyPolicy", () => {
  cy.get("body").then(($body) => {
    if ($body.text().includes("Review Privacy Policy")) {
      cy.get(".surveys-view__privacy-button").click();
      cy.wait(1000);
      cy.get(".conditions-interaction").should("be.visible");
      cy.get(".conditions-interaction__accept-button").click({
        multiple: true
      });
    }
  });
});

Cypress.Commands.add("acceptTnC", () => {
  cy.get("body").then(($body) => {
    if ($body.text().includes("Review Terms and Conditions")) {
      cy.get(".surveys-view__tnc-button").click();
      cy.wait(1000);
      cy.get(".conditions-interaction").should("be.visible");
      cy.get(".conditions-interaction__accept-button").click({
        multiple: true
      });
    }
  });
});

Cypress.Commands.add("acceptCookiePolicy", () => {
  cy.wait(5000);
  cy.get("body").then(($body) => {
    if ($body.text().includes("Cookie Policy")) {
      cy.get(".cookies-confirmation__card").find(".v-btn").click();
    }
  });
});

Cypress.Commands.add("initialization", (self, customloginInfo = {}) => {
  cy.visit("/");
  cy.initPlugins();
  cy.acceptCookiePolicy();

  let login = { ...loginInfo.user, ...customloginInfo };
  cy.loginAsUser(login.email, login.password, self);
});
