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

  async [action.GET_COUNTRIES]({commit}, word) {
    commit(mutator.SET_LOADING, true)
    try {
      const countries = await api.getCountries(word)
      commit(mutator.SET_COUNTRIES, countries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_LANGUAGES]({commit}, word) {
    commit(mutator.SET_LOADING, true)
    try {
      const languages = await api.getLanguages(word)
      commit(mutator.SET_LANGUAGES, languages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOURCES]({commit}, word) {
    commit(mutator.SET_LOADING, true)
    try {
      const sources = await api.getSources(word)
      commit(mutator.SET_SOURCES, sources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS]({commit}, word) {
    commit(mutator.SET_LOADING, true)
    try {
      const authors = await api.getAuthors(word)
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
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      const clippingFeedContent = await api.getClippingFeedContentWidget(
        projectId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const topAuthors = await api.getTopAuthors(projectId)
      commit(mutator.SET_TOP_AUTHORS_WIDGET, topAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_BRANDS_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const topBrands = await api.getTopBrands(projectId)
      commit(mutator.SET_TOP_BRANDS_WIDGET, topBrands)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_COUNTRIES_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const topCountries = await api.getTopCountries(projectId)
      commit(mutator.SET_TOP_COUNTRIES_WIDGET, topCountries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const topLanguages = await api.getTopLanguages(projectId)
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, topLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_SOURCES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopSources = await api.getSentimentTopSources(projectId)
      commit(mutator.SET_SENTIMENT_TOP_SOURCES, sentimentTopSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_COUNTRIES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopCountries = await api.getSentimentTopCountries(
        projectId
      )
      commit(mutator.SET_SENTIMENT_TOP_COUNTRIES, sentimentTopCountries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_LANGUAGES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopLanguages = await api.getSentimentTopLanguages(
        projectId
      )
      commit(mutator.SET_SENTIMENT_TOP_LANGUAGES, sentimentTopLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopAuthors = await api.getSentimentTopAuthors(projectId)
      commit(mutator.SET_SENTIMENT_TOP_AUTHORS, sentimentTopAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_FOR_PERIOD]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentForPeriod = await api.getSentimentForPeriod({
        projectId,
        value,
      })
      commit(mutator.SET_SENTIMENT_FOR_PERIOD, sentimentForPeriod)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_SOURCES]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopSources = await api.getContentVolumeTop10Sources({
        projectId,
        value,
      })
      commit(mutator.SET_CONTENT_VOLUME_TOP_SOURCES, contentVolumeTopSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS]({commit}, {projectId, value}) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopAuthors = await api.getContentVolumeTop10Authors({
        projectId,
        value,
      })
      commit(mutator.SET_CONTENT_VOLUME_TOP_AUTHORS, contentVolumeTopAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_COUNTRIES](
    {commit},
    {projectId, value}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopCountries =
        await api.getContentVolumeTop10Countries({
          projectId,
          value,
        })
      commit(
        mutator.SET_CONTENT_VOLUME_TOP_COUNTRIES,
        contentVolumeTopCountries
      )
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_DIMENSIONS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensions = await api.getDimensions()
      commit(mutator.SET_DIMENSIONS, dimensions)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TEMPLATES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const templates = await api.getTemplates()
      commit(mutator.SET_TEMPLATES, templates)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SELECTED_DIMENSIONS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const selectedDimensions = await api.getSelectedDimensions(projectId)
      commit(mutator.SET_SELECTED_DIMENSIONS, selectedDimensions)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_DIMENSION_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionAuthors = await api.getDimensionAuthors(projectId)
      commit(mutator.SET_DIMENSION_AUTHORS, dimensionAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_DIMENSION_LANGUAGES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionLanguages = await api.getDimensionLanguages(projectId)
      commit(mutator.SET_DIMENSION_LANGUAGES, dimensionLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_DIMENSION_COUNTRIES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionCountries = await api.getDimensionCountries(projectId)
      commit(mutator.SET_DIMENSION_COUNTRIES, dimensionCountries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_ALERTS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const alerts = await api.getAlerts(projectId)
      commit(mutator.SET_ALERTS, alerts)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_REGULAR_REPORTS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const regularReports = await api.getRegularReports(projectId)
      commit(mutator.SET_REGULAR_REPORTS, regularReports)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_COMPANY_USERS]({commit}, companyId) {
    commit(mutator.SET_LOADING, true)
    try {
      const companyUsers = await api.getCompanyUsers(companyId)
      commit(mutator.SET_COMPANY_USERS, companyUsers)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createWorkspace(workspace)
      commit(mutator.SET_NEW_WORKSPACE_ID, response.id)
      commit(mutator.SET_NEW_PROJECT_ID, response.projects[0].id)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createNewProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({commit, dispatch}, data) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      await api.createClippingFeedContent(data.posts)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, data.projectId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.CREATE_NEW_ALERT]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createAlert(data)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_ALERT]({commit, dispatch}, {data, alertId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateAlert({data, alertId})
      await dispatch(action.GET_ALERTS, data.project)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_REGULAR_REPORT]({commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createRegularReport({projectId, data})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_NEW_USER]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createUser(data)
    } catch (e) {
      console.log(e)
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
    } catch (e) {
      console.log(e)
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
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_REGULAR_REPORT](
    {dispatch, commit},
    {projectId, regularReportId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateRegularReport({projectId, regularReportId, data})
      await dispatch(action.GET_REGULAR_REPORTS, projectId)
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
      commit(mutator.SET_SEARCH_DATA, response.posts)
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts)
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.POST_DIMENSIONS]({commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.postDimensions({projectId, data})
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_CLIPPING_FEED_CONTENT](
    {commit, dispatch},
    {projectId, postId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      await api.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, projectId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.DELETE_USER_FROM_COMPANY](
    {commit, dispatch},
    {userId, currentUserId}
  ) {
    console.log(userId, currentUserId)
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteUserFromCompany(userId)
      await dispatch(action.GET_COMPANY_USERS, currentUserId)
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

  async [action.CLEAR_STATE]({commit}) {
    commit(mutator.RESET_STATE)
  },

  async [action.CLEAR_SEARCH_LIST]({commit}) {
    commit(mutator.RESET_SEARCH_LIST)
  },
}
