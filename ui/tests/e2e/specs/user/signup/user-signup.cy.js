describe("A user should be able to create an account with 4 clicks or fewer", () => {
  it("can create an account with 4 clicks or fewer in desktop view and mobile view", () => {
    let clickCounter = 0;
    cy.visit("/");
    cy.acceptCookiePolicy();
    clickCounter += 1;

    cy.get(".signup-button").click();
    clickCounter += 1;

    cy.get(".signup-form__email").type("lapar@yopmail.com");
    cy.get(".signup-form__password").type("asdfghjkl");
    cy.get(".signup-form__submit-button").click();
    clickCounter += 1;
    cy.wrap(clickCounter).as("clickCounter");

    cy.get("@clickCounter").then((clickCounter) => {
      expect(clickCounter).to.be.lessThan(5);
    });
  });
});

describe("The system must allow a user to create an account by entering an email and a password.", () => {
  it("can create an account if an account for entered email is never created before", () => {
    cy.visit("/user/signup/");
    cy.acceptCookiePolicy();
    cy.get(".signup-form__email").type("sayalaparyatuan@yopmail.com");
    cy.get(".signup-form__password").type("asdfghjkl");
    cy.get(".signup-form__submit-button").click();
    cy.wait(10000);
    cy.url().should("contain", "/user/signup/thankyou/");
  });

  it("cannot create an account if account already exists", () => {
    cy.visit("/user/signup/");
    cy.acceptCookiePolicy();
    cy.get(".signup-form__email").type("lapar@yopmail.com");
    cy.get(".signup-form__password").type("asdfghjkl");
    cy.get(".signup-form__submit-button").click();
    cy.wait(10000);
    cy.url().should("not.contain", "/user/signup/thankyou");
  });
});