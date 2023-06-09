import {mutator} from '@store/constants'

export default {
  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces
  },

  [mutator.SET_NEW_COMPARISON_WORKSPACE](state, data) {
    if (data) {
      state.newWorkspace = {
        ...state.newWorkspace,
        ...data,
      }
    }
  },

  [mutator.SET_NEW_COMPARISON_PROJECT](state, data) {
    if (data) {
      state.newComparisonProject = {
        ...state.newComparisonProject,
        ...data,
      }
    }
  },

  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
}
