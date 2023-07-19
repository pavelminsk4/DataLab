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

  [mutator.SET_BEST_TIMES_TO_POST](state, data) {
    state.bestTimesToPost = data
  },

  [mutator.SET_MENTION_TIMELINE](state, data) {
    state.mentionTimeline = data
  },

  [mutator.SET_MOST_FREQUENT_MENTION_MEDIA_TYPES](state, data) {
    state.mostFrequentMentionMediaTypes = data
  },

  [mutator.SET_AUDIENCE_MENTION_TIME](state, data) {
    state.audienceMentionTime = data
  },

  [mutator.SET_TOP_MENTIONS_BY_ENGAGEMENTS](state, data) {
    state.topMentionsByEngagements = data
  },

  [mutator.SET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS](state, data) {
    state.averageEngagementsByDayForMentions = data
  },

  [mutator.SET_MENTION_SUMMARY](state, data) {
    state.mentionSummary = data
  },

  [mutator.SET_MENTION_SENTIMENT](state, data) {
    state.mentionSentiment = data
  },
}
