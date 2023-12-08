export const newWorkspaceInitialState = {
  title: '',
  description: '',
  members: [],
  projects: [],
  department: null,
}

export const newProjectInitialState = {
  title: '',
  note: '',
  keywords: [],
  additional_keywords: [],
  ignore_keywords: [],
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
  start_search_date: null,
  end_search_date: null,
}

export const newReportInitialState = {
  step: 1,
  name: '',
  description: '',
  report_language: 'English',
  report_format: 'PDF',
  report_template: '',
  projects: [],
  widgetsTemplates: {},
}

export const newAccountAnalysisWorkspaceInitialState = {
  step: 1,
  title: '',
  description: '',
  department: null,
  members: [],
  account_analysis_workspace_projects: [],
  projects: [],
}

export const newAccountAnalysisProjectInitialState = {
  title: '',
  profile_handle: '',
  start_search_date: null,
  end_search_date: null,
  min_followers: null,
  max_followers: null,
  language_filter: [],
  country_filter: [],
  sentiment_filter: [],
  source_filter: [],
  author_filter: [],
  language_dimensions: [],
  country_dimensions: [],
  sentiment_dimensions: [],
  source_dimensions: [],
  author_dimensions: [],
  creator: null,
  workspace: null,
  members: [],
}

export const newTFSWorkspaceInitialState = {
  step: 1,
  title: '',
  description: '',
  department: null,
  members: [],
  tfs_workspace_projects: [],
  projects: [],
}

export const newTFSProjectInitialState = {
  step: 2,
  title: '',
  note: '',
  keywords: [],
  additional_keywords: [],
  ignore_keywords: [],
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
  start_search_date: null,
  end_search_date: null,
  searchFilters: {
    page_number: 1,
    posts_per_page: 20,
  },
}

export default {
  loading: false,
  loadingWidgets: {
    loading: false,
    clippingWidget: false,
  },
  mode: '',
  isCreateReportMode: false,
  translation: {},
  platformLanguage: 'ar',

  flashMessages: [],
  flashMessagesCount: 0,

  currentStep: '',
  projects: [],
  workspaces: [],
  workspace: '',
  userInfo: null,
  channelType: '',
  keywords: {},
  searchData: [],
  sortPosts: 'Latest',
  isSearchPerformed: false,
  numberOfPages: 0,
  numberOfPosts: 0,
  newProjectId: null,
  newWorkspaceId: null,
  searchPage: 1,
  dimensionAuthors: null,
  dimensionLanguages: null,
  dimensionCountries: null,
  dimensionSources: null,
  selectedFilters: {},
  additionalFilters: {},
  summary: {
    id: 0,
    data: {},
  },
  clippingFeedContent: [],
  dimensions: [],
  templates: [],

  newWorkspace: {...newWorkspaceInitialState},
  newProject: {...newProjectInitialState},

  isShowCalendarContents: false,
  inreractiveDataModal: {
    isShow: false,
  },
  companyUsers: [],
  interactiveData: [],
  paginationData: {},

  //reports
  regularReports: [],
  reportWidgetsLists: new Map(),
  newReport: {...newReportInitialState},

  // Account Analysis
  newAccountAnalysisWorkspace: {...newAccountAnalysisWorkspaceInitialState},
  newAccountAnalysisProject: {...newAccountAnalysisProjectInitialState},

  // 24/7
  newTFSWorkspace: {...newTFSWorkspaceInitialState},
  newTFSProject: {...newTFSProjectInitialState},

  widgets: {
    hasAnimation: true,
  },
}
