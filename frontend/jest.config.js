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
      moduleNameMapper: {
        '@/(.*)$': '<rootDir>/src/$1',
        '@store/(.*)$': '<rootDir>/store/$1',
        '@components/(.*)$': '<rootDir>/src/components/$1',
      },
      testEnvironmentOptions: {
        customExportConditions: ['node', 'node-addons'],
      },
      transform: {
        '^.+\\.js$': 'babel-jest',
        '^.+\\.vue$': '@vue/vue3-jest',
        '.+\\.(css|styl|less|sass|scss|png|jpg|ttf|woff|woff2|webp)$':
          'jest-transform-stub',
      },
      testEnvironment: 'jsdom',
      passWithNoTests: true,
      testMatch: ['<rootDir>/**/?(*.)+(spec).[jt]s?(x)'],
    },
  ],
  testEnvironmentOptions: {
    customExportConditions: ['node', 'node-addons'],
  },
}
