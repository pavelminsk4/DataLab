import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const summary = await api.online.getSummaryWidget(projectId, widgetId)
      commit(mutator.SET_SUMMARY_WIDGET, {widgetId, data: summary})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
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

  async [action.GET_VOLUME_WIDGET]({commit}, {projectId, value, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const volume = await api.online.getVolumeWidget({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_VOLUME_WIDGET, {widgetId, data: volume})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topAuthors = await api.online.getTopAuthors(projectId, widgetId)
      commit(mutator.SET_TOP_AUTHORS_WIDGET, {widgetId, data: topAuthors})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_BRANDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topBrands = await api.online.getTopBrands(projectId, widgetId)
      commit(mutator.SET_TOP_BRANDS_WIDGET, {widgetId, data: topBrands})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_COUNTRIES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topCountries = await api.online.getTopCountries(projectId, widgetId)
      commit(mutator.SET_TOP_COUNTRIES_WIDGET, {widgetId, data: topCountries})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const topLanguages = await api.online.getTopLanguages(projectId, widgetId)
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, {widgetId, data: topLanguages})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_SOURCES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const contentVolumeTopSources =
        await api.online.getContentVolumeTopSources({
          projectId,
          value,
          widgetId,
        })
      commit(mutator.SET_CONTENT_VOLUME_TOP_SOURCES, {
        widgetId,
        data: contentVolumeTopSources,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const contentVolumeTopAuthors =
        await api.online.getContentVolumeTopAuthors({
          projectId,
          value,
          widgetId,
        })
      commit(mutator.SET_CONTENT_VOLUME_TOP_AUTHORS, {
        widgetId,
        data: contentVolumeTopAuthors,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_COUNTRIES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const contentVolumeTopCountries =
        await api.online.getContentVolumeTopCountries({
          projectId,
          value,
          widgetId,
        })
      commit(mutator.SET_CONTENT_VOLUME_TOP_COUNTRIES, {
        widgetId,
        data: contentVolumeTopCountries,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const sentimentTopSources = await api.online.getSentimentTopSources(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_SOURCES, {
        widgetId,
        data: sentimentTopSources,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_TOP_COUNTRIES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const sentimentTopCountries = await api.online.getSentimentTopCountries(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_COUNTRIES, {
        widgetId,
        data: sentimentTopCountries,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const sentimentTopAuthors = await api.online.getSentimentTopAuthors(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_AUTHORS, {
        widgetId,
        data: sentimentTopAuthors,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_TOP_LANGUAGES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const sentimentTopLanguages = await api.online.getSentimentTopLanguages(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_LANGUAGES, {
        widgetId,
        data: sentimentTopLanguages,
      })
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_FOR_PERIOD](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSentimentForPeriod({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_FOR_PERIOD, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_KEYWORDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getTopKeywordsWidget({projectId, widgetId})
      commit(mutator.SET_TOP_KEYWORDS_WIDGET, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSentimentTopKeywordsWidget({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_TOP_KEYWORDS_WIDGET, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_NUMBER_OF_RESULT](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSentimentNumberOfResult({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_NUMBER_OF_RESULT, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SENTIMENT_DIAGRAM]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSentimentDiagram({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_DIAGRAM, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getAuthorsByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_COUNTRY, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getAuthorsByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_LANGUAGE, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_SENTIMENT]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getAuthorsBySentiment({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_SENTIMENT, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_OVERALL_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getOverallTopAuthors({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_AUTHORS, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_OVERALL_TOP_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getOverallTopSources({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_SOURCES, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SOURCES_BY_COUNTRY]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSourcesByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_COUNTRY, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_SOURCES_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getSourcesByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SOURCES_BY_LANGUAGE, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_SHARING_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getTopSharingSourcesWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_SHARING_SOURCES, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getTopKeywordsByCountryWidget({
        projectId,
        widgetId,
      })
      commit(mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },

  async [action.GET_LANGUAGES_BY_COUNTRY](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: true}, {root: true})
    try {
      const data = await api.online.getLanguagesByCountry({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_LANGUAGES_BY_COUNTRY, {widgetId, data})
    } catch (error) {
      console.error(error)
      return error
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {[widgetId]: false}, {root: true})
    }
  },
}
