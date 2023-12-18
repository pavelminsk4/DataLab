import $api from '../http'
import {fetch} from './api'

export default {
  async getWorkspaces() {
    return fetch('get', '/workspaces/')
  },

  async getWorkspace(workspaceId) {
    return fetch('get', `/workspace/${workspaceId}`)
  },

  async getProject(projectId) {
    return fetch('get', `/projects/${projectId}/`)
  },

  async postSearch(request) {
    return fetch('post', '/search', request)
  },
  async postsPreview(filters) {
    return fetch('get', `/project/preview?${filters}`)
  },

  async createWorkspace(workspace) {
    return fetch('post', '/workspace/create/', workspace)
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `/workspace/update/${workspaceId}/`, data)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `/workspace/delete/${workspaceId}/`)
  },

  async deleteProject(projectId) {
    return fetch('delete', `/projects/${projectId}/`)
  },

  async createNewProject(newProject) {
    return fetch('post', '/projects/', newProject)
  },

  async updateProject(data) {
    return fetch('patch', `/projects/${data.project_pk}/`, data)
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

  async updateStatusCollectingData(projectId, data) {
    return fetch('patch', `/project_statuses/${projectId}/`, data)
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

  async removePostFromProject({postId, projectId}) {
    return fetch('get', `/project/${projectId}/${postId}/delete`)
  },

  async getCountries(word, limit) {
    return fetch('get', `/countries/countries?limit=${limit}&search=${word}`)
  },

  async getLanguages(word, limit) {
    return fetch('get', `/speeches/speeches?limit=${limit}&search=${word}`)
  },

  async getSources(word, limit) {
    return fetch('get', `/sources/sources?limit=${limit}&search=${word}`)
  },

  async getAuthors(word, limit) {
    return fetch('get', `/authors/authors?limit=${limit}&search=${word}`)
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

  // Widgets
  async getSummaryWidget(projectId, widgetId) {
    return fetch('get', `/widgets/onl_summary/${projectId}/${widgetId}`)
  },

  async getVolumeWidget({projectId, value, widgetId}) {
    return fetch('put', `/widgets/onl_volume/${projectId}/${widgetId}`, value)
  },

  async getTopAuthors(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_authors/${projectId}/${widgetId}`)
  },

  async getTopBrands(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_sources/${projectId}/${widgetId}`)
  },

  async getTopCountries(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_countries/${projectId}/${widgetId}`)
  },

  async getTopLanguages(projectId, widgetId) {
    return fetch('get', `/widgets/onl_top_languages/${projectId}/${widgetId}`)
  },

  async getContentVolumeTopSources({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_sources/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTopAuthors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_authors/${projectId}/${widgetId}`,
      value
    )
  },

  async getContentVolumeTopCountries({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_content_volume_top_countries/${projectId}/${widgetId}`,
      value
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

  async getSentimentTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_authors/${projectId}/${widgetId}`
    )
  },

  async getSentimentTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_sentiment_top_languages/${projectId}/${widgetId}`
    )
  },

  async getSentimentForPeriod({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_for_period/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopKeywordsWidget({projectId, widgetId}) {
    return fetch('post', `/widgets/onl_top_keywords/${projectId}/${widgetId}`)
  },

  async getSentimentTopKeywordsWidget({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_top_keywords/${projectId}/${widgetId}`
    )
  },

  async getSentimentNumberOfResult({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_number_of_results/${projectId}/${widgetId}`
    )
  },

  async getSentimentDiagram({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sentiment_diagram/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByCountry({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_country/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_language/${projectId}/${widgetId}`
    )
  },

  async getAuthorsBySentiment({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_authors_by_sentiment/${projectId}/${widgetId}`
    )
  },

  async getOverallTopAuthors({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_overall_top_authors/${projectId}/${widgetId}`
    )
  },

  async getOverallTopSources({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_overall_top_sources/${projectId}/${widgetId}`
    )
  },

  async getSourcesByCountry({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sources_by_country/${projectId}/${widgetId}`
    )
  },

  async getSourcesByLanguage({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_sources_by_language/${projectId}/${widgetId}`
    )
  },

  async getTopSharingSourcesWidget(projectId, widgetId) {
    return fetch(
      'get',
      `/widgets/onl_top_sharing_sources/${projectId}/${widgetId}`
    )
  },

  async getTopKeywordsByCountryWidget({projectId, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_top_keywords_by_country/${projectId}/${widgetId}`
    )
  },

  async getLanguagesByCountry({projectId, value, widgetId}) {
    return fetch(
      'post',
      `/widgets/onl_languages_by_country/${projectId}/${widgetId}`,
      value
    )
  },
}
