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
      },
      passWithNoTests: true,
    },
  ],
}
