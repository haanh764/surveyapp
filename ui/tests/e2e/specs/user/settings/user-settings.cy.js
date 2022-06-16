describe("A user who has logged-in must be able to change their password.", () => {
  it("can change user's password", function () {
    cy.initialization(this);
    cy.wait(5000);
    cy.visit("/user/settings");
    cy.get(".user-settings-form__password").type("asdfghjkl");
    cy.get(".user-settings-form__submit-button").click();
    cy.wait(5000);
    cy.get(".v-snack__content").should("be.visible");
  });
});
