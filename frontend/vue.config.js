const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  publicPath: process.env.NODE_ENV === 'production' ? '/static/dist/' : 'http://localhost:8080',

  chainWebpack: config => {

    config.optimization
        .splitChunks(false)

    config
        .plugin('BundleTracker')
        .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

    config.resolve.alias
        .set('__STATIC__', 'static')
  }
}
