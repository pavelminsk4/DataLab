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
  countries: [],
  languages: [],
  sources: [],
  authors: [],
  additionalFilters: {},
  summary: {},
  volume: {},
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
  },
  isShowCalendar: false,
}

export default state
