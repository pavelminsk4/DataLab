const initialState = {
  loading: false,
  loadingWidgets: {
    clippingWidget: false,
  },
  currentStep: '',
  projects: [],
  workspaces: [],
  workspace: '',
  userInfo: null,
  channelType: '',
  keywords: {},
  searchData: [],
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
  selectedDimensions: {},
  countries: [],
  languages: [],
  sources: [],
  authors: [],
  additionalFilters: {},
  summary: {},
  volume: {},
  clippingFeedContent: [],
  topAuthors: [],
  topBrands: [],
  topCountries: [],
  topLanguages: [],
  topSharingSources: [],
  sourcesByLanguage: [],
  sourcesByCountry: [],
  overallTopSources: [],
  sentimentTopSources: {},
  sentimentTopCountries: {},
  sentimentTopLanguages: {},
  sentimentTopAuthors: {},
  sentimentForPeriod: [],
  contentVolumeTopSources: [],
  contentVolumeTopAuthors: [],
  contentVolumeTopCountries: [],
  sentimentTopKeywordsWidget: {},
  topKeywordsWidget: [],
  sentimentDiagram: [],
  sentimentNumberOfResult: [],
  authorsByCountry: [],
  authorsByLanguage: [],
  authorsBySentiment: [],
  overallTopAuthors: [],
  dimensions: [],
  templates: [],
  newWorkspace: {
    title: '',
    description: '',
    members: [],
    projects: [],
    department: null,
  },
  newProject: {
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
  },
  isShowCalendarContents: false,
  inreractiveDataModal: {
    isShow: false,
  },
  availableWidgets: null,
  alerts: [],
  companyUsers: [],
  interactiveData: [],
  paginationData: {},

  //reports
  regularReports: [],
  reportWidgetsList: [],
  newReport: {
    step: 1,
    name: '',
    description: '',
    report_language: 'English',
    report_format: 'PDF',
    report_template: '',
    projects: [],
    widgetsTemplates: {},
  },
}

const state = {...initialState}

export default state
