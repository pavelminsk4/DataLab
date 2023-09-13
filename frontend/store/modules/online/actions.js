import api from '@api/api'
import {action, mutator} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.online.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.postSearch(data)
      commit(mutator.SET_SEARCH_DATA, response.posts, {root: true})
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {root: true})
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.createWorkspace(workspace)
      commit(mutator.SET_NEW_WORKSPACE_ID, response.id)
      commit(mutator.SET_NEW_PROJECT_ID, response.projects[0].id)
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit, dispatch}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.createNewProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(action.GET_USER_INFORMATION, null, {root: true})
      return response
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.online.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_PROJECT]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
      await dispatch(action.GET_USER_INFORMATION)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    commit(mutator.SET_AVAILABLE_WIDGETS, {}, {root: true})
    commit(mutator.SET_AVAILABLE_WIDGETS, {})
    try {
      const availableWidgets = await api.online.getListOfDisplayedWidgets(
        projectId
      )
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      return availableWidgets
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_INTERACTIVE_WIDGETS](
    {commit},
    {projectId, widgetId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.postInteractiveWidget({
        projectId,
        widgetId,
        data,
      })

      commit(mutator.SET_INTERACTIVE_DATA, response, {
        root: true,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_AVAILABLE_WIDGETS](
    {commit, dispatch},
    {projectId, widgetsList}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.online.updateAvailableWidgets({
        projectId,
        data: widgetsList,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_PROJECT]({dispatch, commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.updateProject({projectId, data})
      await dispatch(action.GET_WORKSPACES)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_INSTANT_REPORT]({commit}, {projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      return api.online.downloadInstantReport(projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      await api.online.createClippingFeedContent(data.posts)
      await dispatch(`widgets/${action.GET_CLIPPING_FEED_CONTENT_WIDGET}`, {
        projectId: data.projectId,
        widgetId: data.widgetId,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.DELETE_CLIPPING_FEED_CONTENT](
    {commit, dispatch},
    {projectId, postId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      await api.online.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(`widgets/${action.GET_CLIPPING_FEED_CONTENT_WIDGET}`, {
        projectId: projectId,
        widgetId: widgetId,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.GET_FILTERS_OPTIONS]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.GET_FILTER_AUTHORS, projectId)
      await dispatch(action.GET_FILTER_COUNTRIES, projectId)
      await dispatch(action.GET_FILTER_LANGUAGES, projectId)
      await dispatch(action.GET_FILTER_SOURCES, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionAuthors = await api.online.getFiltersAuthors(projectId)
      commit(mutator.SET_FILTERS_AUTHORS, dimensionAuthors, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_LANGUAGES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionLanguages = await api.online.getFiltersLanguages(projectId)
      commit(mutator.SET_FILTERS_LANGUAGES, dimensionLanguages, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_COUNTRIES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionCountries = await api.online.getFiltersCountries(projectId)
      commit(mutator.SET_FILTERS_COUNTRIES, dimensionCountries, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_SOURCES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionSources = await api.online.getFiltersSources(projectId)
      commit(mutator.SET_FILTERS_SOURCES, dimensionSources, {root: true})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS]({commit}, word) {
    try {
      const authors = await api.online.getAuthors(word)
      commit(mutator.SET_AUTHORS, authors)
      return authors
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_SOURCES]({commit}, word) {
    try {
      const sources = await api.online.getSources(word)
      commit(mutator.SET_SOURCES, sources)
      return sources
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_LANGUAGES]({commit}, word) {
    try {
      const languages = await api.online.getLanguages(
        capitalizeFirstLetter(word)
      )
      commit(mutator.SET_LANGUAGES, languages)
      return languages
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_COUNTRIES]({commit}, word) {
    try {
      const countries = await api.online.getCountries(
        capitalizeFirstLetter(word)
      )
      commit(mutator.SET_COUNTRIES, countries)
      return countries
    } catch (error) {
      console.error(error)
      return error
    }
  },
}
