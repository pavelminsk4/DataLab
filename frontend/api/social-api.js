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

  async createClippingFeedContent(data) {
    // return fetch('post', '${moduleName}/clipping_feed_content_widget/create', data)
    return data
  },
  async deleteClippingFeedContentPost(projectId, postId) {
    // return fetch(
    //   'delete',
    //   `${moduleName}/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`
    // )
    return [projectId, postId]
  },

  async getAllWidgets(projectId) {
    return fetch('get', `${moduleName}/projects/${projectId}/widgets_list`)
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch(
      'patch',
      `${moduleName}/projects/${projectId}/widgets_list/update`,
      data
    )
  },

  async postInteractiveWidget({projectId, widgetId, data}) {
    // return fetch(
    //   'post',
    //   `${moduleName}/widgets/interactive_widgets/${projectId}/${widgetId}`,
    //   data
    // )
    return {projectId, widgetId, data}
  },

  // Widgets
  async getSummaryWidget(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_summary_widget/${projectId}/${widgetId}`
    )
  },

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_clipping_feed_content/${projectId}/${widgetId}`
    )
  },

  async getContentVolumeWidget({projectId, value, widgetId}) {
    return fetch(
      'put',
      `${moduleName}/social_content_volume/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopLocationsWidget(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_top_locations/${projectId}/${widgetId}`
    )
  },
  async getTopLanguagesWidget(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_top_languages/${projectId}/${widgetId}`
    )
  },
  async getTopAuthorsWidget(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_top_authors/${projectId}/${widgetId}`
    )
  },

  // Content Volume
  async getContentVolumeTopLocations({projectId, value, widgetId}) {
    return fetch(
      'post',
      `${moduleName}/social_content_volume_by_top_locations/${projectId}/${widgetId}`,
      value
    )
  },
  async getContentVolumeTopAuthors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `${moduleName}/social_content_volume_by_top_authors/${projectId}/${widgetId}`,
      value
    )
  },
  async getContentVolumeTopLanguages({projectId, value, widgetId}) {
    return fetch(
      'post',
      `${moduleName}/social_content_volume_by_top_languages/${projectId}/${widgetId}`,
      value
    )
  },
}
