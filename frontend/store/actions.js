import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.LOGOUT]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.logout()
      window.location.href = '/accounts/login/'
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_USER_INFORMATION]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const userInfo = await api.getLoggedUser()
      commit(mutator.SET_USER_INFORMATION, userInfo)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_COUNTRIES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const countries = await api.getCountries()
      commit(mutator.SET_COUNTRIES, countries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_LANGUAGES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const languages = await api.getLanguages()
      commit(mutator.SET_LANGUAGES, languages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOURCES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sources = await api.getSources()
      commit(mutator.SET_SOURCES, sources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const authors = await api.getAuthors()
      commit(mutator.SET_AUTHORS, authors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SUMMARY_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const summary = await api.getSummaryWidget(projectId)
      commit(mutator.SET_SUMMARY_WIDGET, summary)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_VOLUME_WIDGET]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const volume = await api.getVolumeWidget({projectId, value})
      commit(mutator.SET_VOLUME_WIDGET, volume)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.getListOfDisplayedWidgets(projectId)
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const clippingFeedContent = await api.getClippingFeedContentWidget(
        projectId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createWorkspace(workspace)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createNewProject(projectData)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createClippingFeedContent(data)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_OLD_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateWorkspace({workspaceId, data})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_PROJECT]({commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateProject({projectId, data})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_AVAILABLE_WIDGETS]({commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateAvailableWidgets({projectId, data})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.postSearch(data)
      commit(mutator.SET_SEARCH_DATA, response)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_PROJECT_STATE]({commit}, newProject) {
    commit(mutator.SET_NEW_PROJECT, newProject)
  },

  async [action.UPDATE_NEW_WORKSPACE]({commit}, workspaceInfo) {
    commit(mutator.SET_NEW_WORKSPACE, workspaceInfo)
  },

  async [action.UPDATE_KEYWORDS_LIST]({commit}, keywords) {
    commit(mutator.SET_KEYWORDS_LIST, keywords)
  },

  async [action.UPDATE_CURRENT_STEP]({commit}, step) {
    commit(mutator.SET_CURRENT_STEP, step)
  },

  async [action.UPDATE_ADDITIONAL_FILTERS]({commit}, data) {
    commit(mutator.SET_ADDITIONAL_FILTERS, data)
  },

  async [action.REFRESH_DISPLAY_CALENDAR]({commit}, val) {
    commit(mutator.SET_DISPLAY_CALENDAR, val)
  },

  async [action.CLEAR_STATE]({commit}) {
    commit(mutator.RESET_STATE)
  },

  async [action.CLEAR_KEYWORDS_LIST]({commit}, index) {
    commit(mutator.DELETE_KEYWORDS_LIST, index)
  },
}
