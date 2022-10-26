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

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },
}
