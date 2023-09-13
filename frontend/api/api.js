import $api from '../http'

import online from './online-api'
import social from './social-api'
import accountAnalysis from './account-analysis'
import twentyFourSeven from './twenty-four-seven'
import comparison from './comparison'

const endpoint = (resource) => `/api${resource}`

export const fetch = async (action, resource, payload = null) => {
  const response = await $api[action](endpoint(resource), payload)
  return response.data
}

export default {
  online,
  social,
  accountAnalysis,
  twentyFourSeven,
  comparison,

  async logout() {
    const response = await $api.get('/accounts/logout/')
    return response.data
  },

  async getProjects() {
    return fetch('get', '/projects/')
  },

  async getLoggedUser() {
    return fetch('get', '/logged_in_user')
  },

  async getCompanyUsers(companyId) {
    return fetch('get', `/company_users/${companyId}/`)
  },

  async postTranslationText(value) {
    return fetch('post', '/multilanguage/', value)
  },

  async postPlatformLanguage(userId, lang) {
    return fetch('patch', `/profiles/${userId}/`, {platform_language: lang})
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

  async getFilters() {
    return fetch('get', '/dimensions/')
  },

  async getTemplates() {
    return fetch('get', '/templates/')
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

  async postFiltersForWidget({projectId, widgetId, data}) {
    return fetch(
      'patch',
      `/widgets/dimensions_for_each_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  // Reports
  async getRegularReports() {
    return fetch('get', `/reports/regular_reports/`)
  },
  async createRegularReport(data) {
    return fetch('post', `/regularreports/`, data)
  },
  async updateRegularReport(regularReportId, data) {
    return fetch('patch', `/reports/regular_reports/${regularReportId}`, data)
  },
  async deleteRegularReport(regularReportId) {
    fetch('delete', `/reports/regular_reports/${regularReportId}/`)
  },
  async getReportWidgetsList() {
    return fetch('get', `/report_widgets_list`)
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
