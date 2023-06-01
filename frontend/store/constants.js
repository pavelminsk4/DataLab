export const action = {
  LOGOUT: 'LOGOUT',
  GET_PROJECTS: 'GET_PROJECTS',
  GET_WORKSPACES: 'GET_WORKSPACES',
  GET_USER_INFORMATION: 'GET_USER_INFORMATION',
  GET_COUNTRIES: 'GET_COUNTRIES',
  GET_LANGUAGES: 'GET_LANGUAGES',
  GET_SOURCES: 'GET_SOURCES',
  GET_AUTHORS: 'GET_AUTHORS',
  CHANGE_POST_SENTIMENT: 'CHANGE_POST_SENTIMENT',
  GET_SUMMARY_WIDGET: 'GET_SUMMARY_WIDGET',
  GET_VOLUME_WIDGET: 'GET_VOLUME_WIDGET',
  GET_AVAILABLE_WIDGETS: 'GET_AVAILABLE_WIDGETS',
  GET_CLIPPING_FEED_CONTENT_WIDGET: 'GET_CLIPPING_FEED_CONTENT_WIDGET',
  GET_TOP_AUTHORS_WIDGET: 'GET_TOP_AUTHORS_WIDGET',
  GET_TOP_BRANDS_WIDGET: 'GET_TOP_BRANDS_WIDGET',
  GET_TOP_COUNTRIES_WIDGET: 'GET_TOP_COUNTRIES_WIDGET',
  GET_TOP_LANGUAGES_WIDGET: 'GET_TOP_LANGUAGES_WIDGET',
  GET_SENTIMENT_TOP_SOURCES: 'GET_SENTIMENT_TOP_SOURCES',
  GET_SENTIMENT_TOP_COUNTRIES: 'GET_SENTIMENT_TOP_COUNTRIES',
  GET_SENTIMENT_TOP_LANGUAGES: 'GET_SENTIMENT_TOP_LANGUAGES',
  GET_SENTIMENT_TOP_AUTHORS: 'GET_SENTIMENT_TOP_AUTHORS',
  GET_SENTIMENT_FOR_PERIOD: 'GET_SENTIMENT_FOR_PERIOD',
  GET_CONTENT_VOLUME_TOP_SOURCES: 'GET_CONTENT_VOLUME_TOP_SOURCES',
  GET_CONTENT_VOLUME_TOP_COUNTRIES: 'GET_CONTENT_VOLUME_TOP_COUNTRIES',
  GET_CONTENT_VOLUME_TOP_AUTHORS: 'GET_CONTENT_VOLUME_TOP_AUTHORS',
  GET_SENTIMENT_TOP_KEYWORDS_WIDGET: 'GET_SENTIMENT_TOP_KEYWORDS_WIDGET',
  GET_SOURCES_BY_LANGUAGE: 'GET_SOURCES_BY_LANGUAGE',
  GET_SOURCES_BY_COUNTRY: 'GET_SOURCES_BY_COUNTRY',
  GET_OVERALL_TOP_SOURCES: 'GET_OVERALL_TOP_SOURCES',
  GET_DIMENSIONS: 'GET_DIMENSIONS',
  GET_SELECTED_DIMENSIONS: 'GET_SELECTED_DIMENSIONS',
  GET_TEMPLATES: 'GET_TEMPLATES',
  GET_DIMENSION_AUTHORS: 'GET_DIMENSION_AUTHORS',
  GET_DIMENSION_LANGUAGES: 'GET_DIMENSION_LANGUAGES',
  GET_DIMENSION_COUNTRIES: 'GET_DIMENSION_COUNTRIES',
  GET_DIMENSION_SOURCES: 'GET_DIMENSION_SOURCES',
  GET_DIMENSIONS_OPTIONS: 'GET_DIMENSIONS_OPTIONS',
  GET_COMPANY_USERS: 'GET_COMPANY_USERS',
  CREATE_WORKSPACE: 'CREATE_WORKSPACE',
  CREATE_PROJECT: 'CREATE_PROJECT',
  CLEAR_KEYWORDS_LIST: 'CLEAR_KEYWORDS_LIST',
  CLEAR_STATE: 'CLEAR_STATE',
  CLEAR_SEARCH_LIST: 'CLEAR_SEARCH_LIST',
  CLEAR_INTERACTIVE_DATA: 'CLEAR_INTERACTIVE_DATA',
  GET_TOP_KEYWORDS_WIDGET: 'GET_TOP_KEYWORDS_WIDGET',
  GET_SENTIMENT_DIAGRAM: 'GET_SENTIMENT_DIAGRAM',
  GET_SENTIMENT_NUMBER_OF_RESULT: 'GET_SENTIMENT_NUMBER_OF_RESULT',
  GET_AUTHORS_BY_COUNTRY: 'GET_AUTHORS_BY_COUNTRY',
  CREATE_CLIPPING_FEED_CONTENT_WIDGET: 'CREATE_CLIPPING_FEED_CONTENT_WIDGET',
  CREATE_NEW_USER: 'CREATE_NEW_USER',
  UPDATE_NEW_WORKSPACE: 'UPDATE_NEW_WORKSPACE',
  UPDATE_PROJECT: 'UPDATE_PROJECT',
  UPDATE_WORKSPACE: 'UPDATE_WORKSPACE',
  UPDATE_PROJECT_STATE: 'UPDATE_PROJECT_STATE',
  UPDATE_KEYWORDS_LIST: 'UPDATE_KEYWORDS_LIST',
  UPDATE_CURRENT_STEP: 'UPDATE_CURRENT_STEP',
  UPDATE_ADDITIONAL_FILTERS: 'UPDATE_ADDITIONAL_FILTERS',
  UPDATE_AVAILABLE_WIDGETS: 'UPDATE_AVAILABLE_WIDGETS',
  UPDATE_USER_DATA: 'UPDATE_USER_DATA',
  REFRESH_DISPLAY_CALENDAR: 'REFRESH_DISPLAY_CALENDAR',
  POST_SEARCH: 'POST_SEARCH',
  POST_DIMENSIONS_FOR_WIDGET: 'POST_DIMENSIONS_FOR_WIDGET',
  POST_INTERACTIVE_WIDGETS: 'POST_INTERACTIVE_WIDGETS',
  PUT_USER_DEPARTMENT: 'PUT_USER_DEPARTMENT',
  SHOW_INTERACTIVE_DATA_MODAL: 'SHOW_INTERACTIVE_DATA_MODAL',
  DELETE_CLIPPING_FEED_CONTENT: 'DELETE_CLIPPING_FEED_CONTENT',
  DELETE_USER_FROM_COMPANY: 'DELETE_USER_FROM_COMPANY',
  DELETE_WORKSPACE: 'DELETE_WORKSPACE',
  DELETE_PROJECT: 'DELETE_PROJECT',

  // social
  GET_CONTENT_VOLUME_WIDGET: 'GET_CONTENT_VOLUME_WIDGET',
  GET_TOP_LOCATIONS_WIDGET: 'GET_TOP_LOCATIONS_WIDGET',
  GET_CONTENT_VOLUME_TOP_LOCATIONS: 'GET_CONTENT_VOLUME_TOP_LOCATIONS',
  GET_CONTENT_VOLUME_TOP_LANGUAGES: 'GET_CONTENT_VOLUME_TOP_LANGUAGES',
  GET_SENTIMENT_TOP_LOCATIONS: 'GET_SENTIMENT_TOP_LOCATIONS',
  GET_GENDER_VOLUME_WIDGET: 'GET_GENDER_VOLUME_WIDGET',
  GET_SENTIMENT_TOP_KEYWORDS: 'GET_SENTIMENT_TOP_KEYWORDS',
  GET_SENTIMENT_BY_GENDER: 'GET_SENTIMENT_BY_GENDER',
  GET_TOP_SHARING_SOURCES: 'GET_TOP_SHARING_SOURCES',
  GET_OVERALL_TOP_AUTHORS: 'GET_OVERALL_TOP_AUTHORS',
  GET_TOP_AUTHORS_BY_GENDER: 'GET_TOP_AUTHORS_BY_GENDER',
  GET_AUTHORS_BY_LANGUAGE: 'GET_AUTHORS_BY_LANGUAGE',
  GET_AUTHORS_BY_LOCATION: 'GET_AUTHORS_BY_LOCATION',
  GET_AUTHORS_BY_SENTIMENT: 'GET_AUTHORS_BY_SENTIMENT',
  GET_AUTHORS_BY_GENDER: 'GET_AUTHORS_BY_GENDER',
  GET_SOCIAL_DIMENSIONS_OPTIONS: 'GET_SOCIAL_DIMENSIONS_OPTIONS',

  // Reports
  UPDATE_NEW_REPORT: 'UPDATE_NEW_REPORT',
  CLEAR_NEW_REPORT: 'CLEAR_NEW_REPORT',

  GET_REGULAR_REPORTS: 'GET_REGULAR_REPORTS',
  CREATE_REGULAR_REPORT: 'CREATE_REGULAR_REPORT',
  UPDATE_REGULAR_REPORT: 'UPDATE_REGULAR_REPORT',
  DELETE_REGULAR_REPORT: 'DELETE_REGULAR_REPORT',
  GET_REPORT_WIDGETS_LIST: 'GET_REPORT_WIDGETS_LIST',

  GET_INSTANTLY_REPORT: 'GET_INSTANTLY_REPORT',

  GET_WIDGETS_LISTS: 'GET_WIDGETS_LISTS',

  // Alerts

  UPDATE_NEW_ALERT: 'UPDATE_NEW_ALERT',
  CLEAR_NEW_ALERT: 'CLEAR_NEW_ALERT',

  GET_ALERTS: 'GET_ALERTS',
  CREATE_NEW_ALERT: 'CREATE_NEW_ALERT',
  UPDATE_ALERT: 'UPDATE_ALERT',

  DELETE_ALERT: 'DELETE_ALERT',

  // Account Analysis
  GET_LIST_OF_PROFILE_HANDLE: 'GET_LIST_OF_PROFILE_HANDLE',

  CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE:
    'CREATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE',
  CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT: 'CREATE_NEW_ACCOUNT_ANALYSIS_PROJECT',

  UPDATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE:
    'UPDATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE',
  UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT: 'UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT',

  DELETE_ACCOUNT_ANALYSIS_PROJECT: 'DELETE_ACCOUNT_ANALYSIS_PROJECT',

  GET_POSTS: 'GET_POSTS',
  CLEAR_WIDGETS_DATA: 'CLEAR_WIDGETS_DATA',

  GET_PROFILE_TIMELINE: 'GET_PROFILE_TIMELINE',
  GET_SUMMARY: 'GET_SUMMARY',
  GET_MOST_FREQUENT_POST_TYPES: 'GET_MOST_FREQUENT_POST_TYPES',
  GET_MOST_FREQUENT_MEDIA_TYPES: 'GET_MOST_FREQUENT_MEDIA_TYPES',
  GET_MOST_ENGAGING_POST_TYPES: 'GET_MOST_ENGAGING_POST_TYPES',
  GET_MOST_ENGAGING_MEDIA_TYPES: 'GET_MOST_ENGAGING_MEDIA_TYPES',
  GET_FOLLOWER_GROWTH: 'GET_FOLLOWER_GROWTH',
  GET_OPTIMAL_POST_LENGTH: 'GET_OPTIMAL_POST_LENGTH',
  GET_TOP_HASHTAGS: 'GET_TOP_HASHTAGS',
  GET_OPTIMAL_NUMBER_OF_HASHTAGS: 'GET_OPTIMAL_NUMBER_OF_HASHTAGS',
  GET_AVERAGE_ENGAGEMENTS_BY_DAY: 'GET_AVERAGE_ENGAGEMENTS_BY_DAY',
  GET_OPTIMAL_POST_TIME: 'GET_OPTIMAL_POST_TIME',
  GET_TOP_POSTS_BY_ENGAGEMENTS: 'GET_TOP_POSTS_BY_ENGAGEMENTS',
  GET_BEST_TIMES_TO_POST: 'GET_BEST_TIMES_TO_POST',

  GET_MENTION_TIMELINE: 'GET_MENTION_TIMELINE',
  GET_AUDIENCE_MENTION_TIME: 'GET_AUDIENCE_MENTION_TIME',
  GET_MOST_FREQUENT_MENTION_MEDIA_TYPES:
    'GET_MOST_FREQUENT_MENTION_MEDIA_TYPES',

  // 24/7
  CREATE_TFS_WORKSPACE: 'CREATE_TFS_WORKSPACE',
  CREATE_TFS_PROJECT: 'CREATE_TFS_PROJECT',

  UPDATE_NEW_TFS_WORKSPACE: 'UPDATE_NEW_TFS_WORKSPACE',
  UPDATE_NEW_TFS_PROJECT: 'UPDATE_NEW_TFS_PROJECT',
  UPDATE_ITEM_STATUS: 'UPDATE_ITEM_STATUS',

  GET_TFS_ITEMS: 'GET_TFS_ITEMS',
}

