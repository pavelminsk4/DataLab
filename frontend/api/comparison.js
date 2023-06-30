import {fetch} from './api'

const moduleName = '/comparison'

export default {
  async getProjects() {
    return fetch('get', `${moduleName}/projects_list`)
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

  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async updateWorkspacesProjects({workspaceId, data}) {
    return fetch(
      'post',
      `${moduleName}/workspaces/${workspaceId}/projects/`,
      data
    )
  },

  async deleteWorkspaceProject(workspaceId, projectId) {
    return fetch(
      'delete',
      `${moduleName}/workspaces/${workspaceId}/projects/${projectId}/`
    )
  },

  async getSummaryWidgets(projectId) {
    return fetch('get', `${moduleName}/projects/${projectId}/summary`)
  },
}
