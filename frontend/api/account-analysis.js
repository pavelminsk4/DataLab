import {fetch} from './api'

const moduleName = '/account_analysis'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async getListOfProfileHandle() {
    return fetch('get', `${moduleName}/list_of_profile_handle`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/create/`, workspace)
  },

  async createProject(project) {
    return fetch('post', `${moduleName}/projects/ `, project)
  },

  async deleteAccountAnalysisProject(projectId) {
    return fetch('delete', `${moduleName}/projects/${projectId}/ `)
  },

  // Widgets
  async getAllWidgets(projectId) {
    return fetch(
      'get',
      `${moduleName}/account_analysis_projects/${projectId}/widgets_list`
    )
  },

  async getProfileTimeline(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/profile_timeline_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getSummary(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/account_analysis_summary_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMostFrequentPostTypes(projectId, widgetId) {
    return fetch(
      'post',
      `${moduleName}/most_frequent_post_types_widget/${projectId}/${widgetId}`
    )
  },

  async getMostFrequentMediaTypes(projectId, widgetId) {
    return fetch(
      'post',
      `${moduleName}/most_frequent_media_types_widget/${projectId}/${widgetId}`
    )
  },

  async getMostEngagingPostTypes(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/most_engaging_post_types_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMostEngagingMediaTypes(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/most_engaging_media_types_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getFollowerGrowth(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/follower_growth_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getOptimalPostLength(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/optimal_post_length_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch(
      'patch',
      `${moduleName}/account_analysis_projects/${projectId}/widgets_list/update`,
      data
    )
  },
}
