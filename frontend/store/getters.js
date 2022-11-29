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

  [get.DIMENSIONS](state) {
    return state.dimensions
  },

  [get.ALERTS](state) {
    return state.alerts
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
