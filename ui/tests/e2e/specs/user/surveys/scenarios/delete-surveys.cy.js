describe("A survey owner should be able to edit a survey that they own with 3 clicks or fewer after a successful login.", () => {
  beforeEach(() => {
    cy.loginAsUserFromBrowser();
    cy.wait(1000);
    cy.visit("/user/surveys");
    cy.acceptPrivacyPolicy();
    cy.acceptTnC();
  });

  it("should allow editing a survey in 3 clicks or fewer in desktop view", () => {
    let clickCounter = 0;
    cy.get("body").then(($body) => {
      if (!$body.text().includes("Reach your respondents")) {
        cy.get(".surveys-view__delete-button").first().click();
        clickCounter += 1;
        cy.wrap(clickCounter).as("clickCounter");
        cy.get("@clickCounter").then((clickCounter) => {
          expect(clickCounter).to.be.lessThan(4);
        });
      }
    });
  });

  it("should allow editing a survey in 3 clicks or fewer in mobile view", () => {
    let clickCounter = 0;
    cy.viewport("iphone-x");
    cy.get("body").then(($body) => {
      if (!$body.text().includes("Reach your respondents")) {
        cy.get(".user-surveys-list__item").first().click();
        clickCounter += 1;

        cy.get(".detail-questions__delete-button").first().click();
        clickCounter += 1;

        cy.wrap(clickCounter).as("clickCounter");
        cy.get("@clickCounter").then((clickCounter) => {
          expect(clickCounter).to.be.lessThan(4);
        });
      }
    });
  });

  afterEach(() => {
    cy.logoutFromBrowser();
  });
});
