import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  [mutator.SET_DOWNLOADING_INSTANT_REPORT](state, downloadingInstantReport) {
    state.downloadingInstantReport = downloadingInstantReport
  },
  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces.map((workspace) => ({
      ...workspace,
      projects: workspace.social_workspace_projects,
    }))
  },
  [mutator.SET_NEW_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },
  [mutator.SET_NEW_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
  },

  [mutator.SET_PROJECTS](state, projects) {
    state.projects = projects
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
  [mutator.SET_AUTHORS](state, authors) {
    state.authors = authors
  },
}
