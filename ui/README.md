# ui

## Installation

### Yarn

Windows:

- Download and install NodeJs: https://nodejs.org/en/download/
- Enter your cmd and make sure NodeJs is already installed by typing `npm --version`
- Install yarn via cmd with `npm install -g yarn` https://classic.yarnpkg.com/lang/en/docs/install/#windows-stable

Linux:

- Download and install yarn via apt-get
  `sudo apt-get install yarnpkg`

### Vue.js devtools

Install Vue.js devtools on your favourite browser. This devtool is really helpful to track component/state changes in Vue environment.
https://devtools.vuejs.org/guide/installation.html

### VSCode

It's recommended (but not necessary) to use VSCode for better quality code: https://code.visualstudio.com/download

Configure VSCode's settings.json and make sure the formatOnSave mode is enabled, then adjust your settings.json:
https://github.com/vuejs/eslint-plugin-vue/blob/master/.vscode/settings.json

## Project setup

After installing nodejs, you can install yarn by running `npm install -g yarn` in your command line.

### Installing the packages

Run `yarn` to download the packages specified in the `package.json`. The packages will be downloaded to the `node_modules` folder. The command should be run everytime a new package is added in the `package.json`.

### Compiles and hot-reloads for development

```
yarn serve
```

You can specify the port by adding the `--port` flag, for example:

```
yarn serve --port 3000
```

### Compiles and minifies for production

```
yarn build
```

### Lints and fixes files

```
yarn lint
```

Add `--fix` flag to fix the files automatically

### Customize configuration

See [Configuration Reference](https://cli.vuejs.org/config/).

## Tests:E2E

The end to end testing is done by running:
`yarn test-cypress`
Running this command will open the cypress dialog (it's integrated with browser, you can choose either of Chrome, Firefox, or Edge).

The test files can be found in the `tests/e2e/specs` folder. All tests files are named by following `{name}.cy.js`.
