import {fetch} from './api'

const moduleName = '/comparison'

export default {
  async getProjects() {
    return fetch('get', `${moduleName}/projects_list`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/`, workspace)
  },

  async updateWorkspace({workspaceId, workspace}) {
    return fetch('put', `${moduleName}/workspaces/${workspaceId}/`, workspace)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `${moduleName}/workspaces/${workspaceId}/`)
  },

  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },
}
