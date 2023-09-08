import $api from '../http'
import {fetch} from './api'

// const moduleName = '/online'

export default {
  async getWorkspaces() {
    return fetch('get', '/workspaces/')
  },

  async postSearch(request) {
    return fetch('post', '/search', request)
  },

  async createWorkspace(workspace) {
    return fetch('post', '/workspace/create/', workspace)
  },

  async createNewProject(newProject) {
    return fetch('post', '/projects/', newProject)
  },

  async getListOfDisplayedWidgets(projectId) {
    return fetch('get', `/projects/${projectId}/widgets_list`)
  },

  async postInteractiveWidget({projectId, widgetId, data}) {
    return fetch(
      'post',
      `/widgets/interactive_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch('patch', `/projects/${projectId}/widgets_list/update`, data)
  },

  async downloadInstantReport(projectId) {
    const response = await $api.get(
      `/api/reports/instantly_report/${projectId}/`,
      {
        responseType: 'blob',
      }
    )
    return URL.createObjectURL(response.data)
  },

  async createClippingFeedContent(data) {
    return fetch('post', '/clipping_feed_content_widget/create', data)
  },

  async deleteClippingFeedContentPost(projectId, postId) {
    return fetch(
      'delete',
      `/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`
    )
  },

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_clipping_feed_content/${projectId}/${widgetId}`
    )
  },

  // Widgets
  async getSummaryWidget(projectId, widgetId) {
    return fetch('get', `/widgets/onl_summary/${projectId}/${widgetId}`)
  },

  async getVolumeWidget({projectId, value, widgetId}) {
    return fetch('put', `/widgets/onl_volume/${projectId}/${widgetId}`, value)
  },
}
