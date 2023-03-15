import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
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
}
