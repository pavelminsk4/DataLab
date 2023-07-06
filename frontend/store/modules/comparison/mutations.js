import {mutator} from '@store/constants'
import {newProject, newWorkspace} from './state'

export default {
  [mutator.SET_PROJECTS](state, projects) {
    state.modulesProjects = projects
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces
  },

  [mutator.SET_NEW_COMPARISON_WORKSPACE](state, data) {
    if (data) {
      state.newWorkspace = {
        ...state.newWorkspace,
        ...data,
      }
    } else {
      state.newWorkspace = newWorkspace
      state.newProject = newProject
    }
  },

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
  },

  [mutator.SET_NEW_COMPARISON_PROJECT](state, data) {
    if (data) {
      state.newProject = {
        ...state.newProject,
        ...data,
      }
    }
  },

  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.CLEAR_WIDGETS_DATA](state) {
    Object.values(state.widgets).forEach((feature) => (feature.widgets = []))
  },
}
