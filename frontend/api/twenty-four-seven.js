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
    return fetch('delete', `${moduleName}/projects/${projectId}/`)
  },

  async getItems(projectId, status, page) {
    return fetch(
      'get',
      `${moduleName}/projects/${projectId}/items/?page=${page}&page_size=20&status=${encodeURIComponent(
        status
      )}`
    )
  },

  async getRelatedContent(itemId) {
    return fetch('get', `${moduleName}/related_content/?item=${itemId}`)
  },

  async updateItem(projectId, itemId, value) {
    return fetch(
      'patch',
      `${moduleName}/projects/${projectId}/items/${itemId}/`,
      value
    )
  },
}
