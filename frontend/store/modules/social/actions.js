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
      commit(mutator.SET_NEW_PROJECT_ID, response.projects[0].id)
      response.projects = response.social_workspace_projects
      return response
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
}
