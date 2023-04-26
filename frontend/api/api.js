import $api from '../http'

import social from './social-api'

const endpoint = (resource) => `/api${resource}`

export const fetch = async (action, resource, payload = null) => {
  const response = await $api[action](endpoint(resource), payload)
  return response.data
}

export default {
  social,

  async logout() {
    const response = await $api.get('/accounts/logout/')
    return response.data
  },

  async getProjects() {
    return fetch('get', '/projects/')
  },

  async getWorkspaces() {
    return fetch('get', '/workspaces/')
  },

  async getLoggedUser() {
    return fetch('get', '/logged_in_user')
  },

  async getCountries(word) {
    return fetch('get', `/countries/countries?search=${word}`)
  },

  async getLanguages(word) {
    return fetch('get', `/speeches/speeches?search=${word}`)
  },

  async getSources(word) {
    return fetch('post', '/sources', word)
  },

  async getAuthors(word) {
    return fetch('get', `/authors/authors?search=${word}`)
  },

  async getCompanyUsers(companyId) {
    return fetch('get', `/company_users/${companyId}/`)
  },

  async getListOfDisplayedWidgets(projectId) {
    return fetch('get', `/projects/${projectId}/widgets_list`)
  },

  async getSummaryWidget(projectId, widgetId) {
    return fetch('get', `/widgets/summary_widget/${projectId}/${widgetId}`)
  },

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/clipping_feed_content_widget/${projectId}/${widgetId}`
    )
  },

  async getVolumeWidget({projectId, value, widgetId}) {
    return fetch(
      'put',
      `/widgets/volume_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/top_10_authors_by_volume/${projectId}/${widgetId}`
    )
  },

  async getTopBrands(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/top_10_brands_widget/${projectId}/${widgetId}`
    )
  },

  async getTopCountries(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/top_10_countries_widget/${projectId}/${widgetId}`
    )
  },

  async getTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/top_10_languages_widget/${projectId}/${widgetId}`
    )
  },

  async getTopSharingSourcesWidget(projectId, widgetId) {
    return fetch('get', `/widgets/top_sharing_sources/${projectId}/${widgetId}`)
  },

  async getSentimentTopSources(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/sentiment_top_10_sources_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopCountries(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/sentiment_top_10_countries_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/sentiment_top_10_languages_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/sentiment_top_10_authors_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentForPeriod({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/sentiment_for_period_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Sources({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/content_volume_top_5_source_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Authors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/content_volume_top_5_authors_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Countries({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/content_volume_top_5_countries_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopKeywordsWidget({projectId, widgetId}) {
    return fetch('post', `/widgets/top_keywords/${projectId}/${widgetId}`)
  },

  async getAuthorsByCountry({projectId, widgetId}) {
    return fetch('post', `/widgets/authors_by_country/${projectId}/${widgetId}`)
  },

  async getSentimentDiagram({projectId, widgetId}) {
    return fetch('post', `/widgets/sentiment_diagram/${projectId}/${widgetId}`)
  },

  async getSentimentNumberOfResult({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/sentiment_number_of_results/${projectId}/${widgetId}`
    )
  },

  async getSourcesByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/sources_by_language/${projectId}/${widgetId}`
    )
  },

  async getSourcesByCountry({projectId, widgetId}) {
    return fetch('post', `/widgets/sources_by_country/${projectId}/${widgetId}`)
  },

  async getOverallTopSources({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/overall_top_sources/${projectId}/${widgetId}`
    )
  },

  async getOverallTopAuthors({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/overall_top_authors/${projectId}/${widgetId}`
    )
  },

  async getAuthorsBySentiment({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/authors_by_sentiment/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/authors_by_language/${projectId}/${widgetId}`
    )
  },

  async getDimensions() {
    return fetch('get', '/dimensions/')
  },

  async getTemplates() {
    return fetch('get', '/templates/')
  },

  async getDimensionAuthors(projectId) {
    return fetch('get', `/projects/${projectId}/list_authors`)
  },

  async getDimensionLanguages(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_languages`)
  },

  async getDimensionCountries(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_countries`)
  },

  async getDimensionSources(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_sources`)
  },

  async getSentimentTopKeywordsWidget({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/sentiment_top_keywords/${projectId}/${widgetId}`
    )
  },

  async createWorkspace(workspace) {
    return fetch('post', '/workspace/create/', workspace)
  },

  async createNewProject(newProject) {
    return fetch('post', '/projects/', newProject)
  },

  async createClippingFeedContent(data) {
    return fetch('post', '/clipping_feed_content_widget/create', data)
  },

  async createUser(data) {
    return fetch('post', '/register/', data)
  },

  async setUserDepartment({email, data}) {
    return fetch('patch', `/profileuser/${email}/`, data)
  },

  async updateUserData({userId, data}) {
    return fetch('put', `/user/update/${userId}/`, data)
  },

  async deleteUserFromCompany(userId) {
    return fetch('delete', `/user/delete/${userId}/`)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `/workspace/delete/${workspaceId}/`)
  },

  async deleteProject(projectId) {
    return fetch('delete', `/projects/${projectId}/`)
  },

  async postSearch(request) {
    return fetch('post', '/search', request)
  },

  async postDimensionsForWidget({projectId, widgetId, data}) {
    return fetch(
      'patch',
      `/widgets/dimensions_for_each_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async postInteractiveWidget({projectId, widgetId, data}) {
    return fetch(
      'post',
      `/widgets/interactive_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `/workspace/update/${workspaceId}/`, data)
  },

  async updateProject({projectId, data}) {
    return fetch('patch', `/projects/${projectId}/`, data)
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch('patch', `/projects/${projectId}/widgets_list/update`, data)
  },

  async deleteClippingFeedContentPost(projectId, postId) {
    return fetch(
      'delete',
      `/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`
    )
  },

  // Reports
  async getRegularReports(departmentId) {
    return fetch('get', `/reports/${departmentId}/regular_reports/`)
  },
  async createRegularReport(data) {
    return fetch('post', `/regularreports/`, data)
  },
  async updateRegularReport(departmentId, regularReportId, data) {
    return fetch(
      'patch',
      `/reports/${departmentId}/regular_reports/${regularReportId}`,
      data
    )
  },
  async deleteRegularReport(departmentId, regularReportId) {
    fetch(
      'delete',
      `/reports/${departmentId}/regular_reports/${regularReportId}/`
    )
  },
  async getReportWidgetsList() {
    return fetch('get', `/report_widgets_list`)
  },

  async downloadInstantlyReport(projectId) {
    const response = await $api.get(
      `/projects/${projectId}/reports/instantly_report`,
      {
        responseType: 'blob',
      }
    )
    return URL.createObjectURL(response.data)
  },

  // Alerts

  async createAlert(data) {
    return fetch('post', '/alerts/', data)
  },

  async getAlerts(departmentId) {
    return fetch('get', `/departments/${departmentId}/alerts`)
  },

  async updateAlert({data, alertId}) {
    return fetch('put', `/alerts/${alertId}/`, data)
  },

  async deleteAlert(alertId) {
    return fetch('delete', `/alerts/${alertId}/`)
  },
}
