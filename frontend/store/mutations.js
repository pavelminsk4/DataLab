import {mutator} from '@store/constants'
import initialState, {
  newReportInitialState,
} from '@store/constants/initialState'

export default {
  [mutator.SET_TRANSLATION](state, {text, translation}) {
    state.translation[text] = translation
  },

  [mutator.SET_PLATFORM_LANG](state, newLang) {
    state.platformLanguage = newLang
  },

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
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
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

  [mutator.SET_LANGUAGES_BY_COUNTRY](state, languages) {
    state.languagesByCountry = languages
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

  [mutator.SET_SUMMARY_WIDGET](state, {widgetId, data}) {
    state.summary = {id: widgetId, data}
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

  [mutator.SET_SENTIMENT_TOP_KEYWORDS_WIDGET](state, data) {
    state.sentimentTopKeywordsWidget = data
  },

  [mutator.SET_TOP_KEYWORDS_WIDGET](state, data) {
    state.topKeywordsWidget = data
  },

  [mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](state, data) {
    state.topKeywordsByCountryWidget = data
  },

  [mutator.SET_TOP_SHARING_SOURCES](state, data) {
    state.topSharingSources = data
  },

  [mutator.SET_SENTIMENT_DIAGRAM](state, data) {
    state.sentimentDiagram = data
  },

  [mutator.SET_SENTIMENT_NUMBER_OF_RESULT](state, data) {
    state.sentimentNumberOfResult = data
  },

  [mutator.SET_AUTHORS_BY_COUNTRY](state, data) {
    state.authorsByCountry = data
  },

  [mutator.SET_SOURCES_BY_LANGUAGE](state, data) {
    state.sourcesByLanguage = data
  },

  [mutator.SET_SOURCES_BY_COUNTRY](state, data) {
    state.sourcesByCountry = data
  },

  [mutator.SET_OVERALL_TOP_SOURCES](state, data) {
    state.overallTopSources = data
  },

  [mutator.SET_OVERALL_TOP_AUTHORS](state, data) {
    state.overallTopAuthors = data
  },

  [mutator.SET_AUTHORS_BY_LANGUAGE](state, data) {
    state.authorsByLanguage = data
  },

  [mutator.SET_AUTHORS_BY_SENTIMENT](state, data) {
    state.authorsBySentiment = data
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = {...data}
  },

  [mutator.SET_FILTERS](state, data) {
    state.dimensions = [...data]
  },

  [mutator.SET_TEMPLATES](state, data) {
    state.templates = data
  },

  [mutator.SET_FILTERS_AUTHORS](state, data) {
    state.dimensionAuthors = [...data]
  },

  [mutator.SET_FILTERS_LANGUAGES](state, data) {
    state.dimensionLanguages = [...data]
  },

  [mutator.SET_FILTERS_COUNTRIES](state, data) {
    state.dimensionCountries = [...data]
  },

  [mutator.SET_FILTERS_SOURCES](state, data) {
    state.dimensionSources = [...data]
  },

  [mutator.SET_SELECTED_FILTERS](state, data) {
    state.selectedFilters = {...data}
  },

  [mutator.RESET_STATE](state) {
    const {
      currentStep,
      keywords,
      searchData,
      isSearchPerformed,
      numberOfPages,
      numberOfPosts,
      newWorkspace,
      newProject,
      alerts,
      regularReports,
    } = initialState

    state.currentStep = currentStep
    state.keywords = keywords
    state.searchData = searchData
    state.isSearchPerformed = isSearchPerformed
    state.numberOfPages = numberOfPages
    state.numberOfPosts = numberOfPosts
    state.newWorkspace = newWorkspace
    state.newProject = newProject
    state.alerts = alerts
    state.regularReports = regularReports
  },

  [mutator.RESET_SEARCH_LIST](state) {
    state.searchData = []
    state.numberOfPosts = 0
    state.numberOfPages = null
  },

  [mutator.RESET_INTERACTIVE_DATA](state) {
    state.interactiveData = []
    state.inreractiveDataModal = {isShow: false}
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
  [mutator.SET_INTERACTIVE_DATA_MODAL](state, data) {
    state.inreractiveDataModal = {...state.inreractiveDataModal, ...data}
  },

  // Reports
  [mutator.SET_REGULAR_REPORTS](state, data) {
    state.regularReports = data
  },
  [mutator.SET_NEW_REPORT](state, data) {
    if (data) {
      state.newReport = {...state.newReport, ...data}
    } else {
      state.newReport = {...newReportInitialState}
    }
  },

  [mutator.SET_WIDGETS_LISTS](state, {id, projectList}) {
    for (const key in projectList) {
      if (typeof projectList[key] !== 'object') {
        delete projectList[key]
      }
    }

    state.reportWidgetsLists.set(id, projectList)
  },
  [mutator.SET_REPORT_WIDGETS_LIST](state, data) {
    const reportWidgetsLists = Object.values(data).map((widget) => ({
      ...widget,
      name: widget.name.toLowerCase().split(' ').join('_'),
    }))

    const onlineList = reportWidgetsLists.filter(
      (widget) => widget.type === 'Online'
    )
    const socialList = reportWidgetsLists.filter(
      (widget) => widget.type === 'Social'
    )
    state.reportWidgetsLists = {
      online: onlineList,
      social: socialList,
    }
  },

  // Account Analysis
  [mutator.SET_NEW_ACCOUNT_ANALYSIS_WORKSPACE](state, data) {
    if (data) {
      state.newAccountAnalysisWorkspace = {
        ...state.newAccountAnalysisWorkspace,
        ...data,
      }
    }
  },

  [mutator.SET_NEW_ACCOUNT_ANALYSIS_PROJECT](state, data) {
    if (data) {
      state.newAccountAnalysisProject = {
        ...state.newAccountAnalysisProject,
        ...data,
      }
    }
  },

  // 24/7

  [mutator.SET_NEW_TFS_WORKSPACE](state, data) {
    if (data) {
      state.newTFSWorkspace = {
        ...state.newTFSWorkspace,
        ...data,
      }
    }
  },

  [mutator.SET_NEW_TFS_PROJECT](state, data) {
    if (data) {
      state.newTFSProject = {
        ...state.newTFSProject,
        ...data,
      }
    }
  },
}
