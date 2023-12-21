import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces.map((workspace) => ({
      ...workspace,
      projects: workspace.tfs_workspace_projects,
    }))
  },

  [mutator.SET_TFS_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_TFS_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
  },

  [mutator.SET_TFS_ITEMS](state, {items, status}) {
    state.items[status] = items
  },

  [mutator.SET_TFS_RELATED_CONTENT](state, relatedContent) {
    state.relatedContent = relatedContent
  },

  [mutator.SET_TFS_STATUS_MESSAGE](state, statusMessage) {
    state.statusMessage = statusMessage
  },

  [mutator.SET_TFS_TRANSLATED_ORIGINAL_CONTENT](state, {title, text}) {
    state.textTranslation.title = title
    state.textTranslation.text = text
  },

  [mutator.SET_HEADER_TRANSLATED](state, {header, text}) {
    state.translatedText.header = header
    state.translatedText.text = text
  },

  [mutator.SET_TFS_AI_SUMMARY](state, summary) {
    state.aiSummary = summary
  },

  [mutator.SET_TFS_SORT_TYPE](state, sortType) {
    state.sortType = sortType
  },

  [mutator.RESET_TFS_ITEMS](state) {
    state.items = {}
  },
}
