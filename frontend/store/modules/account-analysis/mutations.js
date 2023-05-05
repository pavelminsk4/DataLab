import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces.map((workspace) => ({
      ...workspace,
      projects: workspace.account_analysis_workspace_projects,
    }))
  },

  [mutator.SET_ACCOUNT_ANALYSIS_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_ACCOUNT_ANALYSIS_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.SET_LIST_OF_PROFILE_HANDLE](state, data) {
    state.listOfProfileHandle = data
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = data
  },
}