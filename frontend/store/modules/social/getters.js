import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },
  [get.LOADING_WIDGETS](state) {
    return state.loadingWidgets
  },
  [get.WORKSPACES](state) {
    return state.workspaces
  },
  [get.NEW_WORKSPACE_ID](state) {
    return state.newWorkspaceId
  },
  [get.NEW_PROJECT_ID](state) {
    return state.newProjectId
  },

  [get.PROJECTS](state) {
    return state.projects
  },

  [get.CLIPPING_WIDGETS_DETAILS](state) {
    return state.availableWidgets?.clipping_feed_content
  },

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },

  [get.COUNTRIES](state) {
    return state.countries.results
      .map((country) => country.country)
      .filter((country) => country?.trim())
  },
  [get.LANGUAGES](state) {
    return state.languages.results
      .map((language) => language.language)
      .filter((language) => language?.trim())
  },
  [get.AUTHORS](state) {
    return state.authors.results
      .map((author) => author.user_alias)
      .filter((author) => author?.trim())
  },
  [get.SEARCH_LISTS](state, getters) {
    return {
      authors: getters[get.AUTHORS],
      countries: getters[get.COUNTRIES],
      languages: getters[get.LANGUAGES],
    }
  },
}