export const mutator = {
  SET_LOADING: 'SET_LOADING',
  SET_LOADING_WIDGETS: 'SET_LOADING_WIDGETS',
  SET_PROJECT: 'SET_PROJECT',
  SET_PROJECTS: 'SET_PROJECTS',
  SET_WORKSPACES: 'SET_WORKSPACES',
  UPDATE_WORKSPACE: 'UPDATE_WORKSPACE',
  SET_USER_INFORMATION: 'GET_USER_INFORMATION',
  SET_NEW_WORKSPACE: 'SET_NEW_WORKSPACE',
  SET_NEW_PROJECT: 'SET_NEW_PROJECT',
  SET_KEYWORDS_LIST: 'SET_KEYWORDS_LIST',
  SET_SEARCH_DATA: 'SET_SEARCH_DATA',
  SET_CURRENT_STEP: 'SET_CURRENT_STEP',
  SET_COUNTRIES: 'SET_COUNTRIES',
  SET_LANGUAGES: 'SET_LANGUAGES',
  SET_SOURCES: 'SET_SOURCES',
  SET_AUTHORS: 'SET_AUTHORS',
  SET_DIMENSIONS: 'SET_DIMENSIONS',
  SET_ADDITIONAL_FILTERS: 'SET_ADDITIONAL_FILTERS',
  SET_SUMMARY_WIDGET: 'SET_SUMMARY_WIDGET',
  SET_VOLUME_WIDGET: 'SET_VOLUME_WIDGET',
  SET_CLIPPING_FEED_CONTENT_WIDGET: 'SET_CLIPPING_FEED_CONTENT_WIDGET',
  SET_TOP_AUTHORS_WIDGET: 'SET_TOP_AUTHORS_WIDGET',
  SET_TOP_BRANDS_WIDGET: 'SET_TOP_BRANDS_WIDGET',
  SET_TOP_COUNTRIES_WIDGET: 'SET_TOP_COUNTRIES_WIDGET',
  SET_TOP_LANGUAGES_WIDGET: 'SET_TOP_LANGUAGES_WIDGET',
  SET_SENTIMENT_TOP_SOURCES: 'SET_SENTIMENT_TOP_SOURCES',
  SET_SENTIMENT_TOP_COUNTRIES: 'SET_SENTIMENT_TOP_COUNTRIES',
  SET_SENTIMENT_TOP_AUTHORS: 'SET_SENTIMENT_TOP_AUTHORS',
  SET_SENTIMENT_TOP_LANGUAGES: 'SET_SENTIMENT_TOP_LANGUAGES',
  SET_SENTIMENT_FOR_PERIOD: 'SET_SENTIMENT_FOR_PERIOD',
  SET_CONTENT_VOLUME_TOP_SOURCES: 'SET_CONTENT_VOLUME_TOP_SOURCES',
  SET_CONTENT_VOLUME_TOP_AUTHORS: 'SET_CONTENT_VOLUME_TOP_AUTHORS',
  SET_CONTENT_VOLUME_TOP_COUNTRIES: 'SET_CONTENT_VOLUME_TOP_COUNTRIES',
  SET_SENTIMENT_TOP_KEYWORDS_WIDGET: 'SET_SENTIMENT_TOP_KEYWORDS_WIDGET',
  SET_TOP_KEYWORDS_WIDGET: 'SET_TOP_KEYWORDS_WIDGET',
  SET_SENTIMENT_DIAGRAM: 'SET_SENTIMENT_DIAGRAM',
  SET_SENTIMENT_NUMBER_OF_RESULT: 'SET_SENTIMENT_NUMBER_OF_RESULT',
  SET_AUTHORS_BY_COUNTRY: 'SET_AUTHORS_BY_COUNTRY',
  SET_SOURCES_BY_LANGUAGE: 'SET_SOURCES_BY_LANGUAGE',
  SET_SOURCES_BY_COUNTRY: 'SET_SOURCES_BY_COUNTRY',
  SET_OVERALL_TOP_SOURCES: 'SET_OVERALL_TOP_SOURCES',
  SET_DISPLAY_CALENDAR: 'SET_DISPLAY_CALENDAR',
  SET_AVAILABLE_WIDGETS: 'SET_AVAILABLE_WIDGETS',
  SET_TEMPLATES: 'SET_TEMPLATES',
  SET_NUMBER_OF_PAGES: 'SET_NUMBER_OF_PAGES',
  SET_NUMBER_OF_POSTS: 'SET_NUMBER_OF_POSTS',
  SET_DIMENSION_LANGUAGES: 'SET_DIMENSION_LANGUAGES',
  SET_DIMENSION_COUNTRIES: 'SET_DIMENSION_COUNTRIES',
  SET_DIMENSION_SOURCES: 'SET_DIMENSION_SOURCES',
  SET_DIMENSION_AUTHORS: 'SET_DIMENSION_AUTHORS',
  SET_NEW_PROJECT_ID: 'SET_NEW_PROJECT_ID',
  SET_NEW_WORKSPACE_ID: 'SET_NEW_WORKSPACE_ID',
  SET_REGULAR_REPORTS: 'SET_REGULAR_REPORTS',
  SET_ALERTS: 'SET_ALERTS',
  SET_COMPANY_USERS: 'SET_COMPANY_USERS',
  SET_INTERACTIVE_DATA: 'SET_INTERACTIVE_DATA',
  RESET_STATE: 'RESET_STATE',
  RESET_SEARCH_LIST: 'CLEAR_SEARCH_LIST',
  RESET_INTERACTIVE_DATA: 'RESET_INTERACTIVE_DATA',
  DELETE_KEYWORDS_LIST: 'DELETE_KEYWORDS_LIST',
  SET_SELECTED_DIMENSIONS: 'SET_SELECTED_DIMENSIONS',
  SET_INTERACTIVE_DATA_MODAL: 'SET_INTERACTIVE_DATA_MODAL',
  //social
  SET_CONTENT_VOLUME_WIDGET: 'SET_CONTENT_VOLUME_WIDGET',
  SET_TOP_LOCATIONS_WIDGET: 'SET_TOP_LOCATIONS_WIDGET',
  SET_CONTENT_VOLUME_TOP_LOCATIONS: 'SET_CONTENT_VOLUME_TOP_LOCATIONS',
  SET_CONTENT_VOLUME_TOP_LANGUAGES: 'SET_CONTENT_VOLUME_TOP_LANGUAGES',
  SET_SENTIMENT_TOP_LOCATIONS: 'SET_SENTIMENT_TOP_LOCATIONS',
  SET_GENDER_VOLUME_WIDGET: 'SET_GENDER_VOLUME_WIDGET',
  SET_SENTIMENT_TOP_KEYWORDS: 'SET_SENTIMENT_TOP_KEYWORDS',
  SET_SENTIMENT_BY_GENDER: 'SET_SENTIMENT_BY_GENDER',
  SET_TOP_SHARING_SOURCES: 'SET_TOP_SHARING_SOURCES',
  SET_OVERALL_TOP_AUTHORS: 'SET_OVERALL_TOP_AUTHORS',
  SET_TOP_AUTHORS_BY_GENDER: 'SET_TOP_AUTHORS_BY_GENDER',
  SET_AUTHORS_BY_LANGUAGE: 'SET_AUTHORS_BY_LANGUAGE',
  SET_AUTHORS_BY_LOCATION: 'SET_AUTHORS_BY_LOCATION',
  SET_AUTHORS_BY_SENTIMENT: 'SET_AUTHORS_BY_SENTIMENT',
  SET_AUTHORS_BY_GENDER: 'SET_AUTHORS_BY_GENDER',

  // Reports
  SET_NEW_REPORT: 'SET_NEW_REPORT',
  SET_REPORT_WIDGETS_LIST: 'SET_REPORT_WIDGETS_LIST',
  SET_WIDGETS_LISTS: 'SET_WIDGETS_LISTS',

  // Alerts
  SET_NEW_ALERT: 'SET_NEW_ALERT',

  // Account Analysis
  SET_LIST_OF_PROFILE_HANDLE: 'SET_LIST_OF_PROFILE_HANDLE',

  SET_NEW_ACCOUNT_ANALYSIS_WORKSPACE: 'SET_NEW_ACCOUNT_ANALYSIS_WORKSPACE',
  SET_NEW_ACCOUNT_ANALYSIS_PROJECT: 'SET_NEW_ACCOUNT_ANALYSIS_PROJECT',

  SET_ACCOUNT_ANALYSIS_WORKSPACE_ID: 'SET_ACCOUNT_ANALYSIS_WORKSPACE_ID',
  SET_ACCOUNT_ANALYSIS_PROJECT_ID: 'SET_ACCOUNT_ANALYSIS_PROJECT_ID',

  SET_POSTS: 'SET_POSTS',
  CLEAR_WIDGETS_DATA: 'CLEAR_WIDGETS_DATA',

  SET_PROFILE_TIMELINE: 'SET_PROFILE_TIMELINE',
  SET_SUMMARY: 'SET_SUMMARY',
  SET_MOST_FREQUENT_POST_TYPES: 'SET_MOST_FREQUENT_POST_TYPES',
  SET_MOST_FREQUENT_MEDIA_TYPES: 'SET_MOST_FREQUENT_MEDIA_TYPES',
  SET_MOST_ENGAGING_POST_TYPES: 'SET_MOST_ENGAGING_POST_TYPES',
  SET_MOST_ENGAGING_MEDIA_TYPES: 'SET_MOST_ENGAGING_MEDIA_TYPES',
  SET_FOLLOWER_GROWTH: 'SET_FOLLOWER_GROWTH',
  SET_OPTIMAL_POST_LENGTH: 'SET_OPTIMAL_POST_LENGTH',
  SET_TOP_HASHTAGS: 'SET_TOP_HASHTAGS',
  SET_OPTIMAL_NUMBER_OF_HASHTAGS: 'SET_OPTIMAL_NUMBER_OF_HASHTAGS',
  SET_AVERAGE_ENGAGEMENTS_BY_DAY: 'SET_AVERAGE_ENGAGEMENTS_BY_DAY',
  SET_OPTIMAL_POST_TIME: 'SET_OPTIMAL_POST_TIME',
  SET_TOP_POSTS_BY_ENGAGEMENTS: 'SET_TOP_POSTS_BY_ENGAGEMENTS',
  SET_BEST_TIMES_TO_POST: 'SET_BEST_TIMES_TO_POST',

  SET_MENTION_TIMELINE: 'SET_MENTION_TIMELINE',
  SET_AUDIENCE_MENTION_TIME: 'SET_AUDIENCE_MENTION_TIME',
  SET_MOST_FREQUENT_MENTION_MEDIA_TYPES:
    'SET_MOST_FREQUENT_MENTION_MEDIA_TYPES',

  // 24/7
  SET_NEW_TFS_WORKSPACE: 'SET_NEW_TFS_WORKSPACE',
  SET_NEW_TFS_PROJECT: 'SET_NEW_TFS_PROJECT',

  SET_TFS_WORKSPACE_ID: 'SET_TFS_WORKSPACE_ID',
  SET_TFS_PROJECT_ID: 'SET_TFS_PROJECT_ID',

  SET_TFS_ITEMS: 'SET_TFS_ITEMS',
}

