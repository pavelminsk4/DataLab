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

  [get.KEYWORDS](state) {
    return state.keywords
  },

  [get.NEW_PROJECT](state) {
    return state.newProject
  },

  [get.SEARCH_DATA](state) {
    return state.searchData
  },

  [get.COUNTRIES](state) {
    return state.countries
  },

  [get.LANGUAGES](state) {
    return state.languages
  },

  [get.ADDITIONAL_FILTERS](state) {
    return state.additionalFilters
  },
}
