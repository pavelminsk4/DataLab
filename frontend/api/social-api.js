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
  async updateProject({projectId, data}) {
    return fetch('patch', `${moduleName}/projects/${projectId}/`, data)
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

  async downloadInstantlyReport(departmentId, projectId) {
    const response = fetch(
      'get',
      `${moduleName}/reports/${departmentId}/social_instantly_report/${projectId}/`,
      {
        responseType: 'blob',
      }
    )

    return URL.createObjectURL(response.data)
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
    return fetch(
      'post',
      `${moduleName}/social_interactive_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async postFiltersForWidget({projectId, widgetId, data}) {
    return fetch(
      'patch',
      `${moduleName}/dimensions_for_each_widgets/${projectId}/${widgetId}`,
      data
    )
  },

  async getFiltersAuthors(projectId) {
    return fetch('get', `${moduleName}/projects/${projectId}/dimension_authors`)
  },

  async getFiltersLanguages(projectId) {
    return fetch(
      'get',
      `${moduleName}/projects/${projectId}/dimension_languages`
    )
  },

  async getFiltersCountries(projectId) {
    return fetch(
      'get',
      `${moduleName}/projects/${projectId}/dimension_countries`
    )
  },

  //filters
  async getCountries(word) {
    return fetch('get', `${moduleName}/social_locations_list?search=${word}`)
  },
  async getLanguages(word) {
    return fetch('get', `${moduleName}/social_languages_list?search=${word}`)
  },
  async getAuthors(word) {
    return fetch('get', `${moduleName}/social_authors_list?search=${word}`)
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

  async getGenderVolumeWidget(projectId, widgetId, value) {
    return fetch(
      'put',
      `${moduleName}/social_gender_volume/${projectId}/${widgetId}`,
      value
    )
  },

  async getGenderByLocation(projectId, widgetId, value) {
    return fetch(
      'put',
      `${moduleName}/social_gender_by_location/${projectId}/${widgetId}`,
      value
    )
  },

  async getTopSharingSources({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_top_sharing_sources/${projectId}/${widgetId}`
    )
  },

  async getAuthorsByLocation({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_authors_by_location/${projectId}/${widgetId}`
    )
  },

  async getAuthorsBySentiment({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_authors_by_sentiment/${projectId}/${widgetId}`
    )
  },

  // Top
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

  async getTopKeywords({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_top_keywords/${projectId}/${widgetId}`
    )
  },

  async getTopKeywordsByCountry({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_keywords_by_location/${projectId}/${widgetId}`
    )
  },

  async getOverallTopAuthors({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_overall_top_authors/${projectId}/${widgetId}`
    )
  },
  async getTopAuthorsByGender({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_top_authors_by_gender/${projectId}/${widgetId}`
    )
  },
  async getAuthorsByGender({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_authors_by_gender/${projectId}/${widgetId}`
    )
  },
  async getLanguagesByLocation({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_languages_by_location/${projectId}/${widgetId}`
    )
  },

  // Content Volume
  async getContentVolumeTopLocations({projectId, value, widgetId}) {
    return fetch(
      'put',
      `${moduleName}/social_content_volume_top_locations/${projectId}/${widgetId}`,
      value
    )
  },
  async getContentVolumeTopAuthors({projectId, value, widgetId}) {
    return fetch(
      'post',
      `${moduleName}/social_content_volume_top_authors/${projectId}/${widgetId}`,
      value
    )
  },
  async getContentVolumeTopLanguages({projectId, value, widgetId}) {
    return fetch(
      'put',
      `${moduleName}/social_content_volume_top_languages/${projectId}/${widgetId}`,
      value
    )
  },
  async getAuthorsByLanguage({projectId, value, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_authors_by_language/${projectId}/${widgetId}`,
      value
    )
  },

  // Sentiment
  async getSentimentTopLocations(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_locations/${projectId}/${widgetId}`
    )
  },
  async getSentimentTopLanguages(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_languages/${projectId}/${widgetId}`
    )
  },
  async getSentimentTopAuthors(projectId, widgetId) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_authors/${projectId}/${widgetId}`
    )
  },
  async getSentimentForPeriod({projectId, value, widgetId}) {
    return fetch(
      'put',
      `${moduleName}/social_sentiment/${projectId}/${widgetId}`,
      value
    )
  },
  async getSentimentDiagram({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_diagram/${projectId}/${widgetId}`
    )
  },
  async getSentimentNumberOfResult({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_number_of_results/${projectId}/${widgetId}`
    )
  },
  async getSentimentTopKeywords({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_top_keywords/${projectId}/${widgetId}`
    )
  },
  async getSentimentByGender({projectId, widgetId}) {
    return fetch(
      'get',
      `${moduleName}/social_sentiment_by_gender/${projectId}/${widgetId}`
    )
  },
}
