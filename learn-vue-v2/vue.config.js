const { defineConfig } = require('@vue/cli-service')
module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    resolve: {extensions: ['', '.js', '.jsx', '.css']},
  }
  // module: {
  //   rules: [
  //     {
  //       test: /\.tsx?$/,
  //       use: 'ts-loader',
  //       exclude: /node_modules/
  //     },
  //     {
  //       test: /\.css$/,
  //       use: [ 'style-loader', 'css-loader' ]
  //     },
  //   ]
  // },

  // css: {
  //   loaderOptions: {
  //     css: {
  //       modules: {
  //         auto: () => true
  //       }
  //     }
  //   }
  // },
  // module: {
  //   loaders: [
  //     { test: /\.css$/, loader: 'style!css' },
  //     { test: /\.jsx?$/, loader: 'babel?stage=0', exclude: /node_modules/ },
  //   ]
  // }
})
