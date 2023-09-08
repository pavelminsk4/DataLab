import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },

  [get.WORKSPACES](state) {
    return state.workspaces
  },

  [get.CLIPPING_WIDGETS_DETAILS](state) {
    return state.availableWidgets?.clipping_feed_content
  },
}
