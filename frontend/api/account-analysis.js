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
      'get',
      `${moduleName}/account_analysis_summary_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },
}
