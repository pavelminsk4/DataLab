import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },

  [get.PROJECTS](state) {
    return state.projects
  },

  [get.WORKSPACES](state) {
    return state.workspaces
  },

  [get.USER_ID](state) {
    return state.userId
  },

  [get.KEYWORDS](state) {
    return state.keywords
  },
}
