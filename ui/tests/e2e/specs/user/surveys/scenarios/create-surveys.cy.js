describe("The system must allow a user who has logged-in to create a new survey.", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
    cy.acceptPrivacyPolicy();
    cy.acceptTnC();
  });

  it("should show the create survey button in mobile view", () => {
    cy.viewport("iphone-x");
    cy.get(".surveys-view__create-button").should("be.visible");
  });

  it("should show the create survey button in desktop view", () => {
    cy.get(".surveys-view__create-button").should("be.visible");
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});

describe("A survey owner should be able to create a survey with 3 clicks or fewer after a successful login", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
    cy.acceptPrivacyPolicy();
    cy.acceptTnC();
  });

  it("should allow creating a survey in 3 clicks or fewer in mobile view", () => {
    let clickCounter = 0;
    cy.viewport("iphone-x");
    cy.get(".surveys-view__create-button").click();
    clickCounter += 1;
    cy.url().should("contain", "edit");
    cy.wrap(clickCounter).as("clickCounter");
    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(4);
    });
  });

  it("should allow creating a survey in 3 clicks or fewer in desktop view", () => {
    let clickCounter = 0;
    cy.get(".surveys-view__create-button").click();
    clickCounter += 1;
    cy.url().should("contain", "edit");
    cy.wrap(clickCounter).as("clickCounter");
    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(4);
    });
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});
