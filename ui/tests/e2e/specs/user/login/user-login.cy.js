import loginInfo from "~/tests/e2e/support/data/login-info";
const { user, mockEmails } = loginInfo;

describe("A user should be able to login to their account with 4 clicks or fewer", () => {
  it("can log the user in with 4 clicks or fewer in desktop view and mobile view", () => {
    let clickCounter = 0;
    cy.visit("/");
    cy.acceptCookiePolicy();
    clickCounter += 1;

    cy.get(".login-link").click();
    clickCounter += 1;

    cy.get(".login-form__email").type(user.email);
    cy.get(".login-form__password").type(user.password);
    cy.get(".login-form__submit-button").click();
    clickCounter += 1;
    cy.wrap(clickCounter).as("clickCounter");

    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(5);
    });
  });
});

describe("The system must allow a user to login by entering an email and a password.", () => {
  it("cannot log the user in when user entered wrong email and/or password", () => {
    cy.visit("/user/login/");
    cy.acceptCookiePolicy();
    cy.get(".login-form__email").type(mockEmails.error400);
    cy.get(".login-form__password").type("1234567890");
    cy.get(".login-form__submit-button").click();
    cy.wait(1000);
    cy.url().should("not.contain", "/user/surveys");
  });

  it("can log the user in when user entered correct email and password", function () {
    cy.visit("/user/login/");
    cy.initPlugins();
    cy.acceptCookiePolicy();
    cy.get(".login-form__email").type(user.email);
    cy.get(".login-form__password").type(user.password);
    cy.get(".login-form__submit-button").click();
    cy.wait(5000);
    cy.url().should("contain", "/user/surveys");
    cy.logoutAsUser(this);
  });

  it("can log the user in and show not activated page when user entered correct email and password but has not activated their account", function () {
    cy.visit("/user/login/");
    cy.initPlugins();
    cy.acceptCookiePolicy();
    cy.get(".login-form__email").type(mockEmails.success201);
    cy.get(".login-form__password").type(user.password);
    cy.get(".login-form__submit-button").click();
    cy.wait(5000);
    cy.url().should("contain", "/user/confirm");
    cy.logoutAsUser(this);
  });
});
