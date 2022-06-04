module.exports = {
  root: true,
  env: {
    node: true
  },
  extends: [ "plugin:vue/recommended", "eslint:recommended" ],
  parserOptions: {
    parser: "@babel/eslint-parser",
    sourceType: "module",
    allowImportExportEverywhere: true,
    ecmaVersion: 2019
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
    "vue/valid-v-slot": "warn"
  },
  overrides: [
    {
      files: [
        "**/__tests__/*.{j,t}s?(x)",
        "**/tests/unit/**/*.spec.{j,t}s?(x)"
      ],
      env: {
        jest: true
      }
    }
  ]
};
