const state = {
  loading: false,
  projects: [],
  workspaces: [],
  workspace: '',
  userId: '',
  channelType: '',
  keywords: [],
  searchData: [],
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
    ignore_keywords: '',
    max_items: '',
    image: null,
    arabic_name: '',
    english_name: '',
    social: false,
    online: false,
    premium: false,
    creator: null,
  },
}

export default state
