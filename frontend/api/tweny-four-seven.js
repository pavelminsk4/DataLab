import {fetch} from './api'

const moduleName = '/twenty_four_seven'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/`, workspace)
  },

  async createProject(project) {
    return fetch('post', `${moduleName}/projects/ `, project)
  },
}
