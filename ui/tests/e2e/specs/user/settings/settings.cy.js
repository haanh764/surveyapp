describe("A user who has logged-in must be able to change their password.", () => {
  it("can change user's password", function () {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/settings");
    cy.get(".user-settings-form__password").type("asdfghjkl");
    cy.get(".user-settings-form__submit-button").click();
    cy.wait(1000);
    cy.get(".v-snack__content").should("be.visible");
    cy.logoutFromBrowser();
  });
});

describe("A user who has logged-in must be able to delete their account.", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/settings");
  });

  it("can delete account", function () {
    cy.get(".user-settings-form__delete-button").click();
    cy.wait(1000);
    cy.get(".modal__card").find(".primary-action-button").click();
    cy.wait(1000);
    cy.url().should("contain", "user/delete/thankyou");
  });

  it("will show a warning to which the user can confirm their action", function () {
    cy.get(".user-settings-form__delete-button").click();
    cy.wait(1000);
    cy.get(".modal__card").should("be.visible");
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});
