import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },
  [get.WORKSPACES](state) {
    return state.workspaces
  },

  [get.AVAILABLE_WIDGETS](state) {
    return state.availableWidgets
  },
}
