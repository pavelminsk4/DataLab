import {fetch} from './api'

const moduleName = '/account_analysis'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async getListOfProfileHandle() {
    return fetch('get', `${moduleName}/list_of_profile_handle`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/create/`, workspace)
  },

  async createProject(project) {
    return fetch('post', `${moduleName}/projects/ `, project)
  },
}
