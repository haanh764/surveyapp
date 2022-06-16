// should be run with different browsers to assert that the test runs correctly
describe("Website should be accessible", () => {
  it("can access the website in desktop view", () => {
    cy.visit("/");
    cy.contains(".tagline", "Reach your respondents.");
  });

  it("can access the website in mobile view", () => {
    cy.visit("/");
    cy.viewport("iphone-x");
    cy.contains(".tagline", "Reach your respondents.");
  });
});
