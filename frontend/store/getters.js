import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },

  [get.PROJECTS](state) {
    return state.projects
  },

  [get.WORKSPACES](state) {
    return state.workspaces
  },

  [get.USER_INFO](state) {
    return state.userInfo
  },

  [get.CURRENT_STEP](state) {
    return state.currentStep
  },

  [get.KEYWORDS](state) {
    return state.keywords
  },

  [get.NEW_PROJECT](state) {
    return state.newProject
  },

  [get.NEW_WORKSPACE](state) {
    return state.newWorkspace
  },

  [get.SEARCH_DATA](state) {
    return state.searchData
  },

  [get.COUNTRIES](state) {
    return state.countries.map((el) => el.name)
  },

  [get.LANGUAGES](state) {
    return state.languages.map((el) => el.language)
  },

  [get.SOURCES](state) {
    return state.sources.map((el) => el.source1)
  },

  [get.AUTHORS](state) {
    return state.authors.map((el) => el.entry_author)
  },

  [get.ADDITIONAL_FILTERS](state) {
    return state.additionalFilters
  },

  [get.SUMMARY_WIDGET](state) {
    return state.summary
  },

  [get.VOLUME_WIDGET](state) {
    return state.volume
  },

  [get.CLIPPING_FEED_CONTENT_WIDGET](state) {
    return state.clippingFeedContent
  },

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },

  [get.TOP_AUTHORS](state) {
    return state.topAuthors
  },

  [get.TOP_COUNTRIES](state) {
    return state.topCountries
  },

  [get.TOP_BRANDS](state) {
    return state.topBrands
  },

  [get.TOP_LANGUAGES](state) {
    return state.topLanguages
  },

  [get.SENTIMENT_TOP_SOURCES](state) {
    return state.sentimentTopSources
  },

  [get.SENTIMENT_TOP_COUNTRIES](state) {
    return state.sentimentTopCountries
  },

  [get.SENTIMENT_TOP_LANGUAGES](state) {
    return state.sentimentTopLanguages
  },

  [get.SENTIMENT_TOP_AUTHORS](state) {
    return state.sentimentTopAuthors
  },

  [get.SENTIMENT_FOR_PERIOD](state) {
    return state.sentimentForPeriod
  },

  [get.CONTENT_VOLUME_TOP_SOURCES](state) {
    return state.contentVolumeTopSources
  },

  [get.DIMENSIONS](state) {
    return state.dimensions
  },

  [get.ALERTS](state) {
    return state.alerts
  },

  [get.REGULAR_REPORTS](state) {
    return state.regularReports
  },

  [get.SELECTED_DIMENSIONS](state) {
    return state.selectedDimensions
  },

  [get.DIMENSION_LANGUAGES](state) {
    return state.dimensionLanguages
  },

  [get.DIMENSION_COUNTRIES](state) {
    return state.dimensionCountries
  },

  [get.DIMENSION_AUTHORS](state) {
    return state.dimensionAuthors
  },

  [get.TEMPLATES](state) {
    return state.templates
  },

  [get.NEW_PROJECT_ID](state) {
    return state.newProjectId
  },

  [get.NEW_WORKSPACE_ID](state) {
    return state.newWorkspaceId
  },
}
