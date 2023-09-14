import {get} from '@store/constants'

export default {
  [get.ONLINE_WIDGETS](state) {
    return state
  },

  [get.CLIPPING_FEED_CONTENT_WIDGET](state) {
    return state.clippingFeedContent
  },
}
