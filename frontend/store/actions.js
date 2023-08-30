import api from '@api/api'
import {action, mutator} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

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

  async [action.GET_WORKSPACES]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const workspaces = await api.getWorkspaces()
      commit(mutator.SET_WORKSPACES, workspaces)
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

  async [action.GET_COUNTRIES]({commit}, word) {
    try {
      const countries = await api.getCountries(capitalizeFirstLetter(word))
      commit(mutator.SET_COUNTRIES, countries)
      return countries
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_LANGUAGES]({commit}, word) {
    try {
      const languages = await api.getLanguages(capitalizeFirstLetter(word))
      commit(mutator.SET_LANGUAGES, languages)
      return languages
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_SOURCES]({commit}, word) {
    try {
      const sources = await api.getSources(word)
      commit(mutator.SET_SOURCES, sources)
      return sources
    } catch (error) {
      console.error(error)
      return error
    }
  },

  async [action.GET_AUTHORS]({commit}, word) {
    try {
      const authors = await api.getAuthors(word)
      commit(mutator.SET_AUTHORS, authors)
      return authors
    } catch (error) {
      console.error(error)
      return error
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

  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const summary = await api.getSummaryWidget(projectId, widgetId)
      commit(mutator.SET_SUMMARY_WIDGET, summary)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_VOLUME_WIDGET]({commit}, {projectId, value, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const volume = await api.getVolumeWidget({projectId, value, widgetId})
      commit(mutator.SET_VOLUME_WIDGET, volume)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_AVAILABLE_WIDGETS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const availableWidgets = await api.getListOfDisplayedWidgets(projectId)
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      return availableWidgets
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
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true})
    try {
      const clippingFeedContent = await api.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
    }
  },

  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topAuthors = await api.getTopAuthors(projectId, widgetId)
      commit(mutator.SET_TOP_AUTHORS_WIDGET, topAuthors)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_SHARING_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topSharingSources = await api.getTopSharingSourcesWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_SHARING_SOURCES, topSharingSources)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_BRANDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topBrands = await api.getTopBrands(projectId, widgetId)
      commit(mutator.SET_TOP_BRANDS_WIDGET, topBrands)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_COUNTRIES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topCountries = await api.getTopCountries(projectId, widgetId)
      commit(mutator.SET_TOP_COUNTRIES_WIDGET, topCountries)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topLanguages = await api.getTopLanguages(projectId, widgetId)
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, topLanguages)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentTopSources = await api.getSentimentTopSources(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_SOURCES, sentimentTopSources)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_TOP_COUNTRIES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentTopCountries = await api.getSentimentTopCountries(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_COUNTRIES, sentimentTopCountries)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_TOP_LANGUAGES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentTopLanguages = await api.getSentimentTopLanguages(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_LANGUAGES, sentimentTopLanguages)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentTopAuthors = await api.getSentimentTopAuthors(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_AUTHORS, sentimentTopAuthors)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_FOR_PERIOD](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentForPeriod = await api.getSentimentForPeriod({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_FOR_PERIOD, sentimentForPeriod)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_LANGUAGES_BY_COUNTRY](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const languagesByCountry = await api.getLanguagesByCountry({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_LANGUAGES_BY_COUNTRY, languagesByCountry)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_SOURCES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const contentVolumeTopSources = await api.getContentVolumeTop10Sources({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_CONTENT_VOLUME_TOP_SOURCES, contentVolumeTopSources)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const contentVolumeTopAuthors = await api.getContentVolumeTop10Authors({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_CONTENT_VOLUME_TOP_AUTHORS, contentVolumeTopAuthors)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_COUNTRIES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
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
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
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

  async [action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentTopKeywords = await api.getSentimentTopKeywordsWidget({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_TOP_KEYWORDS_WIDGET, sentimentTopKeywords)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_KEYWORDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topKeywords = await api.getTopKeywordsWidget({projectId, widgetId})
      commit(mutator.SET_TOP_KEYWORDS_WIDGET, topKeywords)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const topKeywords = await api.getTopKeywordsByCountryWidget({
        projectId,
        widgetId,
      })
      commit(mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET, topKeywords)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_AUTHORS_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const authorsByCountry = await api.getAuthorsByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_COUNTRY, authorsByCountry)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_DIAGRAM]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentDiagram = await api.getSentimentDiagram({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_DIAGRAM, sentimentDiagram)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SENTIMENT_NUMBER_OF_RESULT](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sentimentNumberOfResult = await api.getSentimentNumberOfResult({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_NUMBER_OF_RESULT, sentimentNumberOfResult)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SOURCES_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sourcesByLanguage = await api.getSourcesByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_LANGUAGE, sourcesByLanguage)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_SOURCES_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const sourcesByCountry = await api.getSourcesByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_COUNTRY, sourcesByCountry)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_OVERALL_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const overallTopSources = await api.getOverallTopSources({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_SOURCES, overallTopSources)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_OVERALL_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const overallTopAuthors = await api.getOverallTopAuthors({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_AUTHORS, overallTopAuthors)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_AUTHORS_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const authorsByLanguage = await api.getAuthorsByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_LANGUAGE, authorsByLanguage)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
    }
  },

  async [action.GET_AUTHORS_BY_SENTIMENT]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true})
    try {
      const authorsBySentiment = await api.getAuthorsBySentiment({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_SENTIMENT, authorsBySentiment)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false})
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

  async [action.GET_FILTER_AUTHORS]({commit}, projectId) {
    commit(mutator.SET_LOADING, true)
    try {
      const dimensionAuthors = await api.getFiltersAuthors(projectId)
      commit(mutator.SET_FILTERS_AUTHORS, dimensionAuthors)
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
      const dimensionLanguages = await api.getFiltersLanguages(projectId)
      commit(mutator.SET_FILTERS_LANGUAGES, dimensionLanguages)
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
      const dimensionCountries = await api.getFiltersCountries(projectId)
      commit(mutator.SET_FILTERS_COUNTRIES, dimensionCountries)
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
      const dimensionCountries = await api.getFiltersCountries(projectId)
      commit(mutator.SET_FILTERS_COUNTRIES, dimensionCountries)
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
      const dimensionSources = await api.getFiltersSources(projectId)
      commit(mutator.SET_FILTERS_SOURCES, dimensionSources)
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING, false)
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

  async [action.CREATE_WORKSPACE]({commit}, workspace) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createWorkspace(workspace)
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
      const response = await api.createNewProject(projectData)
      commit(mutator.SET_NEW_PROJECT_ID, response.id)
      await dispatch(action.GET_USER_INFORMATION)

      return response
    } catch (error) {
      console.error(error)
      return error
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
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false})
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

  async [action.UPDATE_WORKSPACE]({commit}, {workspaceId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const responseData = await api.updateWorkspace({workspaceId, data})
      commit(mutator.UPDATE_WORKSPACE, responseData)
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
      await api.updateProject({projectId, data})
      await dispatch(action.GET_WORKSPACES)
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
      const availableWidgets = await api.updateAvailableWidgets({
        projectId,
        data: widgetsList,
      })
      commit(mutator.SET_AVAILABLE_WIDGETS, availableWidgets)
      dispatch(action.GET_AVAILABLE_WIDGETS, projectId)
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
      const response = await api.postSearch(data)
      commit(mutator.SET_SEARCH_DATA, response.posts)
      commit(mutator.SET_NUMBER_OF_POSTS, response.num_posts)
      commit(mutator.SET_NUMBER_OF_PAGES, response.num_pages)
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
    } catch (error) {
      console.error(error)
      return error
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
    } catch (error) {
      console.error(error)
      return error
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
      await api.deleteWorkspace(workspaceId)
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
      await api.deleteProject(projectId)
      await dispatch(action.GET_WORKSPACES)
      await dispatch(action.GET_USER_INFORMATION)
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
      return api.downloadInstantReport(projectId)
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
      console.log(moduleType, 'lololo')
      commit(mutator.SET_INTERACTIVE_DATA_MODAL, value)
      switch (moduleType) {
        case 'Online':
          return await dispatch(action.POST_INTERACTIVE_WIDGETS, value)
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
}
