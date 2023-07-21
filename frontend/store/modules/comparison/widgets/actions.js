import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_SUMMARY_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_SUMMARY_WIDGETS_LOADING, true)
    try {
      const summary = await api.comparison.getSummaryWidgets(projectId)
      commit(mutator.SET_SUMMARY_WIDGETS, summary)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_SUMMARY_WIDGETS_LOADING, false)
    }
  },
  async [action.GET_SENTIMENT_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_SENTIMENT_WIDGETS_LOADING, true)
    try {
      const sentiment = await api.comparison.getSentimentWidgets(projectId)
      commit(mutator.SET_SENTIMENT_WIDGETS, sentiment)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_SENTIMENT_WIDGETS_LOADING, false)
    }
  },
  async [action.GET_DEMOGRAPHY_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_DEMOGRAPHY_WIDGETS_LOADING, true)
    try {
      const data = await api.comparison.getDemographyWidgets(projectId)
      commit(mutator.SET_DEMOGRAPHY_WIDGETS, data)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_DEMOGRAPHY_WIDGETS_LOADING, false)
    }
  },
}
