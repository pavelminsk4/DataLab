import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.CREATE_NEW_ALERT]({commit, dispatch}, {data, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createAlert(data)
      await dispatch(action.GET_ALERTS, projectId)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_ALERTS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const alerts = await api.getAlerts(projectId)
      commit(mutator.SET_ALERTS, alerts)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_ALERT]({commit, dispatch}, {data, alertId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateAlert({data, alertId})
      await dispatch(action.GET_ALERTS, data.project)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_ALERT]({commit, dispatch}, {alertId, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteAlert(alertId)
      await dispatch(action.GET_ALERTS, projectId)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_NEW_ALERT]({commit}, data) {
    commit(mutator.SET_NEW_ALERT, data)
  },
  async [action.CLEAR_NEW_ALERT]({commit}) {
    commit(mutator.SET_NEW_ALERT)
  },
}
