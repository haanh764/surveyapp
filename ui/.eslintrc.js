module.exports = {
  root: true,
  env: {
    node: true
  },
  "extends": [
    "plugin:vue/recommended",
    "eslint:recommended"
  ],
  parserOptions: {
    parser: "@babel/eslint-parser",
    "sourceType": "module",
    "allowImportExportEverywhere": true,
    "ecmaVersion": 2019
  },
  rules: {
    "no-console": process.env.NODE_ENV === "production" ? "warn" : "off",
    "no-debugger": process.env.NODE_ENV === "production" ? "warn" : "off",
    "comma-dangle": "error",
    "quotes": [
      "error",
      "double"
    ],
    "linebreak-style": [
      "error",
      "unix"
    ],
    "array-bracket-spacing": [
      "error",
      "always"
    ],
    "semi": [
      "error",
      "always"
    ],
    "eol-last": [
      "error",
      "always"
    ],
    "vue/multi-word-component-names": "warn"
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


