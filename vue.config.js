const BundleTracker = require('webpack-bundle-tracker')
const path = require('path')

module.exports = {
  publicPath:
    process.env.NODE_ENV === 'production'
      ? '/static/dist/'
      : 'http://localhost:8080',

  pages: {
    app: 'frontend/src/main.js',
  },

  chainWebpack: (config) => {
    config.optimization.splitChunks(false)

    config
      .plugin('BundleTracker')
      .use(BundleTracker, [{filename: './webpack-stats.json'}])

    config.resolve.alias
      .set('@api', path.resolve(__dirname, 'frontend/api/'))
      .set('@components', path.resolve(__dirname, 'frontend/src/components'))
      .set('@views', path.resolve(__dirname, 'frontend/src/views'))
      .set('@lib', path.resolve(__dirname, 'frontend/src/lib'))
      .set('@store', path.resolve(__dirname, 'frontend/store/'))
      .set('@router', path.resolve(__dirname, 'frontend/router/'))
      .set('@assets', path.resolve(__dirname, 'frontend/src/assets'))
  },
}
