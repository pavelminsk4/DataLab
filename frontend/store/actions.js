import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_TRANSLATED_TEXT]({commit, state}, text) {
    try {
      const translation = await api.postTranslationText({
        en: text,
      })

      if (state.platformLanguage === 'ar') {
        await commit(mutator.SET_TRANSLATION, {
          text,
          translation: translation.ar,
        })
      } else {
        await commit(mutator.SET_TRANSLATION, {text, translation: text})
      }
      return translation
    } catch (error) {
      console.error(error)
      return text
    }
  },

  async [action.POST_PLATFORM_LANGUAGE]({commit, dispatch, state}, newLang) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.postPlatformLanguage(state.userInfo.user_profile.id, newLang)
      await commit(mutator.SET_PLATFORM_LANG, newLang)
      await dispatch(action.GET_USER_INFORMATION)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.LOGOUT]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.logout()
      window.location.href = '/accounts/login/'
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PROJECTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const projects = await api.getProjects()
      commit(mutator.SET_PROJECTS, projects)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_USER_INFORMATION]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const userInfo = await api.getLoggedUser()
      commit(mutator.SET_USER_INFORMATION, userInfo)

      return userInfo
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      const clippingFeedContent = await api.online.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, {
        widgetId,
        data: clippingFeedContent,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    commit(mutator.SET_AVAILABLE_WIDGETS, {})
    commit(mutator.SET_AVAILABLE_WIDGETS, {})
    try {
      const availableWidgets = await api.online.getListOfDisplayedWidgets(
        projectId
      )
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      return availableWidgets
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CHANGE_ONLINE_POST_SENTIMENT](
    _context,
    {postId, departmentId, newSentiment}
  ) {
    try {
      const response = await api.changeOnlinePostSentiment(
        postId,
        departmentId,
        newSentiment
      )
      return response
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.CHANGE_SOCIAL_POST_SENTIMENT](
    _context,
    {postId, departmentId, newSentiment}
  ) {
    try {
      const response = await api.changeSocialPostSentiment(
        postId,
        departmentId,
        newSentiment
      )
      return response
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_FILTERS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensions = await api.getFilters()
      commit(mutator.SET_FILTERS, dimensions)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SELECTED_FILTERS]({commit}, selectedFilters) {
    commit(mutator.SET_LOADING, true)
    try {
      commit(mutator.SET_SELECTED_FILTERS, selectedFilters)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TEMPLATES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const templates = await api.getTemplates()
      commit(mutator.SET_TEMPLATES, templates)
      return templates
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_COMPANY_USERS]({commit}, companyId) {
    commit(mutator.SET_LOADING, true)
    try {
      const companyUsers = await api.getCompanyUsers(companyId)
      commit(mutator.SET_COMPANY_USERS, companyUsers)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_USER]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      return await api.createUser(data)
    } catch (error) {
      console.error(error)
      return {
        ...error.response.data,
        hasError: true,
      }
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.PUT_USER_DEPARTMENT](
    {commit, dispatch},
    {email, data, userId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.setUserDepartment({email, data})
      await dispatch(action.GET_COMPANY_USERS, userId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_USER_DATA](
    {commit, dispatch},
    {userId, data, currentUserId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateUserData({userId, data})
      await dispatch(action.GET_COMPANY_USERS, currentUserId)
    } catch (error) {
      console.error(error)
      return error
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
      await api.postFiltersForWidget({projectId, widgetId, data})
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_USER_FROM_COMPANY](
    {commit, dispatch},
    {userId, currentUserId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteUserFromCompany(userId)
      await dispatch(action.GET_COMPANY_USERS, currentUserId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOCIAL_INSTANTLY_REPORT](
    {commit},
    {departmentId, projectId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      return api.downloadSocialInstantlyReport(departmentId, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.SHOW_INTERACTIVE_DATA_MODAL](
    {commit, dispatch},
    {value, moduleType}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      commit(mutator.SET_INTERACTIVE_DATA_MODAL, value)
      switch (moduleType) {
        case 'Online':
          return await dispatch(
            `online/${action.POST_INTERACTIVE_WIDGETS}`,
            value
          )
        case 'Social':
          return await dispatch(
            `social/${action.POST_INTERACTIVE_WIDGETS}`,
            value
          )
        case 'AccountAnalysis':
          return await dispatch(
            `accountAnalysis/${action.POST_INTERACTIVE_WIDGETS}`,
            value
          )
      }
    } catch (error) {
      console.error(error)
      return error
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

  async [action.CLEAR_KEYWORDS_LIST]({commit}, index) {
    commit(mutator.DELETE_KEYWORDS_LIST, index)
  },

  async [action.CLEAR_STATE]({commit}) {
    commit(mutator.RESET_STATE)
  },

  async [action.CLEAR_SEARCH_LIST]({commit}) {
    commit(mutator.RESET_SEARCH_LIST)
  },

  async [action.CLEAR_INTERACTIVE_DATA]({commit}) {
    commit(mutator.RESET_INTERACTIVE_DATA)
  },

  // Reports
  async [action.GET_REGULAR_REPORTS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const regularReports = await api.getRegularReports()
      commit(mutator.SET_REGULAR_REPORTS, regularReports)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_REGULAR_REPORT]({commit, dispatch}, {data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createRegularReport(data)
      await dispatch(action.GET_REGULAR_REPORTS)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_REGULAR_REPORT](
    {dispatch, commit},
    {regularReportId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateRegularReport(regularReportId, data)
      await dispatch(action.GET_REGULAR_REPORTS)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.DELETE_REGULAR_REPORT]({dispatch, commit}, {regularReportId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteRegularReport(regularReportId)
      await dispatch(action.GET_REGULAR_REPORTS)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_WIDGETS_LISTS]({commit, dispatch}, projects) {
    commit(mutator.SET_LOADING, true)
    try {
      const projectsWidgetsList = {}

      projects.forEach(async (project) => {
        let currentAction = ''
        if (project.moduleType === 'Online')
          currentAction = action.GET_AVAILABLE_WIDGETS

        if (project.moduleType === 'Social')
          currentAction = `social/${action.GET_AVAILABLE_WIDGETS}`

        const projectList = await dispatch(currentAction, project.id)

        commit(mutator.SET_WIDGETS_LISTS, {id: project.id, projectList})
        projectsWidgetsList[project.id] = projectList
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_NEW_REPORT]({commit}, data) {
    commit(mutator.SET_NEW_REPORT, data)
  },
  async [action.CLEAR_NEW_REPORT]({commit}) {
    commit(mutator.SET_NEW_REPORT)
  },

  // Alerts

  async [action.CREATE_NEW_ALERT]({commit, dispatch}, {data, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createAlert(data)
      await dispatch(action.GET_ALERTS, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_ALERTS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const alerts = await api.getAlerts(projectId)
      commit(mutator.SET_ALERTS, alerts)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_ALERT]({commit, dispatch}, {data, alertId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateAlert({data, alertId})
      await dispatch(action.GET_ALERTS, data.project)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_ALERT]({commit, dispatch}, {alertId, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteAlert(alertId)
      await dispatch(action.GET_ALERTS, projectId)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_NEW_ALERT]({commit}, data) {
    commit(mutator.SET_NEW_ALERT, data)
  },
  async [action.CLEAR_NEW_ALERT]({commit}) {
    commit(mutator.SET_NEW_ALERT)
  },

  // Account Analysis
  async [action.UPDATE_NEW_ACCOUNT_ANALYSIS_WORKSPACE]({commit}, data) {
    commit(mutator.SET_NEW_ACCOUNT_ANALYSIS_WORKSPACE, data)
  },

  async [action.UPDATE_NEW_ACCOUNT_ANALYSIS_PROJECT]({commit}, data) {
    commit(mutator.SET_NEW_ACCOUNT_ANALYSIS_PROJECT, data)
  },

  // 24/7

  async [action.UPDATE_NEW_TFS_WORKSPACE]({commit}, data) {
    commit(mutator.SET_NEW_TFS_WORKSPACE, data)
  },

  async [action.UPDATE_NEW_TFS_PROJECT]({commit}, data) {
    commit(mutator.SET_NEW_TFS_PROJECT, data)
  },

  // Flash message
  [action.OPEN_FLASH_MESSAGE]({commit}, {message, title, type}) {
    commit(mutator.SET_FLASH_MESSAGE, {title, message, type})
  },
  [action.CLOSE_FLASH_MESSAGE]({commit}, flashMessageId) {
    commit(mutator.REMOVE_FLASH_MESSAGE, flashMessageId)
  },
}
