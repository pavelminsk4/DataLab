import {mutator} from '@store/constants'

export default {
  [mutator.SET_PROFILE_TIMELINE](state, data) {
    state.profileTimeline = data
  },
  [mutator.SET_SUMMARY](state, data) {
    state.summary = data
  },

  [mutator.SET_MOST_FREQUENT_POST_TYPES](state, data) {
    state.mostFrequentPostTypes = data
  },
  [mutator.SET_MOST_FREQUENT_MEDIA_TYPES](state, data) {
    state.mostFrequentMediaTypes = data
  },

  [mutator.SET_MOST_ENGAGING_POST_TYPES](state, data) {
    state.mostEngagingPostTypes = data
  },
}
