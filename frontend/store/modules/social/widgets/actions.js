import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const summary = await api.social.getSummaryWidget(projectId, widgetId)
      commit(mutator.SET_SUMMARY_WIDGET, summary)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      const clippingFeedContent = await api.social.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_WIDGET](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const volume = await api.social.getContentVolumeWidget({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_CONTENT_VOLUME_WIDGET, volume)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_GENDER_VOLUME_WIDGET](
    {commit},
    {projectId, widgetId, value}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getGenderVolumeWidget(
        projectId,
        widgetId,
        value
      )
      commit(mutator.SET_GENDER_VOLUME_WIDGET, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  // Top
  async [action.GET_TOP_LOCATIONS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topLocation = await api.social.getTopLocationsWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_LOCATIONS_WIDGET, topLocation)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topLanguages = await api.social.getTopLanguagesWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, topLanguages)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topAuthors = await api.social.getTopAuthorsWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_AUTHORS_WIDGET, topAuthors)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_KEYWORDS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topKeywords = await api.social.getTopKeywords({projectId, widgetId})
      commit(mutator.SET_TOP_KEYWORDS_WIDGET, topKeywords)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topKeywords = await api.social.getTopKeywordsByCountry({
        projectId,
        widgetId,
      })
      commit(mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET, topKeywords)
    } catch (error) {
      return error
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_TOP_SHARING_SOURCES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topSharingSources = await api.social.getTopSharingSources({
        projectId,
        widgetId,
      })
      commit(mutator.SET_TOP_SHARING_SOURCES, topSharingSources)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_OVERALL_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getOverallTopAuthors({
        projectId,
        widgetId,
      })
      commit(mutator.SET_OVERALL_TOP_AUTHORS, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_AUTHORS_BY_GENDER]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getTopAuthorsByGender({
        projectId,
        widgetId,
      })
      commit(mutator.SET_TOP_AUTHORS_BY_GENDER, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  // Content Volume
  async [action.GET_CONTENT_VOLUME_TOP_LOCATIONS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopCountries =
        await api.social.getContentVolumeTopLocations({
          projectId,
          value,
          widgetId,
        })
      commit(
        mutator.SET_CONTENT_VOLUME_TOP_LOCATIONS,
        contentVolumeTopCountries
      )
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopAuthors =
        await api.social.getContentVolumeTopAuthors({
          projectId,
          value,
          widgetId,
        })
      commit(mutator.SET_CONTENT_VOLUME_TOP_AUTHORS, contentVolumeTopAuthors)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_TOP_LANGUAGES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopLanguages =
        await api.social.getContentVolumeTopLanguages({
          projectId,
          value,
          widgetId,
        })
      commit(
        mutator.SET_CONTENT_VOLUME_TOP_LANGUAGES,
        contentVolumeTopLanguages
      )
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_AUTHORS_BY_LANGUAGE]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getAuthorsByLanguage({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_LANGUAGE, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_LOCATION]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getAuthorsByLocation({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_LOCATION, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_SENTIMENT]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getAuthorsBySentiment({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_SENTIMENT, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_AUTHORS_BY_GENDER]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getAuthorsByGender({
        projectId,
        widgetId,
      })
      commit(mutator.SET_AUTHORS_BY_GENDER, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  // Sentiment
  async [action.GET_SENTIMENT_TOP_LOCATIONS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const sentimentTopCountries = await api.social.getSentimentTopLocations(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_LOCATIONS, sentimentTopCountries)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_TOP_LANGUAGES]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const sentimentTopLanguages = await api.social.getSentimentTopLanguages(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_LANGUAGES, sentimentTopLanguages)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_TOP_AUTHORS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const sentimentTopAuthors = await api.social.getSentimentTopAuthors(
        projectId,
        widgetId
      )
      commit(mutator.SET_SENTIMENT_TOP_AUTHORS, sentimentTopAuthors)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_FOR_PERIOD](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const sentimentForPeriod = await api.social.getSentimentForPeriod({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_FOR_PERIOD, sentimentForPeriod)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_DIAGRAM]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getSentimentDiagram({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_DIAGRAM, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_NUMBER_OF_RESULT](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getSentimentNumberOfResult({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_NUMBER_OF_RESULT, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_TOP_KEYWORDS]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getSentimentTopKeywords({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_TOP_KEYWORDS, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_SENTIMENT_BY_GENDER]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const data = await api.social.getSentimentByGender({
        projectId,
        widgetId,
      })
      commit(mutator.SET_SENTIMENT_BY_GENDER, data)
    } catch (e) {
      console.error(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
}
