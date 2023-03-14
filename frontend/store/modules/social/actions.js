import api from '@api/api'
import {action, mutator} from './constants'
import {
  action as generalAction,
  mutator as generalMutator,
} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.social.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
    } catch (e) {
      console.log(e)
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
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.social.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.social.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.social.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit, dispatch}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.social.createProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(generalAction.GET_USER_INFORMATION, null, {root: true})
      return response
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_SEARCH]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.social.postSearch(data)
      commit(generalMutator.SET_SEARCH_DATA, response.posts, {root: true})
      commit(generalMutator.SET_NUMBER_OF_POSTS, response.num_posts, {
        root: true,
      })
      commit(generalMutator.SET_NUMBER_OF_PAGES, response.num_pages, {
        root: true,
      })
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit, dispatch}, data) {
    commit(
      generalMutator.SET_LOADING_WIDGETS,
      {clippingWidget: true},
      {root: true}
    )
    try {
      await api.social.createClippingFeedContent(data.posts)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: data.projectId,
        widgetId: data.widgetId,
      })
    } catch (e) {
      console.log(e)
    } finally {
      commit(
        generalMutator.SET_LOADING_WIDGETS,
        {clippingWidget: false},
        {root: true}
      )
    }
  },
  async [action.DELETE_CLIPPING_FEED_CONTENT](
    {commit, dispatch},
    {projectId, postId, widgetId}
  ) {
    commit(
      generalMutator.SET_LOADING_WIDGETS,
      {clippingWidget: true},
      {root: true}
    )
    try {
      await api.social.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: projectId,
        widgetId: widgetId,
      })
    } catch (e) {
      console.log(e)
    } finally {
      commit(
        generalMutator.SET_LOADING_WIDGETS,
        {clippingWidget: false},
        {root: true}
      )
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(generalMutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.social.getAllWidgets(projectId)

      commit(generalMutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
    } catch (e) {
      console.log(e)
    } finally {
      commit(generalMutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_AVAILABLE_WIDGETS](
    {commit, dispatch},
    {projectId, widgetsList}
  ) {
    commit(generalMutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.social.updateAvailableWidgets({
        projectId,
        data: widgetsList,
      })
      commit(generalMutator.SET_AVAILABLE_WIDGETS, availableWidgets, {
        root: true,
      })
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(generalMutator.SET_LOADING, false)
    }
  },

  async [action.POST_INTERACTIVE_WIDGETS](
    {commit},
    {projectId, widgetId, data}
  ) {
    commit(generalMutator.SET_LOADING, true)
    try {
      const response = await api.social.postInteractiveWidget({
        projectId,
        widgetId,
        data,
      })

      commit(generalMutator.SET_INTERACTIVE_DATA, response)
    } catch (e) {
      console.log(e)
    } finally {
      commit(generalMutator.SET_LOADING, false)
    }
  },

  // Widgets
  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(generalMutator.SET_LOADING, true, {root: true})
    try {
      const summary = await api.social.getSummaryWidget(projectId, widgetId)
      commit(generalMutator.SET_SUMMARY_WIDGET, summary, {root: true})
    } catch (e) {
      console.log(e)
    } finally {
      commit(generalMutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(
      generalMutator.SET_LOADING_WIDGETS,
      {clippingWidget: true},
      {root: true}
    )
    try {
      const clippingFeedContent = await api.social.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(
        generalMutator.SET_CLIPPING_FEED_CONTENT_WIDGET,
        clippingFeedContent,
        {root: true}
      )
    } catch (e) {
      console.log(e)
    } finally {
      commit(
        generalMutator.SET_LOADING_WIDGETS,
        {clippingWidget: false},
        {root: true}
      )
    }
  },

  async [action.GET_CONTENT_VOLUME_WIDGET](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(generalMutator.SET_LOADING, true, {root: true})
    try {
      const volume = await api.social.getContentVolumeWidget({
        projectId,
        value,
        widgetId,
      })
      commit(generalMutator.SET_VOLUME_WIDGET, volume, {root: true})
    } catch (e) {
      console.log(e)
    } finally {
      commit(generalMutator.SET_LOADING, false, {root: true})
    }
  },
}
