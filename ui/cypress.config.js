const { defineConfig } = require("cypress");
const webpackPreprocessor = require("@cypress/webpack-preprocessor");
const path = require("path");

const options = {
  resolve: {
    alias: {
      "~": path.join(__dirname, "./"),
      "@": path.join(__dirname, "./src/"),
      "~e2e": path.join(__dirname, "./tests/e2e/"),
    },
  },
};

module.exports = defineConfig({
  fixturesFolder: "tests/e2e/fixtures",
  screenshotsFolder: "tests/e2e/screenshots",
  videosFolder: "tests/e2e/videos",
  env: {
    VUE_APP_API_BASE_URL: "http://localhost:8000/api/",
  },
  e2e: {
    setupNodeEvents(on) {
      on("file:preprocessor", webpackPreprocessor(options));
    },
    baseUrl: "http://localhost:3000",
    specPattern: "tests/e2e/specs/**/*.cy.{js,jsx,ts,tsx}",
    supportFile: "tests/e2e/support/index.js",
  },
});
