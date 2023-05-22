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

  [mutator.SET_MOST_ENGAGING_MEDIA_TYPES](state, data) {
    state.mostEngagingMediaTypes = data
  },

  [mutator.SET_FOLLOWER_GROWTH](state, data) {
    state.followerGrowth = data
  },

  [mutator.SET_OPTIMAL_POST_LENGTH](state, data) {
    state.optimalPostLength = data
  },

  [mutator.SET_TOP_HASHTAGS](state, data) {
    state.topHashtags = data
  },

  [mutator.SET_OPTIMAL_NUMBER_OF_HASHTAGS](state, data) {
    state.optimalNumberOfHashtags = data
  },

  [mutator.SET_AVERAGE_ENGAGEMENTS_BY_DAY](state, data) {
    state.averageEngagementsByDay = data
  },

  [mutator.SET_OPTIMAL_POST_TIME](state, data) {
    state.optimalPostTime = data
  },

  [mutator.SET_TOP_POSTS_BY_ENGAGEMENTS](state, data) {
    state.topPostsByEngagements = data
  },

  [mutator.CLEAR_WIDGETS_DATA](state) {
    for (const widget in state) {
      state[widget] = {}
    }
  },
}
