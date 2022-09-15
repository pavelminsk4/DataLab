import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.LOGOUT]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.logout()
      window.location.href = '/accounts/login/'
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_USER_INFORMATION]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const user = await api.getLoggedUser()
      commit(mutator.SET_USER_INFORMATION, user.id)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createWorkspace(workspace)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit}, newProject) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createNewProject(newProject)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_NEW_WORKSPACE]({commit}, workspaceInfo) {
    commit(mutator.SET_NEW_WORKSPACE, workspaceInfo)
  },

  async [action.UPDATE_KEYWORDS_LIST]({commit}, keywords) {
    commit(mutator.SET_KEYWORDS_LIST, keywords)
  },

  async [action.CLEAR_KEYWORDS_LIST]({commit}, index) {
    commit(mutator.DELETE_KEYWORDS_LIST, index)
  },
}
