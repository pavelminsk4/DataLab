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

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIdex = state.workspaces.findIndex(
      (w) => w.id === workspace.id
    )
    state.workspaces[currentWorkspaceIdex] = workspace
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

  [mutator.SET_POSTS](state, data) {
    state.posts = data
  },
}
