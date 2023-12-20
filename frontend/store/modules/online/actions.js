import api from '@api/api'
import {action, mutator} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.online.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_WORKSPACE]({commit}, id) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspace = await api.online.getWorkspace(id)
      commit(mutator.SET_WORKSPACE, workspace)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECT]({commit}, id) {
    commit(mutator.SET_LOADING, true)
    try {
      const project = await api.online.getProject(id)
      commit(mutator.SET_PROJECT, project)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.online.postSearch(data)
      commit(
        mutator.SET_SEARCH_DATA,
        {posts: response.posts, sortPosts: data.sort_posts},
        {root: true}
      )
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts, {root: true})
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages, {root: true})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.POSTS_PREVIEW]({commit}, filters) {
    commit(mutator.SET_LOADING, true)

    const strFilters = Object.keys(filters)
      .map((e) => filters[e].map((f) => `${e}=${f}`))
      .filter((e) => e.length > 0)
      .join('&')

    try {
      const response = await api.online.postsPreview(strFilters)
      commit(mutator.SET_SEARCH_DATA, {posts: response.posts}, {root: true})
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
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.online.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_STATUS_COLLECTING_DATA](
    {commit, dispatch},
    {projectId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.updateStatusCollectingData(projectId, data)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
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
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_PROJECT]({dispatch, commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.online.updateProject(data)
      await dispatch(action.GET_PROJECT, data.project_pk)
      await dispatch(action.POST_SEARCH, {
        sort_posts: data.sort_posts || [],
        project_pk: data.project_pk,
        posts_per_page: 20,
        page_number: 1,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_INSTANT_REPORT]({commit, dispatch}, {projectId}) {
    commit(mutator.SET_DOWNLOADING_INSTANT_REPORT, true)
    try {
      const response = await api.online.downloadInstantReport(projectId)

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

  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      await api.online.createClippingFeedContent(data.posts)
      await dispatch(`widgets/${action.GET_CLIPPING_FEED_CONTENT_WIDGET}`, {
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
      await api.online.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(`widgets/${action.GET_CLIPPING_FEED_CONTENT_WIDGET}`, {
        projectId: projectId,
        widgetId: widgetId,
      })
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.REMOVE_POST_FROM_PROJECT](
    {rootState, dispatch},
    {postId, projectId}
  ) {
    await api.online.removePostFromProject({postId, projectId})
    await dispatch(action.POST_SEARCH, {
      sort_posts: rootState.sortPosts,
      project_pk: projectId,
      posts_per_page: 20,
      page_number: 1,
    })

    await dispatch(
      action.OPEN_FLASH_MESSAGE,
      {
        type: 'Success',
        message: 'The Post removed from this project',
      },
      {root: true}
    )
  },

  async [action.GET_FILTERS_OPTIONS]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.GET_FILTER_AUTHORS, projectId)
      await dispatch(action.GET_FILTER_COUNTRIES, projectId)
      await dispatch(action.GET_FILTER_LANGUAGES, projectId)
      await dispatch(action.GET_FILTER_SOURCES, projectId)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionAuthors = await api.online.getFiltersAuthors(projectId)
      commit(mutator.SET_FILTERS_AUTHORS, dimensionAuthors, {root: true})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_LANGUAGES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionLanguages = await api.online.getFiltersLanguages(projectId)
      commit(mutator.SET_FILTERS_LANGUAGES, dimensionLanguages, {root: true})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_COUNTRIES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionCountries = await api.online.getFiltersCountries(projectId)
      commit(mutator.SET_FILTERS_COUNTRIES, dimensionCountries, {root: true})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_FILTER_SOURCES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionSources = await api.online.getFiltersSources(projectId)
      commit(mutator.SET_FILTERS_SOURCES, dimensionSources, {root: true})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS]({commit}, {word, limit}) {
    try {
      const authors = await api.online.getAuthors(word, limit)
      commit(mutator.SET_AUTHORS, authors)
      return authors
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOURCES]({commit}, {word, limit}) {
    try {
      const sources = await api.online.getSources(word, limit)
      commit(mutator.SET_SOURCES, sources)
      return sources
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_LANGUAGES]({commit}, {word, limit}) {
    try {
      const languages = await api.online.getLanguages(
        capitalizeFirstLetter(word),
        limit
      )
      commit(mutator.SET_LANGUAGES, languages)
      return languages
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_COUNTRIES]({commit}, {word, limit}) {
    try {
      const countries = await api.online.getCountries(
        capitalizeFirstLetter(word),
        limit
      )
      commit(mutator.SET_COUNTRIES, countries)
      return countries
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CLEAR_CURRENT_PROJECT]({commit}) {
    commit(mutator.RESET_PROJECT_STATE)
  },
}
