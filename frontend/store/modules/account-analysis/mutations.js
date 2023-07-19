import {mutator} from '@store/constants'
import {initialState} from '@store/modules/account-analysis/widgets/state'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  [mutator.SET_WORKSPACES](state, workspaces) {
    state.workspaces = workspaces.map((workspace) => ({
      ...workspace,
      projects: workspace.account_analysis_workspace_projects,
    }))
  },

  [mutator.UPDATE_WORKSPACE](state, workspace) {
    const currentWorkspaceIndex = state.workspaces.findIndex(
      (currentWorkspace) => currentWorkspace.id === workspace.id
    )
    state.workspaces[currentWorkspaceIndex] = workspace
  },

  [mutator.SET_ACCOUNT_ANALYSIS_WORKSPACE_ID](state, id) {
    state.newWorkspaceId = id
  },

  [mutator.SET_ACCOUNT_ANALYSIS_PROJECT_ID](state, id) {
    state.newProjectId = id
  },

  [mutator.SET_LIST_OF_PROFILE_HANDLE](state, data) {
    state.listOfProfilesHandle = data
  },

  [mutator.SET_AVAILABLE_WIDGETS](state, data) {
    state.availableWidgets = data
  },

  [mutator.SET_ACCOUNT_ACTIVITY_POSTS](state, data) {
    state.accountActivityPosts = data.posts || []
    state.accountActivityNumOfPosts = data.num_posts
  },

  [mutator.SET_MENTIONS_POSTS](state, data) {
    state.mentionsPosts = data.posts || []
    state.mentionsNumOfPosts = data.num_posts
  },

  [mutator.CLEAR_WIDGETS_DATA](state) {
    state.widgets = {...initialState}
  },
}
