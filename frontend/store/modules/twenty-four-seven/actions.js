import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.twentyFourSeven.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_TFS_WORKSPACE]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.UPDATE_NEW_TFS_WORKSPACE, data, {
        root: true,
      })
      const response = await api.twentyFourSeven.createWorkspace(data)
      commit(mutator.SET_TFS_WORKSPACE_ID, response.id)
      commit(mutator.SET_TFS_PROJECT_ID, response.tfs_workspace_projects[0].id)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_TFS_PROJECT]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.twentyFourSeven.createProject(data)
      commit(mutator.SET_TFS_PROJECT_ID, response.id)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
}
