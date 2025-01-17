import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_PROFILE_TIMELINE]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const profileTimeline = await api.accountAnalysis.getProfileTimeline(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_PROFILE_TIMELINE, profileTimeline)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SUMMARY]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const summary = await api.accountAnalysis.getSummary(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_SUMMARY, summary)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MOST_FREQUENT_POST_TYPES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const postTypes = await api.accountAnalysis.getMostFrequentPostTypes(
        projectId,
        widgetId
      )
      commit(mutator.SET_MOST_FREQUENT_POST_TYPES, postTypes)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MOST_FREQUENT_MEDIA_TYPES](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mostFrequentMediaTypes =
        await api.accountAnalysis.getMostFrequentMediaTypes(projectId, widgetId)
      commit(mutator.SET_MOST_FREQUENT_MEDIA_TYPES, mostFrequentMediaTypes)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MOST_ENGAGING_POST_TYPES](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const postTypes = await api.accountAnalysis.getMostEngagingPostTypes(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_MOST_ENGAGING_POST_TYPES, postTypes)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MOST_ENGAGING_MEDIA_TYPES](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mediaTypes = await api.accountAnalysis.getMostEngagingMediaTypes(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_MOST_ENGAGING_MEDIA_TYPES, mediaTypes)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_FOLLOWER_GROWTH]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const followerGrowth = await api.accountAnalysis.getFollowerGrowth(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_FOLLOWER_GROWTH, followerGrowth)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_OPTIMAL_POST_LENGTH](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const optimalPostLength = await api.accountAnalysis.getOptimalPostLength(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_OPTIMAL_POST_LENGTH, optimalPostLength)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_HASHTAGS]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topHashtags = await api.accountAnalysis.getTopHashtags(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_TOP_HASHTAGS, topHashtags)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  [action.CLEAR_WIDGETS_DATA]({commit}) {
    commit(mutator.CLEAR_WIDGETS_DATA)
  },

  async [action.GET_OPTIMAL_NUMBER_OF_HASHTAGS](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const optimalNumberOfHashtags =
        await api.accountAnalysis.getOptimalNumberOfHashtags(
          projectId,
          widgetId,
          value
        )
      commit(mutator.SET_OPTIMAL_NUMBER_OF_HASHTAGS, optimalNumberOfHashtags)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AVERAGE_ENGAGEMENTS_BY_DAY](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const averageEngagements =
        await api.accountAnalysis.getAverageEngagemensByDay(
          projectId,
          widgetId,
          value
        )
      commit(mutator.SET_AVERAGE_ENGAGEMENTS_BY_DAY, averageEngagements)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_OPTIMAL_POST_TIME]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const optimalPostTime = await api.accountAnalysis.getOptimalPostTime(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_OPTIMAL_POST_TIME, optimalPostTime)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_POSTS_BY_ENGAGEMENTS](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topPostsByEngagements =
        await api.accountAnalysis.getTopPostsByEngagements(
          projectId,
          widgetId,
          value
        )
      commit(mutator.SET_TOP_POSTS_BY_ENGAGEMENTS, topPostsByEngagements)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_BEST_TIMES_TO_POST](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const bestTimesToPost = await api.accountAnalysis.getBestTimesToPost(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_BEST_TIMES_TO_POST, bestTimesToPost)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MENTION_TIMELINE]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mentionTimeline = await api.accountAnalysis.getMentionTimeline(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_MENTION_TIMELINE, mentionTimeline)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MOST_FREQUENT_MENTION_MEDIA_TYPES](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mostFrequentMentionMediaTypes =
        await api.accountAnalysis.getMostFrequentMentionMediaTypes(
          projectId,
          widgetId
        )
      commit(
        mutator.SET_MOST_FREQUENT_MENTION_MEDIA_TYPES,
        mostFrequentMentionMediaTypes
      )
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AUDIENCE_MENTION_TIME]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const audienceMentionTime =
        await api.accountAnalysis.getAudienceMentionTime(projectId, widgetId)
      commit(mutator.SET_AUDIENCE_MENTION_TIME, audienceMentionTime)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_MENTIONS_BY_ENGAGEMENTS](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topMentionsByEngagements =
        await api.accountAnalysis.getTopMentionsByEngagements(
          projectId,
          widgetId
        )
      commit(mutator.SET_TOP_MENTIONS_BY_ENGAGEMENTS, topMentionsByEngagements)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const averageEngagementsForMentions =
        await api.accountAnalysis.getAverageEngagemensByDayForMentions(
          projectId,
          widgetId
        )
      commit(
        mutator.SET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS,
        averageEngagementsForMentions
      )
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MENTION_SUMMARY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mentionSummary = await api.accountAnalysis.getMentionSummary(
        projectId,
        widgetId
      )
      commit(mutator.SET_MENTION_SUMMARY, mentionSummary)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_MENTION_SENTIMENT]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const mentionSentiment = await api.accountAnalysis.getMentionSentiment(
        projectId,
        widgetId
      )
      commit(mutator.SET_MENTION_SENTIMENT, mentionSentiment)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },
}
