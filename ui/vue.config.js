const { defineConfig } = require("@vue/cli-service");
const path = require("path");
const webpack = require("webpack");
const VuetifyLoaderPlugin = require("vuetify-loader/lib/plugin");


const vueSrc = "./src";
module.exports = defineConfig({
  transpileDependencies: true,
  lintOnSave: false,
  configureWebpack: {
    resolve: {
      alias: {
        "@": path.resolve(__dirname, vueSrc),
        "@components": path.resolve(__dirname, `${vueSrc}/components/`),
        "@layouts": path.resolve(__dirname, `${vueSrc}/layouts/`),
        "@api": path.resolve(__dirname, `${vueSrc}/api/`),
        "@assets": path.resolve(__dirname, `${vueSrc}/assets/`),
        "@views": path.resolve(__dirname, `${vueSrc}/views/`),
        "@helpers": path.resolve(__dirname, `${vueSrc}/helpers/`),
        "@plugins": path.resolve(__dirname, `${vueSrc}/plugins/`),
        "@store": path.resolve(__dirname, `${vueSrc}/store/`),
        "@router": path.resolve(__dirname, `${vueSrc}/router/`),
        "@styles": path.resolve(__dirname, `${vueSrc}/styles/`),
        "@tests": path.resolve(__dirname, `${vueSrc}/tests/`)
      },
      extensions: [".js", ".vue", ".json", ".scss"]
    },
    plugins: [
      new VuetifyLoaderPlugin(),
      new webpack.DefinePlugin({
        VUE_APP_API_BASE_URL: JSON.stringify(process.env.VUE_APP_API_BASE_URL)
      }),
      new webpack.ProvidePlugin({
        _: "lodash/lodash.min.js",
        moment: "moment"
      })
    ]
  },
  css: {
    loaderOptions: {
      scss: {
        additionalData: `
          @import "@/styles/variables.scss";
        `
      }
    }
  }
});
