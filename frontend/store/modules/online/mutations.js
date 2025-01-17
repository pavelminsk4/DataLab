import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  [mutator.SET_DOWNLOADING_INSTANT_REPORT](state, downloadingInstantReport) {
    state.downloadingInstantReport = downloadingInstantReport
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces
  },

  [mutator.SET_PROJECT](state, project) {
    state.currentProject = project
  },

  [mutator.SET_WORKSPACE](state, workspace) {
    state.currentWorkspace = workspace
  },

  [mutator.SET_NEW_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_NEW_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = data
  },

  [mutator.SET_COUNTRIES](state, countries) {
    state.countries = countries
  },

  [mutator.SET_LANGUAGES](state, languages) {
    state.languages = languages
  },

  [mutator.SET_SOURCES](state, sources) {
    state.sources = sources
  },

  [mutator.SET_AUTHORS](state, authors) {
    state.authors = authors
  },

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
  },

  [mutator.SET_CLIPPING_FEED_CONTENT_WIDGET](state, {widgetId, data}) {
    state.clippingFeedContent = {id: widgetId, data}
  },

  [mutator.RESET_PROJECT_STATE](state) {
    state.currentProject = null
  },
}
