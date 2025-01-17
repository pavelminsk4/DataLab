import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_WORKSPACES]({commit}, id) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.twentyFourSeven.getWorkspaces(id)
      commit(mutator.SET_WORKSPACES, workspaces)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_TFS_WORKSPACE]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.UPDATE_NEW_TFS_WORKSPACE, data, {
        root: true,
      })
      const response = await api.twentyFourSeven.createWorkspace(data)
      commit(mutator.SET_TFS_WORKSPACE_ID, response.id)
      commit(mutator.SET_TFS_PROJECT_ID, response.tfs_workspace_projects[0].id)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_TFS_PROJECT]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.twentyFourSeven.createProject(data)
      commit(mutator.SET_TFS_PROJECT_ID, response.id)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.twentyFourSeven.updateWorkspace({
        workspaceId,
        data,
      })
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_PROJECT]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TFS_ITEMS]({commit, state}, {projectId, status, page}) {
    commit(mutator.SET_LOADING, true)
    try {
      const items = await api.twentyFourSeven.getItems(
        projectId,
        status,
        page,
        state.sortType.value
      )
      commit(mutator.SET_TFS_ITEMS, {items, status})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TFS_RELATED_CONTENT]({commit}, itemId) {
    commit(mutator.SET_LOADING, true)
    try {
      const relatedContent = await api.twentyFourSeven.getRelatedContent(itemId)
      commit(mutator.SET_TFS_RELATED_CONTENT, relatedContent)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_TFS_ITEM_STATUS](
    {commit, dispatch},
    {projectId, postId, value, oldStatus, page}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.updatePostDetails(projectId, postId, value)
      await dispatch(action.GET_TFS_ITEMS, {
        projectId,
        page,
        ...value,
      })
      await dispatch(action.GET_TFS_ITEMS, {projectId, status: oldStatus, page})
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_TFS_ITEM_DATA](
    {commit, dispatch},
    {projectId, postId, value, page}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.twentyFourSeven.updatePostDetails(projectId, postId, value)
      await dispatch(action.GET_TFS_ITEMS, {
        projectId,
        status: value.status,
        page,
      })
      return
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.SEND_TFS_MESSAGE_TO_WHATSAPP](
    {commit},
    {phoneNumber, message}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.twentyFourSeven.sendMessageToWhatsapp(
        phoneNumber,
        message
      )
      commit(mutator.SET_TFS_STATUS_MESSAGE, response.status)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_TFS_ORIGINAL_CONTENT_LANGUAGE](
    {commit},
    {newLanguage, title, text}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const translatedTitle = await api.twentyFourSeven.translateLanguage(
        newLanguage,
        title
      )
      const translatedText = await api.twentyFourSeven.translateLanguage(
        newLanguage,
        text
      )
      commit(mutator.SET_TFS_TRANSLATED_ORIGINAL_CONTENT, {
        title: translatedTitle.translated_text,
        text: translatedText.translated_text,
      })
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CHANGE_HEADER_LANGUAGE]({commit}, {newLanguage, header}) {
    commit(mutator.SET_LOADING, true)
    try {
      const translatedHeader = await api.twentyFourSeven.translateLanguage(
        newLanguage,
        header
      )
      commit(mutator.SET_HEADER_TRANSLATED, {
        header: translatedHeader.translated_text,
      })
      return
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_TFS_AI_SUMMARY]({commit}, postId) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.twentyFourSeven.createAISummary(postId)
      commit(mutator.SET_TFS_AI_SUMMARY, response)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_TFS_SORT_TYPE]({commit}, sortType) {
    commit(mutator.SET_TFS_SORT_TYPE, sortType)
  },

  async [action.CLEAR_TFS_ITEMS]({commit}) {
    commit(mutator.RESET_TFS_ITEMS)
  },

  async [action.CLEAR_TFS_TRANSLATED_TEXT]({commit}) {
    commit(mutator.SET_TFS_TRANSLATED_ORIGINAL_CONTENT, {
      title: '',
      text: '',
    })
  },

  async [action.CLEAR_TFS_WHATSAPP_MESSAGE]({commit}) {
    commit(mutator.SET_TFS_STATUS_MESSAGE, null)
  },

  async [action.CLEAR_TFS_RELATED_CONTENT]({commit}) {
    commit(mutator.SET_TFS_RELATED_CONTENT, [])
  },

  async [action.CLEAR_TFS_AI_SUMMARY]({commit}) {
    commit(mutator.SET_TFS_AI_SUMMARY, '')
    commit(mutator.SET_HEADER_TRANSLATED, {
      header: '',
      text: '',
    })
  },
}
