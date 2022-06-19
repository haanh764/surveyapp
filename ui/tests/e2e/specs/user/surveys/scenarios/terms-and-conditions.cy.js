describe("The system must show the TnC and Privacy Policy", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
  });

  it("should show the buttons to review privacy policy and terms and conditions on first visit", () => {
    cy.get(".surveys-view__privacy-button").should("be.visible");
    cy.get(".surveys-view__tnc-button").should("be.visible");
  });

  it("should show the Privacy Policy when clicking on the button and hide the button when user has accepted", () => {
    cy.get(".surveys-view__privacy-button").click();
    cy.wait(1000);
    cy.get(".conditions-interaction").should("be.visible");
    cy.get(".conditions-interaction__accept-button").click();
    cy.get(".surveys-view__privacy-button").should("not.be.visible");
  });

  it("should show the TnC when clicking on the button and hide the button when user has accepted", () => {
    cy.get(".surveys-view__tnc-button").click();
    cy.wait(1000);
    cy.get(".conditions-interaction").should("be.visible");
    cy.get(".conditions-interaction__accept-button").click();
    cy.get(".surveys-view__tnc-button").should("not.be.visible");
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});
