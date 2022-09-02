const state = {
  loading: false,
  projects: [],
  workspaces: [],
  workspace: '',
  userId: '',
  channelType: '',
  newProject: {
    title: '',
    note: '',
    keywords: '',
    ignore_keywords: '',
    max_items: '',
    image: null,
    arabic_name: '',
    english_name: '',
    social: false,
    online: false,
    premium: false,
    creator: null,
    workspace: null,
  },
}

export default state
