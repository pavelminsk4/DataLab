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

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.twentyFourSeven.updateWorkspace({
        workspaceId,
        data,
      })
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_PROJECT]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TFS_ITEMS]({commit}, {projectId, status, page}) {
    commit(mutator.SET_LOADING, true)
    try {
      const items = await api.twentyFourSeven.getItems(projectId, status, page)
      commit(mutator.SET_TFS_ITEMS, {items, status})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TFS_RELATED_CONTENT]({commit}, itemId) {
    commit(mutator.SET_LOADING, true)
    try {
      const relatedContent = await api.twentyFourSeven.getRelatedContent(itemId)
      commit(mutator.SET_TFS_RELATED_CONTENT, relatedContent)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_TFS_ITEM_STATUS](
    {commit, dispatch},
    {projectId, itemId, value, oldStatus, page}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.updateItemStatus(projectId, itemId, value)
      await dispatch(action.GET_TFS_ITEMS, {
        projectId,
        status: value.status,
        page,
      })
      await dispatch(action.GET_TFS_ITEMS, {projectId, status: oldStatus, page})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CLEAR_TFS_ITEMS]({commit}) {
    commit(mutator.RESET_TFS_ITEMS)
  },
}
