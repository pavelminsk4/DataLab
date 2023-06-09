import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.comparison.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_NEW_COMPARISON_WORKSPACE]({commit}, data) {
    commit(mutator.SET_NEW_COMPARISON_WORKSPACE, data)
  },

  async [action.UPDATE_NEW_COMPARISON_PROJECT]({commit}, data) {
    commit(mutator.SET_NEW_COMPARISON_PROJECT, data)
  },
}
