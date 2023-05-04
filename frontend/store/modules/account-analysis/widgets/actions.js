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
}
