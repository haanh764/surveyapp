module.exports = {
  root: true,
  env: {
    node: true,
    es6: true,
    browser: true
  },
  plugins: [ "cypress" ],
  extends: [
    "eslint:recommended",
    "plugin:cypress/recommended",
    "plugin:vue/recommended"
  ],
  parserOptions: {
    parser: "@babel/eslint-parser",
    sourceType: "module",
    allowImportExportEverywhere: true
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "comma-dangle": "warn",
    quotes: [ "warn", "double" ],
    "linebreak-style": [ "warn", "unix" ],
    "array-bracket-spacing": [ "warn", "always" ],
    semi: [ "warn", "always" ],
    "eol-last": [ "warn", "always" ],
    "vue/multi-word-component-names": "warn",
    "vue/no-v-text-v-html-on-component": "warn",
    "vue/no-unused-vars": "warn",
    "vue/valid-v-slot": "off",
    "vue/no-mutating-props": "warn", // bad practice, should be removed later
    "jest/expect-expect": "off",
    "cypress/no-unnecessary-waiting": "off" // bad practice, but needed because docker is slow
  },
  globals: {
    _: "readonly",
    moment: "readonly",
    NODE_ENV: "readonly",
    VUE_APP_API_BASE_URL: "readonly",
    IS_API_MOCKED: "readonly",
    cy: "readonly",
    Cypress: "readonly"
  },
  overrides: [
    {
      files: [ "**/__tests__/*.{j,t}s?(x)", "**/tests/e2e/**/*.cy.{j,t}s?(x)" ],
      env: {
        mocha: true
      }
    }
  ]
};
