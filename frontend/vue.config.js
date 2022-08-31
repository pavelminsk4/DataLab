const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')

module.exports = {
  publicPath:
    process.env.NODE_ENV === 'productio   n'
      ? '/static/dist/'
      : 'http://localhost:8080',

  chainWebpack: (config) => {
    config.optimization.splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{filename: '../frontend/webpack-stats.json'}])

    config.resolve.alias
      .set('@api', path.resolve(__dirname, './api/'))
      .set('@components', path.resolve(__dirname, './src/components'))
      .set('@store', path.resolve(__dirname, './store/'))
      .set('@router', path.resolve(__dirname, './router/'))
  },
}
