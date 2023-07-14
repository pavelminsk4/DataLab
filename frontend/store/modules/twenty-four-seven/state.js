const state = {
  loading: false,
  workspaces: [],
  items: {},
  relatedContent: [],
  newProjectId: null,
  newWorkspaceId: null,
  statusMessage: null,
  textTranslation: {title: '', text: ''},
  aiSummary: null,
  translatedAISummary: null,
  sortType: {label: 'Latest', value: 'asc_date'},
}

export default state
