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

  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const summary = await api.getSummaryWidget(projectId, widgetId)
      commit(mutator.SET_SUMMARY_WIDGET, summary)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_VOLUME_WIDGET]({commit}, {projectId, value, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const volume = await api.getVolumeWidget({projectId, value, widgetId})
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

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      const clippingFeedContent = await api.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topAuthors = await api.getTopAuthors(projectId, widgetId)
      commit(mutator.SET_TOP_AUTHORS_WIDGET, topAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_SHARING_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topSharingSources = await api.getTopSharingSourcesWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_SHARING_SOURCES, topSharingSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_BRANDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topBrands = await api.getTopBrands(projectId, widgetId)
      commit(mutator.SET_TOP_BRANDS_WIDGET, topBrands)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_COUNTRIES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topCountries = await api.getTopCountries(projectId, widgetId)
      commit(mutator.SET_TOP_COUNTRIES_WIDGET, topCountries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topLanguages = await api.getTopLanguages(projectId, widgetId)
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, topLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopSources = await api.getSentimentTopSources(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_SOURCES, sentimentTopSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_COUNTRIES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopCountries = await api.getSentimentTopCountries(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_COUNTRIES, sentimentTopCountries)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_LANGUAGES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopLanguages = await api.getSentimentTopLanguages(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_LANGUAGES, sentimentTopLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopAuthors = await api.getSentimentTopAuthors(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_AUTHORS, sentimentTopAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_FOR_PERIOD](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentForPeriod = await api.getSentimentForPeriod({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_FOR_PERIOD, sentimentForPeriod)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_SOURCES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopSources = await api.getContentVolumeTop10Sources({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_CONTENT_VOLUME_TOP_SOURCES, contentVolumeTopSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopAuthors = await api.getContentVolumeTop10Authors({
        projectId,
        value,
        widgetId,
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
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const contentVolumeTopCountries =
        await api.getContentVolumeTop10Countries({
          projectId,
          value,
          widgetId,
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

  async [action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentTopKeywords = await api.getSentimentTopKeywordsWidget({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_TOP_KEYWORDS_WIDGET, sentimentTopKeywords)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_TOP_KEYWORDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const topKeywords = await api.getTopKeywordsWidget({projectId, widgetId})
      commit(mutator.SET_TOP_KEYWORDS_WIDGET, topKeywords)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const authorsByCountry = await api.getAuthorsByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_COUNTRY, authorsByCountry)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_DIAGRAM]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentDiagram = await api.getSentimentDiagram({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_DIAGRAM, sentimentDiagram)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SENTIMENT_NUMBER_OF_RESULT](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const sentimentNumberOfResult = await api.getSentimentNumberOfResult({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_NUMBER_OF_RESULT, sentimentNumberOfResult)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOURCES_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sourcesByLanguage = await api.getSourcesByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_LANGUAGE, sourcesByLanguage)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SOURCES_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const sourcesByCountry = await api.getSourcesByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_COUNTRY, sourcesByCountry)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_OVERALL_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const overallTopSources = await api.getOverallTopSources({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_SOURCES, overallTopSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_OVERALL_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const overallTopAuthors = await api.getOverallTopAuthors({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_AUTHORS, overallTopAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const authorsByLanguage = await api.getAuthorsByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_LANGUAGE, authorsByLanguage)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_AUTHORS_BY_SENTIMENT]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const authorsBySentiment = await api.getAuthorsBySentiment({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_SENTIMENT, authorsBySentiment)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_SELECTED_DIMENSIONS]({commit}, selectedDimensions) {
    commit(mutator.SET_LOADING, true)
    try {
      commit(mutator.SET_SELECTED_DIMENSIONS, selectedDimensions)
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

  async [action.GET_DIMENSION_SOURCES]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionSources = await api.getDimensionSources(projectId)
      commit(mutator.SET_DIMENSION_SOURCES, dimensionSources)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_DIMENSIONS_OPTIONS]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await dispatch(action.GET_DIMENSION_AUTHORS, projectId)
      await dispatch(action.GET_DIMENSION_COUNTRIES, projectId)
      await dispatch(action.GET_DIMENSION_LANGUAGES, projectId)
      await dispatch(action.GET_DIMENSION_SOURCES, projectId)
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
      return response
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.CREATE_PROJECT]({commit, dispatch}, projectData) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createNewProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(action.GET_USER_INFORMATION)

      return response
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
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: data.projectId,
        widgetId: data.widgetId,
      })
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.CREATE_NEW_ALERT]({commit, dispatch}, {data, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createAlert(data)
      await dispatch(action.GET_ALERTS, projectId)
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

  async [action.CREATE_NEW_USER]({commit}, data) {
    commit(mutator.SET_LOADING, true)
    try {
      return await api.createUser(data)
    } catch (e) {
      console.log(e)
      return {
        ...e.response.data,
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

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.UPDATE_PROJECT]({dispatch, commit}, {projectId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateProject({projectId, data})
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
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
      const availableWidgets = await api.updateAvailableWidgets({
        projectId,
        data: widgetsList,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
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

  async [action.POST_DIMENSIONS_FOR_WIDGET](
    {commit},
    {projectId, widgetId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.postDimensionsForWidget({projectId, widgetId, data})
    } catch (e) {
      console.log(e)
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
      const response = await api.postInteractiveWidget({
        projectId,
        widgetId,
        data,
      })

      commit(mutator.SET_INTERACTIVE_DATA, response)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_CLIPPING_FEED_CONTENT](
    {commit, dispatch},
    {projectId, postId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      await api.deleteClippingFeedContentPost(projectId, postId)
      await dispatch(action.GET_CLIPPING_FEED_CONTENT_WIDGET, {
        projectId: projectId,
        widgetId: widgetId,
      })
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

  async [action.DELETE_WORKSPACE]({commit, dispatch}, workspaceId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteWorkspace(workspaceId)
      await dispatch(action.GET_WORKSPACES)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_PROJECT]({commit, dispatch}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
      await dispatch(action.GET_USER_INFORMATION)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.DELETE_ALERT]({commit, dispatch}, {alertId, projectId}) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteAlert(alertId)
      await dispatch(action.GET_ALERTS, projectId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_INSTANTLY_REPORT]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      return api.downloadInstantlyReport(projectId)
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
  async [action.GET_REGULAR_REPORTS]({commit}, departmentId) {
    commit(mutator.SET_LOADING, true)
    try {
      const regularReports = await api.getRegularReports(departmentId)
      commit(mutator.SET_REGULAR_REPORTS, regularReports)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_REGULAR_REPORT](
    {commit, dispatch},
    {departmentId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.createRegularReport(departmentId, data)
      await dispatch(action.GET_REGULAR_REPORTS, departmentId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_REGULAR_REPORT](
    {dispatch, commit},
    {departmentId, regularReportId, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.updateRegularReport(departmentId, regularReportId, data)
      await dispatch(action.GET_REGULAR_REPORTS, departmentId)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.DELETE_REGULAR_REPORT](
    {dispatch, commit},
    {departmentId, regularReportId}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      await api.deleteRegularReport(departmentId, regularReportId)
      await dispatch(action.GET_REGULAR_REPORTS, departmentId)
    } catch (e) {
      console.log(e)
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
}
