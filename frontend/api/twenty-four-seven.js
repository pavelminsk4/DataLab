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

  async getItems(projectId, status) {
    if (status === 'Q&A Check') {
      return fetch(
        'get',
        `${moduleName}/projects/${projectId}/items/?page=1&&status=Q%26A%20Check`
      )
    }

    return fetch(
      'get',
      `${moduleName}/projects/${projectId}/items/?page=1&&status=${status}`
    )
  },

  async updateItemStatus(projectId, itemId, value) {
    return fetch(
      'patch',
      `${moduleName}/projects/${projectId}/items/${itemId}/`,
      value
    )
  },
}
