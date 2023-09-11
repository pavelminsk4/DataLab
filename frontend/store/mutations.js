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

  // [mutator.SET_COUNTRIES](state, countries) {
  //   state.countries = countries
  // },

  // [mutator.SET_LANGUAGES](state, languages) {
  //   state.languages = languages
  // },

  // [mutator.SET_SOURCES](state, sources) {
  //   state.sources = sources
  // },

  // [mutator.SET_AUTHORS](state, authors) {
  //   state.authors = authors
  // },

  [mutator.DELETE_KEYWORDS_LIST](state, index) {
    state.keywords.splice(index, 1)
  },

  [mutator.SET_ADDITIONAL_FILTERS](state, data) {
    state.additionalFilters = {...state.additionalFilters, ...data}
  },

  [mutator.SET_SUMMARY_WIDGET](state, {widgetId, data}) {
    state.summary = {id: widgetId, data}
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = data
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