export const get = {
  LOADING: 'LOADING',
  LOADING_WIDGETS: 'LOADING_WIDGETS',
  PROJECT: 'PROJECT',
  PROJECTS: 'PROJECTS',
  WORKSPACES: 'WORKSPACES',
  USER_INFO: 'USER_INFO',
  DEPARTMENT: 'DEPARTMENT',
  NEW_PROJECT: 'NEW_PROJECT',
  KEYWORDS: 'KEYWORDS',
  SEARCH_DATA: 'SEARCH_DATA',
  COUNTRIES: 'COUNTRIES',
  LANGUAGES: 'LANGUAGES',
  SOURCES: 'SOURCES',
  AUTHORS: 'AUTHORS',
  ADDITIONAL_FILTERS: 'ADDITIONAL_FILTERS',
  SUMMARY_WIDGET: 'SUMMARY_WIDGET',
  VOLUME_WIDGET: 'VOLUME_WIDGET',
  CLIPPING_FEED_CONTENT_WIDGET: 'CLIPPING_FEED_CONTENT_WIDGET',
  TOP_AUTHORS: 'TOP_AUTHORS',
  TOP_BRANDS: 'TOP_BRANDS',
  TOP_COUNTRIES: 'TOP_COUNTRIES',
  TOP_LANGUAGES: 'TOP_LANGUAGES',
  SOURCES_BY_LANGUAGE: 'SOURCES_BY_LANGUAGE',
  SOURCES_BY_COUNTRY: 'SOURCES_BY_COUNTRY',
  OVERALL_TOP_SOURCES: 'OVERALL_TOP_SOURCES',
  SENTIMENT_TOP_SOURCES: 'SENTIMENT_TOP_SOURCES',
  SENTIMENT_TOP_COUNTRIES: 'SENTIMENT_TOP_COUNTRIES',
  SENTIMENT_TOP_LANGUAGES: 'SENTIMENT_TOP_LANGUAGES',
  SENTIMENT_TOP_AUTHORS: 'SENTIMENT_TOP_AUTHORS',
  SENTIMENT_FOR_PERIOD: 'SENTIMENT_FOR_PERIOD',
  TOP_SHARING_SOURCES: 'TOP_SHARING_SOURCES',
  CONTENT_VOLUME_TOP_SOURCES: 'CONTENT_VOLUME_TOP_SOURCES',
  CONTENT_VOLUME_TOP_AUTHORS: 'CONTENT_VOLUME_TOP_AUTHORS',
  CONTENT_VOLUME_TOP_COUNTRIES: 'CONTENT_VOLUME_TOP_COUNTRIES',
  AUTHORS_BY_COUNTRY: 'AUTHORS_BY_COUNTRY',
  AVAILABLE_WIDGETS: 'AVAILABLE_WIDGETS',
  CURRENT_STEP: 'CURRENT_STEP',
  NEW_WORKSPACE: 'NEW_WORKSPACE',
  DIMENSIONS: 'DIMENSIONS',
  TEMPLATES: 'TEMPLATES',
  POSTS_NUMBER: 'POSTS_NUMBER',
  PAGES_NUMBER: 'PAGES_NUMBER',
  DIMENSION_AUTHORS: 'DIMENSION_AUTHORS',
  DIMENSION_LANGUAGES: 'DIMENSION_LANGUAGES',
  DIMENSION_COUNTRIES: 'DIMENSION_COUNTRIES',
  DIMENSION_SOURCES: 'DIMENSION_SOURCES',
  DIMENSIONS_LIST: 'DIMENSIONS_LIST',
  NEW_PROJECT_ID: 'NEW_PROJECT_ID',
  NEW_WORKSPACE_ID: 'NEW_WORKSPACE_ID',
  ALERTS: 'ALERTS',
  REGULAR_REPORTS: 'REGULAR_REPORTS',
  COMPANY_USERS: 'COMPANY_USERS',
  SELECTED_DIMENSIONS: 'SELECTED_DIMENSIONS',
  INTERACTIVE_DATA: 'INTERACTIVE_DATA',
  SENTIMENT_TOP_KEYWORDS_WIDGET: 'SENTIMENT_TOP_KEYWORDS_WIDGET',
  TOP_KEYWORDS_WIDGET: 'TOP_KEYWORDS_WIDGET',
  SENTIMENT_DIAGRAM: 'SENTIMENT_DIAGRAM',
  SENTIMENT_NUMBER_OF_RESULT: 'SENTIMENT_NUMBER_OF_RESULT',
  CLIPPING_WIDGETS_DETAILS: 'CLIPPING_WIDGETS_DETAILS',
  AUTHORS_BY_SENTIMENT: 'AUTHORS_BY_SENTIMENT',
  AUTHORS_BY_LANGUAGE: 'AUTHORS_BY_LANGUAGE',
  OVERALL_TOP_AUTHORS: 'OVERALL_TOP_AUTHORS',
  INTERACTIVE_DATA_MODAL: 'INTERACTIVE_DATA_MODAL',

  ALL_PROJECTS: 'ALL_PROJECTS',

  // social
  SOCIAL_WIDGETS: 'SOCIAL_WIDGETS',
  SOCIAL_DIMENSIONS_LIST: 'SOCIAL_DIMENSIONS_LIST',

  // Reports
  CREATE_REPORTS_STEP: 'CREATE_REPORTS_STEP',

  // Account Analysis
  LIST_OF_PROFILE_HANDLE: 'LIST_OF_PROFILE_HANDLE',
}
