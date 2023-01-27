export const action = {
  LOGOUT: 'LOGOUT',
  GET_PROJECTS: 'GET_PROJECTS',
  GET_WORKSPACES: 'GET_WORKSPACES',
  GET_USER_INFORMATION: 'GET_USER_INFORMATION',
  GET_COUNTRIES: 'GET_COUNTRIES',
  GET_LANGUAGES: 'GET_LANGUAGES',
  GET_SOURCES: 'GET_SOURCES',
  GET_AUTHORS: 'GET_AUTHORS',
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
  GET_DIMENSIONS: 'GET_DIMENSIONS',
  GET_TEMPLATES: 'GET_TEMPLATES',
  GET_SELECTED_DIMENSIONS: 'GET_SELECTED_DIMENSIONS',
  GET_DIMENSION_AUTHORS: 'GET_DIMENSION_AUTHORS',
  GET_DIMENSION_LANGUAGES: 'GET_DIMENSION_LANGUAGES',
  GET_DIMENSION_COUNTRIES: 'GET_DIMENSION_COUNTRIES',
  GET_ALERTS: 'GET_ALERTS',
  GET_REGULAR_REPORTS: 'GET_REGULAR_REPORTS',
  GET_COMPANY_USERS: 'GET_COMPANY_USERS',
  CREATE_WORKSPACE: 'CREATE_WORKSPACE',
  CREATE_PROJECT: 'CREATE_PROJECT',
  CLEAR_KEYWORDS_LIST: 'CLEAR_KEYWORDS_LIST',
  CLEAR_STATE: 'CLEAR_STATE',
  CLEAR_SEARCH_LIST: 'CLEAR_SEARCH_LIST',
  CREATE_CLIPPING_FEED_CONTENT_WIDGET: 'CREATE_CLIPPING_FEED_CONTENT_WIDGET',
  CREATE_NEW_USER: 'CREATE_NEW_USER',
  CREATE_NEW_ALERT: 'CREATE_NEW_ALERT',
  UPDATE_ALERT: 'UPDATE_ALERT',
  CREATE_NEW_REGULAR_REPORT: 'CREATE_NEW_REGULAR_REPORT',
  UPDATE_REGULAR_REPORT: 'UPDATE_REGULAR_REPORT',
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
  POST_DIMENSIONS: 'POST_DIMENSIONS',
  PUT_USER_DEPARTMENT: 'PUT_USER_DEPARTMENT',
  DELETE_CLIPPING_FEED_CONTENT: 'DELETE_CLIPPING_FEED_CONTENT',
  DELETE_USER_FROM_COMPANY: 'DELETE_USER_FROM_COMPANY',
  DELETE_WORKSPACE: 'DELETE_WORKSPACE',
  DELETE_PROJECT: 'DELETE_PROJECT',
  DELETE_ALERT: 'DELETE_ALERT',
  GET_INSTANTLY_REPORT: 'GET_INSTANTLY_REPORT',
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
  SET_DISPLAY_CALENDAR: 'SET_DISPLAY_CALENDAR',
  SET_AVAILABLE_WIDGETS: 'SET_AVAILABLE_WIDGETS',
  SET_TEMPLATES: 'SET_TEMPLATES',
  SET_NUMBER_OF_PAGES: 'SET_NUMBER_OF_PAGES',
  SET_NUMBER_OF_POSTS: 'SET_NUMBER_OF_POSTS',
  SET_SELECTED_DIMENSIONS: 'SET_SELECTED_DIMENSIONS',
  SET_DIMENSION_LANGUAGES: 'SET_DIMENSION_LANGUAGES',
  SET_DIMENSION_COUNTRIES: 'SET_DIMENSION_COUNTRIES',
  SET_DIMENSION_AUTHORS: 'SET_DIMENSION_AUTHORS',
  SET_NEW_PROJECT_ID: 'SET_NEW_PROJECT_ID',
  SET_NEW_WORKSPACE_ID: 'SET_NEW_WORKSPACE_ID',
  SET_ALERTS: 'SET_ALERTS',
  SET_REGULAR_REPORTS: 'SET_REGULAR_REPORTS',
  SET_COMPANY_USERS: 'SET_COMPANY_USERS',
  RESET_STATE: 'RESET_STATE',
  RESET_SEARCH_LIST: 'CLEAR_SEARCH_LIST',
  DELETE_KEYWORDS_LIST: 'DELETE_KEYWORDS_LIST',
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
  SENTIMENT_TOP_SOURCES: 'SENTIMENT_TOP_SOURCES',
  SENTIMENT_TOP_COUNTRIES: 'SENTIMENT_TOP_COUNTRIES',
  SENTIMENT_TOP_LANGUAGES: 'SENTIMENT_TOP_LANGUAGES',
  SENTIMENT_TOP_AUTHORS: 'SENTIMENT_TOP_AUTHORS',
  SENTIMENT_FOR_PERIOD: 'SENTIMENT_FOR_PERIOD',
  CONTENT_VOLUME_TOP_SOURCES: 'CONTENT_VOLUME_TOP_SOURCES',
  CONTENT_VOLUME_TOP_AUTHORS: 'CONTENT_VOLUME_TOP_AUTHORS',
  CONTENT_VOLUME_TOP_COUNTRIES: 'CONTENT_VOLUME_TOP_COUNTRIES',
  AVAILABLE_WIDGETS: 'AVAILABLE_WIDGETS',
  CURRENT_STEP: 'CURRENT_STEP',
  NEW_WORKSPACE: 'NEW_WORKSPACE',
  DIMENSIONS: 'DIMENSIONS',
  TEMPLATES: 'TEMPLATES',
  POSTS_NUMBER: 'POSTS_NUMBER',
  PAGES_NUMBER: 'POSTS_NUMBER',
  SELECTED_DIMENSIONS: 'SELECTED_DIMENSIONS',
  DIMENSION_AUTHORS: 'DIMENSION_AUTHORS',
  DIMENSION_LANGUAGES: 'DIMENSION_LANGUAGES',
  DIMENSION_COUNTRIES: 'DIMENSION_COUNTRIES',
  NEW_PROJECT_ID: 'NEW_PROJECT_ID',
  NEW_WORKSPACE_ID: 'NEW_WORKSPACE_ID',
  ALERTS: 'ALERTS',
  REGULAR_REPORTS: 'REGULAR_REPORTS',
  COMPANY_USERS: 'COMPANY_USERS',
}
