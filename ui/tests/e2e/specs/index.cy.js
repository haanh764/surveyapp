// should be run with different browsers to assert that the test runs correctly
describe("Website should be accessible", () => {
  it("Visits the app root url", () => {
    cy.visit("/");
    cy.contains(".tagline", "Reach your respondents.");
  });
});
