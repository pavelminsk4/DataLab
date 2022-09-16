import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_PROJECTS](state, projects) {
    state.projects = projects
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces
  },

  [mutator.SET_USER_INFORMATION](state, userId) {
    state.userId = userId
  },

  [mutator.SET_NEW_PROJECT](state, newProject) {
    state.newProject = {...state.newProject, ...newProject}
  },

  [mutator.SET_NEW_WORKSPACE](state, workspaceInfo) {
    state.newWorkspace = {...state.newWorkspace, ...workspaceInfo}
  },

  [mutator.SET_KEYWORDS_LIST](state, keywords) {
    state.keywords = [...state.keywords, ...keywords]
  },

  [mutator.DELETE_KEYWORDS_LIST](state, index) {
    state.keywords.splice(index, 1)
  },

  [mutator.SET_SEARCH_DATA](state, data) {
    state.searchData = [...data]
  },

  [mutator.SET_CURRENT_STEP](state, step) {
    state.currentStep = step
  },

  [mutator.RESET_STATE](state) {
    state.currentStep = 'Step1'
    state.keywords = []
    state.searchData = []
    state.newWorkspace = {
      title: '',
      description: '',
      members: [],
      company: null,
      projects: [],
    }
    state.newProject = {
      title: '',
      note: '',
      keywords: [],
      ignore_keywords: '',
      max_items: '',
      image: null,
      arabic_name: '',
      english_name: '',
      social: false,
      online: false,
      premium: false,
      creator: null,
      source: '',
      workspace: null,
    }
  },
}
