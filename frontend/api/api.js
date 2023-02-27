import $api from '../http'

const endpoint = (resource) => `${resource}`

const fetch = async (action, resource, payload = null) => {
  const response = await $api[action](endpoint(resource), payload)
  return response.data
}

export default {
  async logout() {
    return fetch('get', '/accounts/logout/')
  },

  async getProjects() {
    return fetch('get', '/api/projects/')
  },

  async getWorkspaces() {
    return fetch('get', '/api/workspaces/')
  },

  async getLoggedUser() {
    return fetch('get', '/api/logged_in_user')
  },

  async getCountries(word) {
    return fetch('get', `/api/countries/countries?search=${word}`)
  },

  async getLanguages(word) {
    return fetch('get', `/api/speeches/speeches?search=${word}`)
  },

  async getSources(word) {
    return fetch('post', '/api/sources', word)
  },

  async getAuthors(word) {
    return fetch('get', `/api/authors/authors?search=${word}`)
  },

  async getCompanyUsers(companyId) {
    return fetch('get', `/api/company_users/${companyId}/`)
  },

  async getListOfDisplayedWidgets(projectId) {
    return fetch('get', `/api/projects/${projectId}/widgets_list`)
  },

  async getSummaryWidget(projectId, widgetId) {
    return fetch('get', `/api/widgets/summary_widget/${projectId}/${widgetId}`)
  },

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/clipping_feed_content_widget/${projectId}/${widgetId}`
    )
  },

  async getVolumeWidget({projectId, value, widgetId}) {
    return fetch(
      'put',
      `/api/widgets/volume_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/top_10_authors_by_volume/${projectId}/${widgetId}`
    )
  },

  async getTopBrands(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/top_10_brands_widget/${projectId}/${widgetId}`
    )
  },

  async getTopCountries(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/top_10_countries_widget/${projectId}/${widgetId}`
    )
  },

  async getTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/top_10_languages_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopSources(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/sentiment_top_10_sources_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopCountries(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/sentiment_top_10_countries_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/sentiment_top_10_languages_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/api/widgets/sentiment_top_10_authors_widget/${projectId}/${widgetId}`
    )
  },

  async getSentimentForPeriod({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/api/widgets/sentiment_for_period_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Sources({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/api/widgets/content_volume_top_5_source_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Authors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/api/widgets/content_volume_top_5_authors_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Countries({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/api/widgets/content_volume_top_5_countries_widget/${projectId}/${widgetId}`,
      value
    )
  },

  async getDimensions() {
    return fetch('get', '/api/dimensions/')
  },

  async getTemplates() {
    return fetch('get', '/api/templates/')
  },

  async getDimensionAuthors(projectId) {
    return fetch('get', `/api/projects/${projectId}/list_authors`)
  },

  async getDimensionLanguages(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_languages`)
  },

  async getDimensionCountries(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_countries`)
  },

  async getDimensionSources(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_sources`)
  },

  async getAlerts(projectId) {
    return fetch('get', `/api/projects/${projectId}/alerts`)
  },

  async getRegularReports(projectId) {
    return fetch('get', `/projects/${projectId}/reports/regular_reports/`)
  },

  async createWorkspace(workspace) {
    return fetch('post', '/api/workspace/create/', workspace)
  },

  async createNewProject(newProject) {
    return fetch('post', '/api/projects/', newProject)
  },

  async createClippingFeedContent(data) {
    return fetch('post', '/api/clipping_feed_content_widget/create', data)
  },

  async createAlert(data) {
    return fetch('post', '/api/alerts/', data)
  },

  async createUser(data) {
    return fetch('post', '/api/register/', data)
  },

  async setUserDepartment({email, data}) {
    return fetch('patch', `api/profileuser/${email}/`, data)
  },

  async updateAlert({data, alertId}) {
    return fetch('put', `/api/alerts/${alertId}/`, data)
  },

  async updateUserData({userId, data}) {
    return fetch('put', `/api/user/update/${userId}/`, data)
  },

  async deleteUserFromCompany(userId) {
    return fetch('delete', `/api/user/delete/${userId}/`)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `/api/workspace/delete/${workspaceId}/`)
  },

  async deleteProject(projectId) {
    return fetch('delete', `/api/projects/${projectId}/`)
  },

  async deleteAlert(alertId) {
    return fetch('delete', `/api/alerts/${alertId}/`)
  },

  async createRegularReport({projectId, data}) {
    return fetch(
      'post',
      `/projects/${projectId}/reports/regular_reports/`,
      data
    )
  },

  async updateRegularReport({projectId, regularReportId, data}) {
    return fetch(
      'patch',
      `/projects/${projectId}/reports/regular_reports/${regularReportId}/`,
      data
    )
  },

  async postSearch(request) {
    return fetch('post', '/api/search', request)
  },

  async postDimensionsForWidget({projectId, widgetId, data}) {
    return fetch(
      'patch',
      `/api/widgets/dimensions_for_each_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `/api/workspace/update/${workspaceId}/`, data)
  },

  async updateProject({projectId, data}) {
    return fetch('patch', `/api/projects/${projectId}/`, data)
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch(
      'patch',
      `/api/projects/${projectId}/widgets_list/update`,
      data
    )
  },

  async deleteClippingFeedContentPost(projectId, postId) {
    return fetch(
      'delete',
      `/api/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`
    )
  },

  async downloadInstantlyReport(projectId) {
    const response = await $api.get(
      endpoint(`/projects/${projectId}/reports/instantly_report`),
      {
        responseType: 'blob',
      }
    )
    return URL.createObjectURL(response.data)
  },
}
