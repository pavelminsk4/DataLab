import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  [mutator.SET_LOADING_WIDGETS](state, loadingWidgets) {
    state.loadingWidgets = {...state.loadingWidgets, ...loadingWidgets}
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

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIdex = state.workspaces.findIndex(
      (w) => w.id === workspace.id
    )
    state.workspaces[currentWorkspaceIdex] = workspace
  },

  [mutator.SET_KEYWORDS_LIST](state, keywords) {
    state.keywords = {...state.keywords, ...keywords}
  },

  [mutator.SET_SEARCH_DATA](state, data) {
    state.searchData = [...data]
    state.isSearchPerformed = true
  },

  [mutator.SET_NUMBER_OF_PAGES](state, number) {
    state.numberOfPages = number
  },

  [mutator.SET_NUMBER_OF_POSTS](state, number) {
    state.numberOfPosts = number
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

  [mutator.SET_TOP_COUNTRIES_WIDGET](state, countries) {
    state.topCountries = countries
  },

  [mutator.SET_TOP_BRANDS_WIDGET](state, brands) {
    state.topBrands = brands
  },

  [mutator.SET_TOP_LANGUAGES_WIDGET](state, languages) {
    state.topLanguages = languages
  },

  [mutator.SET_CONTENT_VOLUME_TOP_SOURCES](state, contentVolumeSources) {
    state.contentVolumeTopSources = contentVolumeSources
  },

  [mutator.SET_CONTENT_VOLUME_TOP_AUTHORS](state, contentVolumeAuthors) {
    state.contentVolumeTopAuthors = contentVolumeAuthors
  },

  [mutator.SET_CONTENT_VOLUME_TOP_COUNTRIES](state, contentVolumeCountries) {
    state.contentVolumeTopCountries = contentVolumeCountries
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

  [mutator.SET_CLIPPING_FEED_CONTENT_WIDGET](state, data) {
    state.clippingFeedContent = [...data]
  },

  [mutator.SET_TOP_AUTHORS_WIDGET](state, data) {
    state.topAuthors = [...data]
  },

  [mutator.SET_SENTIMENT_TOP_SOURCES](state, data) {
    state.sentimentTopSources = {...data}
  },

  [mutator.SET_SENTIMENT_TOP_COUNTRIES](state, data) {
    state.sentimentTopCountries = {...data}
  },

  [mutator.SET_SENTIMENT_TOP_LANGUAGES](state, data) {
    state.sentimentTopLanguages = {...data}
  },

  [mutator.SET_SENTIMENT_TOP_AUTHORS](state, data) {
    state.sentimentTopAuthors = {...data}
  },

  [mutator.SET_SENTIMENT_FOR_PERIOD](state, data) {
    state.sentimentForPeriod = [...data]
  },

  [mutator.SET_TOP_KEYWORDS_WIDGET](state, data) {
    state.topKeywordsWidget = data
  },

  [mutator.SET_SENTIMENT_DIAGRAM](state, data) {
    state.sentimentDiagram = data
  },

  [mutator.SET_SENTIMENT_NUMBER_OF_RESULT](state, data) {
    state.sentimentNumberOfResult = data
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = {...data}
  },

  [mutator.SET_DIMENSIONS](state, data) {
    state.dimensions = [...data]
  },

  [mutator.SET_TEMPLATES](state, data) {
    state.templates = [...data]
  },

  [mutator.SET_DIMENSION_AUTHORS](state, data) {
    state.dimensionAuthors = [...data]
  },

  [mutator.SET_DIMENSION_LANGUAGES](state, data) {
    state.dimensionLanguages = [...data]
  },

  [mutator.SET_DIMENSION_COUNTRIES](state, data) {
    state.dimensionCountries = [...data]
  },

  [mutator.SET_DIMENSION_SOURCES](state, data) {
    state.dimensionSources = [...data]
  },

  [mutator.SET_SELECTED_DIMENSIONS](state, data) {
    state.selectedDimensions = {...data}
  },

  [mutator.SET_ALERTS](state, data) {
    state.alerts = [...data]
  },

  [mutator.SET_REGULAR_REPORTS](state, data) {
    state.regularReports = [...data]
  },

  [mutator.RESET_STATE](state) {
    state.currentStep = 'Step1'
    state.keywords = []
    state.searchData = []
    state.isSearchPerformed = false
    state.additionalFilters = null
    state.numberOfPages = 0
    state.numberOfPosts = 0
    state.newWorkspace = {
      title: '',
      description: '',
      members: [],
      projects: [],
      department: null,
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
    state.alerts = []
    state.regularReports = []
  },

  [mutator.RESET_SEARCH_LIST](state) {
    state.searchData = []
    state.numberOfPosts = 0
    state.numberOfPages = null
  },

  [mutator.RESET_INTERACTIVE_DATA](state) {
    state.interactiveData = []
  },

  [mutator.SET_DISPLAY_CALENDAR](state, value) {
    state.isShowCalendarContents = value
  },

  [mutator.SET_NEW_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.SET_NEW_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_COMPANY_USERS](state, users) {
    state.companyUsers = users
  },

  [mutator.SET_INTERACTIVE_DATA](state, posts) {
    state.interactiveData = posts
  },
}
