const resolvePlugin = [
  [
    "module-resolver",
    {
      alias: {
        "@": "./src",
        "~": "./",
        "~e2e": "./tests/e2e/"
      }
    }
  ]
];

module.exports = {
  presets: [ "@vue/cli-plugin-babel/preset" ],
  plugins: [ ...resolvePlugin ]
};
