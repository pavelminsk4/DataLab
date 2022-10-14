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

  [mutator.SET_USER_INFORMATION](state, userInfo) {
    state.userInfo = userInfo
  },

  [mutator.SET_NEW_PROJECT](state, newProject) {
    state.newProject = {...state.newProject, ...newProject}
  },

  [mutator.SET_NEW_WORKSPACE](state, workspaceInfo) {
    state.newWorkspace = {...state.newWorkspace, ...workspaceInfo}
  },

  [mutator.SET_KEYWORDS_LIST](state, keywords) {
    state.keywords = {...state.keywords, ...keywords}
  },

  [mutator.SET_SEARCH_DATA](state, data) {
    state.searchData = [...data]
  },

  [mutator.SET_CURRENT_STEP](state, step) {
    state.currentStep = step
  },

  [mutator.SET_COUNTRIES](state, countries) {
    state.countries = countries
  },

  [mutator.SET_LANGUAGES](state, languages) {
    state.languages = languages
  },

  [mutator.SET_SOURCES](state, sources) {
    state.sources = sources
  },

  [mutator.SET_AUTHORS](state, authors) {
    state.authors = authors
  },

  [mutator.DELETE_KEYWORDS_LIST](state, index) {
    state.keywords.splice(index, 1)
  },

  [mutator.SET_ADDITIONAL_FILTERS](state, data) {
    state.additionalFilters = {...state.additionalFilters, ...data}
  },

  [mutator.SET_SUMMARY_WIDGET](state, data) {
    state.summary = {...data}
  },

  [mutator.SET_VOLUME_WIDGET](state, data) {
    state.volume = {...data}
  },

  [mutator.RESET_STATE](state) {
    state.currentStep = 'Step1'
    state.keywords = []
    state.searchData = []
    state.additionalFilters = null
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

  [mutator.SET_DISPLAY_CALENDAR](state, value) {
    state.isShowCalendar = value
  },
}
