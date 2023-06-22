import $api from '../http'

import social from './social-api'
import accountAnalysis from './account-analysis'
import twentyFourSeven from './twenty-four-seven'

const endpoint = (resource) => `/api${resource}`

export const fetch = async (action, resource, payload = null) => {
  const response = await $api[action](endpoint(resource), payload)
  return response.data
}

export default {
  social,
  accountAnalysis,
  twentyFourSeven,

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
    return fetch('get', `/sources/sources?search=${word}`)
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

  async changeOnlinePostSentiment(postId, departmentId, newSentiment) {
    return fetch(
      'post',
      `/change_online_sentiment/${postId}/${departmentId}/${newSentiment}`
    )
  },

  async changeSocialPostSentiment(postId, departmentId, newSentiment) {
    return fetch(
      'post',
      `/social/change_social_sentiment/${postId}/${departmentId}/${newSentiment}`
    )
  },

  async getSummaryWidget(projectId, widgetId) {
    return fetch('get', `/widgets/onl_summary/${projectId}/${widgetId}`)
  },

  async getClippingFeedContentWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_clipping_feed_content/${projectId}/${widgetId}`
    )
  },

  async getVolumeWidget({projectId, value, widgetId}) {
    return fetch('put', `/widgets/onl_volume/${projectId}/${widgetId}`, value)
  },

  async getTopAuthors(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_authors/${projectId}/${widgetId}`)
  },

  async getTopBrands(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_brands/${projectId}/${widgetId}`)
  },

  async getTopCountries(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_countries/${projectId}/${widgetId}`)
  },

  async getTopLanguages(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_languages/${projectId}/${widgetId}`)
  },

  async getTopSharingSourcesWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_top_sharing_sources/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopSources(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_sources/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopCountries(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_countries/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_languages/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_authors/${projectId}/${widgetId}`
    )
  },

  async getSentimentForPeriod({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_for_period/${projectId}/${widgetId}`,
      value
    )
  },

  async getLanguagesByCountry({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_languages_by_country/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Sources({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_sources/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Authors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_authors/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTop10Countries({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_countries/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopKeywordsWidget({projectId, widgetId}) {
    return fetch('post', `/widgets/onl_top_keywords/${projectId}/${widgetId}`)
  },

  async getTopKeywordsByCountryWidget({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_top_keywords_by_country/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByCountry({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_country/${projectId}/${widgetId}`
    )
  },

  async getSentimentDiagram({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_diagram/${projectId}/${widgetId}`
    )
  },

  async getSentimentNumberOfResult({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_number_of_results/${projectId}/${widgetId}`
    )
  },

  async getSourcesByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sources_by_language/${projectId}/${widgetId}`
    )
  },

  async getSourcesByCountry({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sources_by_country/${projectId}/${widgetId}`
    )
  },

  async getOverallTopSources({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_overall_top_sources/${projectId}/${widgetId}`
    )
  },

  async getOverallTopAuthors({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_overall_top_authors/${projectId}/${widgetId}`
    )
  },

  async getAuthorsBySentiment({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_sentiment/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_language/${projectId}/${widgetId}`
    )
  },

  async getFilters() {
    return fetch('get', '/dimensions/')
  },

  async getTemplates() {
    return fetch('get', '/templates/')
  },

  async getFiltersAuthors(projectId) {
    return fetch('get', `/projects/${projectId}/list_authors`)
  },

  async getFiltersLanguages(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_languages`)
  },

  async getFiltersCountries(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_countries`)
  },

  async getFiltersSources(projectId) {
    return fetch('get', `/projects/${projectId}/dimension_sources`)
  },

  async getSentimentTopKeywordsWidget({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_top_keywords/${projectId}/${widgetId}`
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

  async postFiltersForWidget({projectId, widgetId, data}) {
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

  async downloadInstantlyReport(departmentId, projectId) {
    const response = await $api.get(
      `/api/reports/${departmentId}/instantly_report/${projectId}/`,
      {
        responseType: 'blob',
      }
    )
    return URL.createObjectURL(response.data)
  },

  async downloadSocialInstantlyReport(departmentId, projectId) {
    const response = await $api.get(
      `/reports/${departmentId}/social_instantly_report/${projectId}/`,
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
