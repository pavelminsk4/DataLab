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

  async getItems(projectId, status, page, order) {
    return fetch(
      'get',
      `${moduleName}/projects/${projectId}/items/?page=${page}&page_size=20&status=${encodeURIComponent(
        status
      )}&order=${order}`
    )
  },

  async getRelatedContent(itemId) {
    return fetch('get', `${moduleName}/related_content/?item=${itemId}`)
  },

  async updatePostDetails(projectId, postId, value) {
    return fetch(
      'patch',
      `${moduleName}/projects/${projectId}/items/${postId}/`,
      value
    )
  },

  async sendMessageToWhatsapp(phoneNumber, message) {
    return fetch('post', `${moduleName}/whatsapp/`, {
      phone_number: phoneNumber,
      message_content: message,
    })
  },

  async translateLanguage(newLanguage, value) {
    return fetch('post', `${moduleName}/translator/`, {
      target_lang: newLanguage,
      text: value,
    })
  },

  async createAISummary(postId) {
    return fetch('get', `${moduleName}/summary/${postId}/`)
  },
}
