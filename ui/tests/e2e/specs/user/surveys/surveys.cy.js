describe("The system must show the list of surveys that a user owns after they have logged-in.", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
    cy.acceptPrivacyPolicy();
    cy.acceptTnC();
  });

  it("should show the list in mobile view", () => {
    cy.viewport("iphone-x");
    cy.get(".user-surveys-list").should("be.visible");
  });

  it("should show the list in desktop view", () => {
    cy.get(".user-surveys-table").should("be.visible");
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});

describe("A survey owner should be able to see the list of all surveys that they own with 2 clicks or fewer after a successful login.", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
    cy.acceptPrivacyPolicy();
    cy.acceptTnC();
  });

  it("should allow seeing list of surveys with 2 clicks or fewer in mobile view", () => {
    let clickCounter = 0;
    cy.viewport("iphone-x");
    cy.get(".user-surveys-list").should("be.visible");
    cy.wrap(clickCounter).as("clickCounter");
    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(2);
    });
  });

  it("should allow seeing list of surveys with 2 clicks or fewer in desktop view", () => {
    let clickCounter = 0;
    cy.get(".user-surveys-table").should("be.visible");
    cy.wrap(clickCounter).as("clickCounter");
    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(2);
    });
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});
