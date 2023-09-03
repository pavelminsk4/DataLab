import {mutator} from '@store/constants'

export default {
  [mutator.SET_SUMMARY_WIDGET](state, {widgetId, data}) {
    state.summary = {id: widgetId, data}
  },
  [mutator.SET_CLIPPING_FEED_CONTENT_WIDGET](state, {widgetId, data}) {
    state.clippingFeedContent = {id: widgetId, data}
  },
  [mutator.SET_CONTENT_VOLUME_WIDGET](state, {widgetId, data}) {
    state.contentVolume = {id: widgetId, data}
  },
  [mutator.SET_GENDER_VOLUME_WIDGET](state, {widgetId, data}) {
    state.genderVolume = {id: widgetId, data}
  },

  [mutator.SET_GENDER_BY_LOCATION](state, {widgetId, data}) {
    state.genderByLocation = {id: widgetId, data}
  },

  // Top
  [mutator.SET_TOP_LOCATIONS_WIDGET](state, {widgetId, data}) {
    state.topLocations = {id: widgetId, data}
  },
  [mutator.SET_TOP_LANGUAGES_WIDGET](state, {widgetId, data}) {
    state.topLanguages = {id: widgetId, data}
  },
  [mutator.SET_TOP_AUTHORS_WIDGET](state, {widgetId, data}) {
    state.topAuthors = {id: widgetId, data}
  },
  [mutator.SET_TOP_KEYWORDS_WIDGET](state, {widgetId, data}) {
    state.topKeywords = {id: widgetId, data}
  },
  [mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](state, {widgetId, data}) {
    state.topKeywordsByCountry = {id: widgetId, data}
  },
  [mutator.SET_TOP_SHARING_SOURCES](state, {widgetId, data}) {
    state.topSharingSources = {id: widgetId, data}
  },
  [mutator.SET_OVERALL_TOP_AUTHORS](state, {widgetId, data}) {
    state.overallTopAuthors = {id: widgetId, data}
  },
  [mutator.SET_TOP_AUTHORS_BY_GENDER](state, {widgetId, data}) {
    state.topAuthorsByGender = {id: widgetId, data}
  },

  // Content volume
  [mutator.SET_CONTENT_VOLUME_TOP_LOCATIONS](state, {widgetId, data}) {
    state.contentVolumeTopLocations = {id: widgetId, data}
  },
  [mutator.SET_CONTENT_VOLUME_TOP_AUTHORS](state, {widgetId, data}) {
    state.contentVolumeTopAuthors = {id: widgetId, data}
  },
  [mutator.SET_CONTENT_VOLUME_TOP_LANGUAGES](state, {widgetId, data}) {
    state.contentVolumeTopLanguages = {id: widgetId, data}
  },
  [mutator.SET_AUTHORS_BY_LANGUAGE](state, {widgetId, data}) {
    state.authorsByLanguage = {id: widgetId, data}
  },
  [mutator.SET_AUTHORS_BY_LOCATION](state, {widgetId, data}) {
    state.authorsByLocation = {id: widgetId, data}
  },
  [mutator.SET_AUTHORS_BY_SENTIMENT](state, {widgetId, data}) {
    state.authorsBySentiment = {id: widgetId, data}
  },
  [mutator.SET_AUTHORS_BY_GENDER](state, {widgetId, data}) {
    state.authorsByGender = {id: widgetId, data}
  },
  [mutator.SET_LANGUAGES_BY_LOCATION](state, {widgetId, data}) {
    state.languagesByLocation = {id: widgetId, data}
  },

  // Sentiment
  [mutator.SET_SENTIMENT_TOP_LOCATIONS](state, {widgetId, data}) {
    state.sentimentTopLocations = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_TOP_LANGUAGES](state, {widgetId, data}) {
    state.sentimentTopLanguages = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_TOP_AUTHORS](state, {widgetId, data}) {
    state.sentimentTopAuthors = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_FOR_PERIOD](state, {widgetId, data}) {
    state.sentimentForPeriod = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_DIAGRAM](state, {widgetId, data}) {
    state.sentimentDiagram = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_NUMBER_OF_RESULT](state, {widgetId, data}) {
    state.sentimentNumberOfResult = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_TOP_KEYWORDS](state, {widgetId, data}) {
    state.sentimentTopKeywords = {id: widgetId, data}
  },
  [mutator.SET_SENTIMENT_BY_GENDER](state, {widgetId, data}) {
    state.sentimentByGender = {id: widgetId, data}
  },
}
