/*
 * For a detailed explanation regarding each configuration property, visit:
 * https://jestjs.io/docs/configuration
 */

module.exports = {
  clearMocks: true,
  collectCoverage: true,
  coverageDirectory: 'coverage',
  verbose: true,
  projects: [
    {
      moduleFileExtensions: ['js', 'vue'],
      moduleNameMapper: {
        '^@/(.*)$': '<rootDir>/src/$1',
        '^@store(.*)$': '<rootDir>/store/$1',
        '^@api(.*)$': '<rootDir>/api/$1',
        '^@lib(.*)$': '<rootDir>/src/lib/$1',
        '^@components(.*)$': '<rootDir>/src/components/$1',
        '^@router(.*)$': '<rootDir>/router/$1',
        '\\.(css|less|scss|sass)$': 'identity-obj-proxy',
      },
      testEnvironmentOptions: {
        customExportConditions: ['node'],
      },
      moduleFileExtensions: ['js', 'json', 'vue'],
      transform: {
        '^.+\\.js$': 'babel-jest',
        '^.+\\.vue$': '@vue/vue3-jest',
        '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2|webp|svg)$':
          'jest-transform-stub',
      },
      testEnvironment: 'jsdom',
      passWithNoTests: true,
      transformIgnorePatterns: ['/node_modules/(?!vuewordcloud)'],
      testPathIgnorePatterns: ['/node_modules/'],
      testMatch: ['<rootDir>/**/?(*.)+(spec).[jt]s?(x)'],
    },
  ],
  testEnvironmentOptions: {
    customExportConditions: ['node', 'node-addons'],
  },
}
