import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces.map((workspace) => ({
      ...workspace,
      projects: workspace.tfs_workspace_projects,
    }))
  },

  [mutator.SET_TFS_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_TFS_PROJECT_ID](state, id) {
    state.newProjectId = id
  },
}
