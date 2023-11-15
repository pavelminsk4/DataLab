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
        '^@/(.*)$': '<rootDir>/frontend/src/$1',
        '^@store(.*)$': '<rootDir>/frontend/store/$1',
        '^@api(.*)$': '<rootDir>/frontend/api/$1',
        '^@lib(.*)$': '<rootDir>/frontend/src/lib/$1',
        '^@components(.*)$': '<rootDir>/frontend/src/components/$1',
        '^@router(.*)$': '<rootDir>/frontend/router/$1',
        '^@views(.*)$': '<rootDir>/frontend/src/views/$1',
        '^@assets(.*)$': '<rootDir>/frontend/src/assets/$1',
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
      testMatch: ['<rootDir>/frontend/**/?(*.)+(spec).[jt]s?(x)'],
    },
  ],
  testEnvironmentOptions: {
    customExportConditions: ['node', 'node-addons'],
  },
}
