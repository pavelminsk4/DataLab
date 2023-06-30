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
}
