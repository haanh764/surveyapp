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
Configure settings.json and make sure the formatOnSave mode is enabled, then adjust your settings.json: 
https://github.com/vuejs/eslint-plugin-vue/blob/master/.vscode/settings.json 

## Project setup
If you are using npm: 
```
npm install 
```

If you are using yarn: 
```
yarn
```
### Compiles and hot-reloads for development
If you are using npm: 
```
npm run serve
```

If you are using yarn: 
```
yarn serve
```

### Compiles and minifies for production
```
npm run build
```

If you are using yarn: 
```
yarn build
```


### Lints and fixes files
```
npm run lint
```

If you are using yarn: 
```
yarn lint
```

Add `--fix` flag to fix the files automatically

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).
