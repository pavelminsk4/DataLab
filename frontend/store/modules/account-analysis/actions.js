import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.accountAnalysis.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (error) {
      console.error(error)
      return error
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
      const response = await api.accountAnalysis.createWorkspace(data)
      commit(mutator.SET_ACCOUNT_ANALYSIS_WORKSPACE_ID, response.id)
      commit(
        mutator.SET_ACCOUNT_ANALYSIS_PROJECT_ID,
        response.account_analysis_workspace_projects[0].id
      )
      await dispatch(action.GET_WORKSPACES)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.accountAnalysis.createProject(data)
      commit(mutator.SET_ACCOUNT_ANALYSIS_PROJECT_ID, response.id)
      await dispatch(action.GET_WORKSPACES)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.accountAnalysis.updateWorkspace({
        workspaceId,
        data,
      })
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } catch (error) {
      console.error(error)
      return error
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
    } catch (error) {
      console.error(error)
      return error
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
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.accountAnalysis.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.accountAnalysis.getAllWidgets(
        projectId
      )

      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      return availableWidgets
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_AVAILABLE_WIDGETS](
    {commit, dispatch},
    {projectId, widgetsList}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.accountAnalysis.updateAvailableWidgets(
        {
          projectId,
          data: widgetsList,
        }
      )
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_ACCOUNT_ACTIVITY_POSTS]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.accountAnalysis.getAccountActivityPosts(
        projectId,
        value
      )
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {
        root: true,
      })
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {
        root: true,
      })
      commit(mutator.SET_ACCOUNT_ACTIVITY_POSTS, response.posts)
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_MENTIONS_POSTS]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.accountAnalysis.getMentionsPosts(
        projectId,
        value
      )
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {
        root: true,
      })
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {
        root: true,
      })
      commit(mutator.SET_MENTIONS_POSTS, response.posts || [])
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
}
