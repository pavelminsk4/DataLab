export const action = {
  LOGOUT: 'LOGOUT',
  GET_PROJECTS: 'GET_PROJECTS',
  GET_WORKSPACES: 'GET_WORKSPACES',
  GET_USER_INFORMATION: 'GET_USER_INFORMATION',
  GET_COUNTRIES: 'GET_COUNTRIES',
  GET_LANGUAGES: 'GET_LANGUAGES',
  GET_SOURCES: 'GET_SOURCES',
  GET_AUTHORS: 'GET_AUTHORS',
  CHANGE_ONLINE_POST_SENTIMENT: 'CHANGE_ONLINE_POST_SENTIMENT',
  CHANGE_SOCIAL_POST_SENTIMENT: 'CHANGE_SOCIAL_POST_SENTIMENT',
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
  GET_LANGUAGES_BY_COUNTRY: 'GET_LANGUAGES_BY_COUNTRY',
  GET_CONTENT_VOLUME_TOP_SOURCES: 'GET_CONTENT_VOLUME_TOP_SOURCES',
  GET_CONTENT_VOLUME_TOP_COUNTRIES: 'GET_CONTENT_VOLUME_TOP_COUNTRIES',
  GET_CONTENT_VOLUME_TOP_AUTHORS: 'GET_CONTENT_VOLUME_TOP_AUTHORS',
  GET_SENTIMENT_TOP_KEYWORDS_WIDGET: 'GET_SENTIMENT_TOP_KEYWORDS_WIDGET',
  GET_SOURCES_BY_LANGUAGE: 'GET_SOURCES_BY_LANGUAGE',
  GET_SOURCES_BY_COUNTRY: 'GET_SOURCES_BY_COUNTRY',
  GET_OVERALL_TOP_SOURCES: 'GET_OVERALL_TOP_SOURCES',
  GET_FILTERS: 'GET_FILTERS',
  GET_SELECTED_FILTERS: 'GET_SELECTED_FILTERS',
  GET_TEMPLATES: 'GET_TEMPLATES',
  GET_FILTER_AUTHORS: 'GET_FILTER_AUTHORS',
  GET_FILTER_LANGUAGES: 'GET_FILTER_LANGUAGES',
  GET_FILTER_COUNTRIES: 'GET_FILTER_COUNTRIES',
  GET_FILTER_SOURCES: 'GET_FILTER_SOURCES',
  GET_FILTERS_OPTIONS: 'GET_FILTERS_OPTIONS',
  GET_COMPANY_USERS: 'GET_COMPANY_USERS',
  CREATE_WORKSPACE: 'CREATE_WORKSPACE',
  CREATE_PROJECT: 'CREATE_PROJECT',
  CLEAR_KEYWORDS_LIST: 'CLEAR_KEYWORDS_LIST',
  CLEAR_STATE: 'CLEAR_STATE',
  CLEAR_SEARCH_LIST: 'CLEAR_SEARCH_LIST',
  CLEAR_INTERACTIVE_DATA: 'CLEAR_INTERACTIVE_DATA',
  GET_TOP_KEYWORDS_WIDGET: 'GET_TOP_KEYWORDS_WIDGET',
  GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET: 'GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET',
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
  POST_FILTERS_FOR_WIDGET: 'POST_FILTERS_FOR_WIDGET',
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
  GET_SOCIAL_FILTERS_OPTIONS: 'GET_SOCIAL_FILTERS_OPTIONS',

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

  GET_ACCOUNT_ACTIVITY_POSTS: 'GET_ACCOUNT_ACTIVITY_POSTS',
  GET_MENTIONS_POSTS: 'GET_MENTIONS_POSTS',

  CLEAR_WIDGETS_DATA: 'CLEAR_WIDGETS_DATA',

  GET_PROFILE_TIMELINE: 'GET_PROFILE_TIMELINE',
  GET_SUMMARY: 'GET_SUMMARY',
  GET_MENTION_SENTIMENT: 'GET_MENTION_SENTIMENT',
  GET_MENTION_SUMMARY: 'GET_MENTION_SUMMARY',
  GET_MOST_FREQUENT_POST_TYPES: 'GET_MOST_FREQUENT_POST_TYPES',
  GET_MOST_FREQUENT_MEDIA_TYPES: 'GET_MOST_FREQUENT_MEDIA_TYPES',
  GET_MOST_ENGAGING_POST_TYPES: 'GET_MOST_ENGAGING_POST_TYPES',
  GET_MOST_ENGAGING_MEDIA_TYPES: 'GET_MOST_ENGAGING_MEDIA_TYPES',
  GET_FOLLOWER_GROWTH: 'GET_FOLLOWER_GROWTH',
  GET_OPTIMAL_POST_LENGTH: 'GET_OPTIMAL_POST_LENGTH',
  GET_TOP_HASHTAGS: 'GET_TOP_HASHTAGS',
  GET_OPTIMAL_NUMBER_OF_HASHTAGS: 'GET_OPTIMAL_NUMBER_OF_HASHTAGS',
  GET_AVERAGE_ENGAGEMENTS_BY_DAY: 'GET_AVERAGE_ENGAGEMENTS_BY_DAY',
  GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS:
    'GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS',
  GET_OPTIMAL_POST_TIME: 'GET_OPTIMAL_POST_TIME',
  GET_TOP_POSTS_BY_ENGAGEMENTS: 'GET_TOP_POSTS_BY_ENGAGEMENTS',
  GET_BEST_TIMES_TO_POST: 'GET_BEST_TIMES_TO_POST',

  GET_MENTION_TIMELINE: 'GET_MENTION_TIMELINE',
  GET_AUDIENCE_MENTION_TIME: 'GET_AUDIENCE_MENTION_TIME',
  GET_TOP_MENTIONS_BY_ENGAGEMENTS: 'GET_TOP_MENTIONS_BY_ENGAGEMENTS',
  GET_MOST_FREQUENT_MENTION_MEDIA_TYPES:
    'GET_MOST_FREQUENT_MENTION_MEDIA_TYPES',

  // 24/7
  CREATE_TFS_WORKSPACE: 'CREATE_TFS_WORKSPACE',
  CREATE_TFS_PROJECT: 'CREATE_TFS_PROJECT',
  CREATE_TFS_AI_SUMMARY: 'CREATE_TFS_AI_SUMMARY',

  UPDATE_NEW_TFS_WORKSPACE: 'UPDATE_NEW_TFS_WORKSPACE',
  UPDATE_NEW_TFS_PROJECT: 'UPDATE_NEW_TFS_PROJECT',
  UPDATE_TFS_ITEM_STATUS: 'UPDATE_TFS_ITEM_STATUS',
  UPDATE_TFS_ITEM_DATA: 'UPDATE_TFS_ITEM_DATA',
  UPDATE_TFS_ORIGINAL_CONTENT_LANGUAGE: 'UPDATE_TFS_ORIGINAL_CONTENT_LANGUAGE',
  UPDATE_AI_SUMMARY_LANGUAGE: 'UPDATE_AI_SUMMARY_LANGUAGE',

  GET_TFS_ITEMS: 'GET_TFS_ITEMS',
  GET_TFS_RELATED_CONTENT: 'GET_TFS_RELATED_CONTENT',

  SEND_TFS_MESSAGE_TO_WHATSAPP: 'SEND_TFS_MESSAGE_TO_WHATSAPP',

  CLEAR_TFS_ITEMS: 'CLEAR_TFS_ITEMS',
  CLEAR_TFS_TRANSLATED_TEXT: 'CLEAR_TFS_TRANSLATED_TEXT',
  CLEAR_TFS_WHATSAPP_MESSAGE: 'CLEAR_TFS_WHATSAPP_MESSAGE',
  CLEAR_TFS_RELATED_CONTENT: 'CLEAR_TFS_RELATED_CONTENT',
  CLEAR_TFS_AI_SUMMARY: 'CLEAR_TFS_AI_SUMMARY',
}
