import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.comparison.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.comparison.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit, dispatch}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.comparison.createWorkspace(workspace)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.comparison.updateWorkspace({
        workspaceId,
        data,
      })
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACES_PROJECTS](
    {commit, dispatch},
    {workspaceId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.comparison.updateWorkspacesProjects({
        workspaceId,
        data,
      })
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE_PROJECT](
    {commit, dispatch},
    {workspaceId, projectId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.comparison.deleteWorkspaceProject(workspaceId, projectId)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.comparison.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
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

  async [action.CLEAR_WIDGETS_DATA]({commit}) {
    commit(mutator.CLEAR_WIDGETS_DATA)
  },
}
