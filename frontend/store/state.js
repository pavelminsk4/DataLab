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
  numberOfPages: null,
  numberOfPosts: null,
  searchPage: 1,
  countries: [],
  languages: [],
  sources: [],
  authors: [],
  additionalFilters: {},
  summary: {},
  volume: {},
  clippingFeedContent: [],
  topAuthors: [],
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
}

export default state
