import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_PROFILE_TIMELINE]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const profileTimeline = await api.accountAnalysis.getProfileTimeline(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_PROFILE_TIMELINE, profileTimeline)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_SUMMARY]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const summary = await api.accountAnalysis.getSummary(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_SUMMARY, summary)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_MOST_FREQUENT_POST_TYPES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const postTypes = await api.accountAnalysis.getMostFrequentPostTypes(
        projectId,
        widgetId
      )
      commit(mutator.SET_MOST_FREQUENT_POST_TYPES, postTypes)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_MOST_FREQUENT_MEDIA_TYPES](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const summary = await api.accountAnalysis.getMostFrequentMediaTypes(
        projectId,
        widgetId
      )
      commit(mutator.SET_MOST_FREQUENT_MEDIA_TYPES, summary)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_MOST_ENGAGING_POST_TYPES](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const postTypes = await api.accountAnalysis.getMostEngagingPostTypes(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_MOST_ENGAGING_POST_TYPES, postTypes)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_FOLLOWER_GROWTH]({commit}, {projectId, widgetId, value}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const followerGrowth = await api.accountAnalysis.getFollowerGrowth(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_FOLLOWER_GROWTH, followerGrowth)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_OPTIMAL_POST_LENGTH](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const optimalPostLength = await api.accountAnalysis.getOptimalPostLength(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_OPTIMAL_POST_LENGTH, optimalPostLength)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
}
