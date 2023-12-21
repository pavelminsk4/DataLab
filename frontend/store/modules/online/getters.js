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

  [get.CURRENT_PROJECT](state) {
    return state.currentProject
  },

  [get.CURRENT_WORKSPACE](state) {
    return state.currentWorkspace
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

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },

  [get.COUNTRIES](state) {
    return state.countries
      .map((country) => country.country)
      .filter((country) => country?.trim())
  },

  [get.LANGUAGES](state) {
    return state.languages
      .map((language) => language.language)
      .filter((language) => language?.trim())
  },

  [get.SOURCES](state) {
    return state.sources
      .map((source) => source.source1)
      .filter((source) => source?.trim())
  },

  [get.AUTHORS](state) {
    return state.authors
      .map((author) => author.entry_author)
      .filter((author) => author?.trim())
  },

  [get.SEARCH_LISTS](state, getters) {
    return {
      authors: getters[get.AUTHORS],
      countries: getters[get.COUNTRIES],
      languages: getters[get.LANGUAGES],
      sources: getters[get.SOURCES],
    }
  },
}
