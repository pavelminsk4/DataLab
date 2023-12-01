import api from '@api/api'
import {action, mutator} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.social.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.social.createWorkspace(workspace)
      commit(mutator.SET_NEW_WORKSPACE_ID, response.id)
      commit(
        mutator.SET_NEW_PROJECT_ID,
        response.social_workspace_projects[0].id
      )
      return {
        ...response,
        projects: response.social_workspace_projects,
      }
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.social.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.social.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.social.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_PROJECT]({commit, dispatch}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.social.createProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(action.GET_USER_INFORMATION, null, {root: true})
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_PROJECT]({dispatch, commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.social.updateProject({projectId, data})
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_PROJECT]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.social.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.social.postSearch(data)
      commit(mutator.SET_SEARCH_DATA, response.posts, {root: true})
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {
        root: true,
      })
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {
        root: true,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      await api.social.createClippingFeedContent(data.posts)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: data.projectId,
        widgetId: data.widgetId,
      })
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
      await api.social.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: projectId,
        widgetId: widgetId,
      })
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    commit(mutator.SET_AVAILABLE_WIDGETS, {}, {root: true})
    commit(mutator.SET_AVAILABLE_WIDGETS, {})
    try {
      const availableWidgets = await api.social.getAllWidgets(projectId)

      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      return availableWidgets
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
      const availableWidgets = await api.social.updateAvailableWidgets({
        projectId,
        data: widgetsList,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
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
      const response = await api.social.postInteractiveWidget({
        projectId,
        widgetId,
        data,
      })

      commit(mutator.SET_INTERACTIVE_DATA, response, {
        root: true,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS]({commit}, {word, limit}) {
    try {
      const authors = await api.social.getAuthors(word, limit)
      commit(mutator.SET_AUTHORS, authors)
      return authors
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.GET_COUNTRIES]({commit}, {word, limit}) {
    try {
      const countries = await api.social.getCountries(
        capitalizeFirstLetter(word),
        limit
      )
      commit(mutator.SET_COUNTRIES, countries)
      return countries
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.GET_LANGUAGES]({commit}, {word, limit}) {
    try {
      const languages = await api.social.getLanguages(
        capitalizeFirstLetter(word, limit)
      )
      commit(mutator.SET_LANGUAGES, languages)
      return languages
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_FILTERS_FOR_WIDGET](
    {commit, dispatch},
    {projectId, widgetId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.social.postFiltersForWidget({projectId, widgetId, data})
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionAuthors = await api.social.getFiltersAuthors(projectId)
      commit(mutator.SET_FILTERS_AUTHORS, dimensionAuthors, {
        root: true,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_COUNTRIES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionCountries = await api.social.getFiltersCountries(projectId)
      commit(mutator.SET_FILTERS_COUNTRIES, dimensionCountries, {
        root: true,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_LANGUAGES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionLanguages = await api.social.getFiltersLanguages(projectId)
      commit(mutator.SET_FILTERS_LANGUAGES, dimensionLanguages, {
        root: true,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOCIAL_FILTERS_OPTIONS]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.GET_FILTER_AUTHORS, projectId)
      await dispatch(action.GET_FILTER_COUNTRIES, projectId)
      await dispatch(action.GET_FILTER_LANGUAGES, projectId)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_INSTANT_REPORT]({commit, dispatch}, {projectId}) {
    commit(mutator.SET_DOWNLOADING_INSTANT_REPORT, true)
    try {
      const response = await api.social.downloadInstantReport(projectId)

      dispatch(
        action.OPEN_FLASH_MESSAGE,
        {
          message: 'Your report is generated. Starting the download.',
          title: 'Instant Report',
          type: 'Success',
        },
        {root: true}
      )

      return response
    } finally {
      commit(mutator.SET_DOWNLOADING_INSTANT_REPORT, false)
    }
  },
}
