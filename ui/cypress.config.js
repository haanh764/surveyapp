const { defineConfig } = require("cypress");
const webpackPreprocessor = require("@cypress/webpack-preprocessor");
const path = require("path");

const options = {
  resolve: {
    alias: {
      "~": path.join(__dirname, "./"),
      "@": path.join(__dirname, "./src/"),
      "~e2e": path.join(__dirname, "./tests/e2e/")
    }
  }
};

module.exports = defineConfig({
  fixturesFolder: "tests/e2e/fixtures",
  screenshotsFolder: "tests/e2e/screenshots",
  videosFolder: "tests/e2e/videos",
  // mimic the env variables in process.env, so "false" instead of false
  // somehow cypress cannot read process.env so the value is hard coded twice
  // to do: should be fixed later
  env: {
    VUE_APP_API_BASE_URL: "http://localhost:8080/api/",
    IS_API_MOCKED: "false"
  },
  e2e: {
    setupNodeEvents(on, config) {
      config.env = process.env;
      on("file:preprocessor", webpackPreprocessor(options));
    },
    baseUrl: "http://localhost:3000",
    specPattern: "tests/e2e/specs/**/*.cy.{js,jsx,ts,tsx}",
    supportFile: "tests/e2e/support/index.js"
  }
});
