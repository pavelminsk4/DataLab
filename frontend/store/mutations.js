import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_PROJECTS](state, projects) {
    state.projects = projects
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces
  },

  [mutator.SET_USER_INFORMATION](state, userId) {
    state.userId = userId
  },

  [mutator.SET_NEW_WORKSPACE](state, workspaceInfo) {
    state.newWorkspace = {...state.newWorkspace, ...workspaceInfo}
  },

  [mutator.SET_KEYWORDS_LIST](state, keywords) {
    state.keywords = [...state.keywords, ...keywords]
  },

  [mutator.DELETE_KEYWORDS_LIST](state, index) {
    state.keywords.splice(index, 1)
  },
}
