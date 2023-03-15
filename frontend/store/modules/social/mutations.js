import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
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
    const currentWorkspaceIdex = state.workspaces.findIndex(
      (w) => w.id === workspace.id
    )
    state.workspaces[currentWorkspaceIdex] = workspace
  },

  [mutator.SET_PROJECTS](state, projects) {
    state.projects = projects
  },
}
