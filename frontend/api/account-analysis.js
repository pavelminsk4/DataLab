import {fetch} from './api'

const moduleName = '/account_analysis'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },

  async getListOfProfilesHandle() {
    return fetch('get', `${moduleName}/list_of_profile_handle`)
  },

  async createWorkspace(workspace) {
    return fetch('post', `${moduleName}/workspaces/create/`, workspace)
  },

  async deleteWorkspace(workspaceId) {
    return fetch('delete', `${moduleName}/workspaces/delete/${workspaceId}/`)
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `${moduleName}/workspaces/update/${workspaceId}/`, data)
  },

  async createProject(project) {
    return fetch('post', `${moduleName}/projects/`, project)
  },

  async deleteAccountAnalysisProject(projectId) {
    return fetch('delete', `${moduleName}/projects/${projectId}/`)
  },

  async getAccountActivityPosts(projectId, value) {
    return fetch('post', `${moduleName}/search_posts/${projectId}`, value)
  },

  async getMentionsPosts(projectId, value) {
    return fetch(
      'post',
      `${moduleName}/search_posts_mentions/${projectId}`,
      value
    )
  },

  // Widgets
  async getAllWidgets(projectId) {
    return fetch(
      'get',
      `${moduleName}/account_analysis_projects/${projectId}/widgets_list`
    )
  },

  async updateAvailableWidgets({projectId, data}) {
    return fetch(
      'patch',
      `${moduleName}/account_analysis_projects/${projectId}/widgets_list/update`,
      data
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

  async getOptimalNumberOfHashtags(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/optimal_number_of_hashtags_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getTopHashtags(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/top_hashtags_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getAverageEngagemensByDay(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/average_engagements_by_day_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getOptimalPostTime(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/optimal_post_time_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getTopPostsByEngagements(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/top_posts_by_engagements_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getBestTimesToPost(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/best_times_to_post_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMentionTimeline(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/mention_timeline_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMostFrequentMentionMediaTypes(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/most_frequent_mention_media_types_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getAudienceMentionTime(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/audience_mention_time_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getTopMentionsByEngagements(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/top_mentions_by_engagements_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getAverageEngagemensByDayForMentions(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/average_engagements_by_day_for_mentions_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMentionSummary(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/mention_summary_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },

  async getMentionSentiment(projectId, widgetId, value) {
    return fetch(
      'post',
      `${moduleName}/mention_sentiment_widget/${projectId}/${widgetId}`,
      {aggregation_period: value}
    )
  },
}
