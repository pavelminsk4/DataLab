const state = {
  loading: false,
  currentStep: 'Step1',
  projects: [],
  workspaces: [],
  workspace: '',
  userInfo: [],
  channelType: '',
  keywords: {},
  searchData: [],
  numberOfPages: 0,
  numberOfPosts: 0,
  newProjectId: null,
  newWorkspaceId: null,
  searchPage: 1,
  selectedDimensions: null,
  dimensionAuthors: null,
  dimensionLanguages: null,
  dimensionCountries: null,
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
  dimensions: [],
  templates: [],
  newWorkspace: {
    title: '',
    description: '',
    members: [],
    company: null,
    projects: [],
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
  availableWidgets: null,
  alerts: [],
}

export default state
