import {fetch} from './api'

const moduleName = '/twenty_four_seven'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/`, workspace)
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `${moduleName}/workspaces/${workspaceId}/`, data)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `${moduleName}/workspaces/${workspaceId}/`)
  },

  async createProject(project) {
    return fetch('post', `${moduleName}/projects/ `, project)
  },

  async deleteProject(projectId) {
    return fetch('delete', `${moduleName}/projects/${projectId}/ `)
  },
}
