import {fetch} from './api'

const moduleName = '/social'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/social_workspaces/`)
  },
  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/social_workspaces/create/`, workspace)
  },
  async updateWorkspace({workspaceId, data}) {
    return fetch(
      'put',
      `${moduleName}/social_workspaces/update/${workspaceId}/`,
      data
    )
  },
  async deleteWorkspace(workspaceId) {
    return fetch(
      'delete',
      `${moduleName}/social_workspaces/delete/${workspaceId}/`
    )
  },

  async getProjects() {
    return fetch('get', `${moduleName}/projects/`)
  },
  async createProject(project) {
    return fetch('post', `${moduleName}/projects/`, project)
  },

  async postSearch(request) {
    return fetch('post', `${moduleName}/twitter_post_search/`, request)
  },
}
