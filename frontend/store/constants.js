export const action = {
  LOGOUT: 'LOGOUT',
  GET_PROJECTS: 'GET_PROJECTS',
  GET_WORKSPACES: 'GET_WORKSPACES',
  GET_USER_INFORMATION: 'GET_USER_INFORMATION',
  GET_COUNTRIES: 'GET_COUNTRIES',
  GET_LANGUAGES: 'GET_LANGUAGES',
  CREATE_WORKSPACE: 'CREATE_WORKSPACE',
  CREATE_PROJECT: 'CREATE_PROJECT',
  CLEAR_KEYWORDS_LIST: 'CLEAR_KEYWORDS_LIST',
  CLEAR_STATE: 'CLEAR_STATE',
  UPDATE_NEW_WORKSPACE: 'UPDATE_NEW_WORKSPACE',
  UPDATE_OLD_WORKSPACE: 'UPDATE_OLD_WORKSPACE',
  UPDATE_PROJECT_STATE: 'UPDATE_PROJECT_STATE',
  UPDATE_WORKSPACES_STATE: 'UPDATE_WORKSPACES_STATE',
  UPDATE_KEYWORDS_LIST: 'UPDATE_KEYWORDS_LIST',
  UPDATE_CURRENT_STEP: 'UPDATE_CURRENT_STEP',
  UPDATE_ADDITIONAL_FILTERS: 'UPDATE_ADDITIONAL_FILTERS',
  POST_SEARCH: 'POST_SEARCH',
}

export const mutator = {
  SET_LOADING: 'SET_LOADING',
  SET_PROJECT: 'SET_PROJECT',
  SET_PROJECTS: 'SET_PROJECTS',
  SET_WORKSPACES: 'SET_WORKSPACES',
  SET_USER_INFORMATION: 'GET_USER_INFORMATION',
  SET_NEW_WORKSPACE: 'SET_NEW_WORKSPACE',
  SET_NEW_PROJECT: 'SET_NEW_PROJECT',
  SET_KEYWORDS_LIST: 'SET_KEYWORDS_LIST',
  SET_SEARCH_DATA: 'SET_SEARCH_DATA',
  SET_CURRENT_STEP: 'SET_CURRENT_STEP',
  SET_COUNTRIES: 'SET_COUNTRIES',
  SET_LANGUAGES: 'SET_LANGUAGES',
  SET_ADDITIONAL_FILTERS: 'SET_ADDITIONAL_FILTERS',
  RESET_STATE: 'RESET_STATE',
  DELETE_KEYWORDS_LIST: 'DELETE_KEYWORDS_LIST',
}

export const get = {
  LOADING: 'LOADING',
  PROJECT: 'PROJECT',
  PROJECTS: 'PROJECTS',
  WORKSPACES: 'WORKSPACES',
  USER_INFO: 'USER_INFO',
  NEW_PROJECT: 'NEW_PROJECT',
  KEYWORDS: 'KEYWORDS',
  SEARCH_DATA: 'SEARCH_DATA',
  COUNTRIES: 'COUNTRIES',
  LANGUAGES: 'LANGUAGES',
  ADDITIONAL_FILTERS: 'ADDITIONAL_FILTERS',
}
