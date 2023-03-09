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

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/social_clipping_feed_content/${projectId}/${widgetId}`
    )
  },
  async createClippingFeedContent(data) {
    // return fetch('post', '/clipping_feed_content_widget/create', data)
    return data
  },
  async deleteClippingFeedContentPost(projectId, postId) {
    // return fetch(
    //   'delete',
    //   `/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`
    // )
    return [projectId, postId]
  },
}
