import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.accountAnalysis.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE](
    {commit, dispatch},
    data
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.UPDATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE, data, {
        root: true,
      })
      await api.accountAnalysis.createWorkspace(data)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.accountAnalysis.createProject(data)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_LIST_OF_PROFILE_HANDLE]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const listOfProfileHandle =
        await api.accountAnalysis.getListOfProfileHandle()
      commit(mutator.SET_LIST_OF_PROFILE_HANDLE, listOfProfileHandle)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_ACCOUNT_ANALYSIS_PROJECT](
    {commit, dispatch},
    projectId
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.accountAnalysis.deleteAccountAnalysisProject(projectId)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
}
