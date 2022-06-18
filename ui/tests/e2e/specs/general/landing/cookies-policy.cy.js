describe("Cookie policy", () => {
  it("should show the cookie policy dialog on first visit", () => {
    cy.clearCookies();
    cy.clearLocalStorage();
    cy.visit("/");
    cy.get(".cookies-confirmation__card").should("be.visible");
  });

  it("should hide the cookie policy dialog after clicking on the accept button", () => {
    cy.visit("/");
    cy.get(".cookies-confirmation__card").find(".v-btn").click();
    cy.get(".cookies-confirmation__card").should("not.be.visible");
  });
});
