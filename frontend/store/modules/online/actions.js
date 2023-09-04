import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.online.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.postSearch(data)
      commit(mutator.SET_SEARCH_DATA, response.posts, {root: true})
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {root: true})
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.createWorkspace(workspace)
      commit(mutator.SET_NEW_WORKSPACE_ID, response.id)
      commit(mutator.SET_NEW_PROJECT_ID, response.projects[0].id)
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit, dispatch}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.createNewProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(action.GET_USER_INFORMATION, null, {root: true})
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
}
