import {fetch} from './api'

// const moduleName = '/online'

export default {
  async getWorkspaces() {
    return fetch('get', '/workspaces/')
  },

  async postSearch(request) {
    return fetch('post', '/search', request)
  },

  async createWorkspace(workspace) {
    return fetch('post', '/workspace/create/', workspace)
  },

  async createNewProject(newProject) {
    return fetch('post', '/projects/', newProject)
  },
}
