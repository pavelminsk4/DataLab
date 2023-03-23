import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },
  [get.WORKSPACES](state) {
    return state.workspaces
  },
  [get.NEW_WORKSPACE_ID](state) {
    return state.newWorkspaceId
  },
  [get.NEW_PROJECT_ID](state) {
    return state.newProjectId
  },

  [get.PROJECTS](state) {
    return state.projects
  },

  [get.CLIPPING_WIDGETS_DETAILS](state) {
    return state.availableWidgets?.clipping_feed_content
  },

  [get.COUNTRIES](state) {
    return state.countries.map((el) => el.locationString)
  },

  [get.LANGUAGES](state) {
    return state.languages.map((el) => el.language)
  },

  [get.AUTHORS](state) {
    return state.authors.map((el) => el.user_name)
  },
}
