describe("A user who has logged-in must be able to change their password.", () => {
  it("can change user's password", function () {
    cy.initialization(this);
    cy.wait(1000);
    cy.visit("/user/settings");
    cy.get(".user-settings-form__password").type("asdfghjkl");
    cy.get(".user-settings-form__submit-button").click();
    cy.wait(1000);
    cy.get(".v-snack__content").should("be.visible");
  });
});

describe("A user who has logged-in must be able to delete their account.", () => {
  it("can delete account", function () {
    cy.initialization(this);
    cy.wait(1000);
    cy.visit("/user/settings");

    cy.get(".user-settings-form__password").type("asdfghjkl");
    cy.get(".user-settings-form__delete-button").click();

    cy.wait(1000);
    cy.get(".delete-modal").should("be.visible");
    cy.get(".delete-modal").find(".primary-action-button").click();
    cy.wait(1000);
    cy.url().contains("user/delete/thankyou");
  });
});
