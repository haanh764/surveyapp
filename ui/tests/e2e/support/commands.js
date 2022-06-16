import Cookies from "js-cookie";

// ***********************************************
// This example commands.js shows you how to
// create various custom commands and overwrite
// existing commands.
//
// For more comprehensive examples of custom
// commands please read more here:
// https://on.cypress.io/custom-commands
// ***********************************************
//
//

Cypress.Commands.add("initPlugins", () => {
  cy.window().then((win) => {
    cy.wrap(Cookies).as("$cookies");
    cy.wrap(win.router).as("$router");
    cy.wrap(win.store).as("$store");
  });
});

Cypress.Commands.add("loginAsUser", (email, password, self) => {
  cy.request({
    method: "POST",
    url: "http://localhost:8000/api/authentication/login",
    headers: {
      "content-type": "application/json",
    },
    body: {
      email,
      password,
    },
  }).then((response) => {
    const authKey = response.body.message.split("Access token is ")[1];
    Cookies.set("access_token_cookie", authKey, { expires: 7 });
    const userData = {
      accountType: 0,
      email,
    };
    self.$cookies.set("access_token_cookie", authKey, { expires: 7 });
    self.$store.dispatch("user/setToken", authKey);
    self.$store.dispatch("user/setUserData", userData);
    self.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
  });
});

Cypress.Commands.add("loginAsAdmin", (self) => {
  cy.request({
    method: "POST",
    url: "http://localhost:8000/api/authentication/login",
    headers: {
      "content-type": "application/json",
    },
    body: {
      email: "surveyapp.manager@gmail.com",
      password: "admin123",
    },
  }).then((response) => {
    const authKey = response.body.message.split("Access token is ")[1];
    Cookies.set("access_token_cookie", authKey, { expires: 7 });
    const userData = {
      accountType: 1,
      email: "surveyapp.manager@gmail.com",
    };
    self.$cookies.set("access_token_cookie", authKey, { expires: 7 });
    self.$store.dispatch("user/setToken", authKey);
    self.$store.dispatch("user/setUserData", userData);
    self.$store.dispatch("user/checkAccountTypeAndSetMenuItems");
  });
});

Cypress.Commands.add("initialization", (self, loginData = {}) => {
  cy.visit("/");
  cy.initPlugins();
  cy.acceptCookiePolicy();

  // change the value as you wish, but make sure don't push the change
  let login = {
    email: "sapi@yopmail.com",
    password: "asdfghjkl",
  };
  login = { ...login, ...loginData };
  cy.loginAsUser(...login, self);
});

// api is still buggy, couldnt test
Cypress.Commands.add("checkUserActivationStatus", (self) => {
  cy.request({
    method: "GET",
    url: "http://localhost:8000/api/authentication/notactivated",
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

// logout api is still buggy, couldnt test
Cypress.Commands.add("logoutAsUser", (self) => {
  cy.request({
    method: "POST",
    url: "http://localhost:8000/api/authentication/logout",
    headers: {
      Authentication: `Bearer ${Cookies.get("access_token_cookie")}`,
    },
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

Cypress.Commands.add("logoutAsAdmin", (self) => {
  cy.request({
    method: "POST",
    url: "http://localhost:8000/api/admin/logout",
    headers: {
      Authentication: `Bearer ${Cookies.get("access_token_cookie")}`,
    },
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

Cypress.Commands.add("acceptCookiePolicy", () => {
  cy.get(".cookies-confirmation__card").find(".v-btn").click();
});

//
//
// -- This is a child command --
// Cypress.Commands.add("drag", { prevSubject: 'element'}, (subject, options) => { ... })
//
//
// -- This is a dual command --
// Cypress.Commands.add("dismiss", { prevSubject: 'optional'}, (subject, options) => { ... })
//
//
// -- This is will overwrite an existing command --
// Cypress.Commands.overwrite("visit", (originalFn, url, options) => { ... })
