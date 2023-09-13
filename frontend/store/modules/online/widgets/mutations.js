import {mutator} from '@store/constants'

export default {
  [mutator.SET_SUMMARY_WIDGET](state, {widgetId, data}) {
    state.summary = {id: widgetId, data}
  },

  [mutator.SET_CLIPPING_FEED_CONTENT_WIDGET](state, {widgetId, data}) {
    state.clippingFeedContent = {id: widgetId, data}
  },

  [mutator.SET_VOLUME_WIDGET](state, {widgetId, data}) {
    state.volume = {id: widgetId, data}
  },

  [mutator.SET_TOP_AUTHORS_WIDGET](state, {widgetId, data}) {
    state.topAuthors = {id: widgetId, data}
  },

  [mutator.SET_TOP_BRANDS_WIDGET](state, {widgetId, data}) {
    state.topBrands = {id: widgetId, data}
  },

  [mutator.SET_TOP_COUNTRIES_WIDGET](state, {widgetId, data}) {
    state.topCountries = {id: widgetId, data}
  },

  [mutator.SET_TOP_LANGUAGES_WIDGET](state, {widgetId, data}) {
    state.topLanguages = {id: widgetId, data}
  },

  [mutator.SET_CONTENT_VOLUME_TOP_SOURCES](state, {widgetId, data}) {
    state.contentVolumeTopSources = {id: widgetId, data}
  },

  [mutator.SET_CONTENT_VOLUME_TOP_AUTHORS](state, {widgetId, data}) {
    state.contentVolumeTopAuthors = {id: widgetId, data}
  },

  [mutator.SET_CONTENT_VOLUME_TOP_COUNTRIES](state, {widgetId, data}) {
    state.contentVolumeTopCountries = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_TOP_SOURCES](state, {widgetId, data}) {
    state.sentimentTopSources = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_TOP_COUNTRIES](state, {widgetId, data}) {
    state.sentimentTopCountries = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_TOP_AUTHORS](state, {widgetId, data}) {
    state.sentimentTopAuthors = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_TOP_LANGUAGES](state, {widgetId, data}) {
    state.sentimentTopLanguages = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_FOR_PERIOD](state, {widgetId, data}) {
    state.sentimentForPeriod = {id: widgetId, data}
  },

  [mutator.SET_TOP_KEYWORDS_WIDGET](state, {widgetId, data}) {
    state.topKeywordsWidget = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_TOP_KEYWORDS_WIDGET](state, {widgetId, data}) {
    state.sentimentTopKeywordsWidget = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_NUMBER_OF_RESULT](state, {widgetId, data}) {
    state.sentimentNumberOfResult = {id: widgetId, data}
  },

  [mutator.SET_SENTIMENT_DIAGRAM](state, {widgetId, data}) {
    state.sentimentDiagram = {id: widgetId, data}
  },

  [mutator.SET_AUTHORS_BY_COUNTRY](state, {widgetId, data}) {
    state.authorsByCountry = {id: widgetId, data}
  },

  [mutator.SET_AUTHORS_BY_LANGUAGE](state, {widgetId, data}) {
    state.authorsByLanguage = {id: widgetId, data}
  },

  [mutator.SET_AUTHORS_BY_SENTIMENT](state, {widgetId, data}) {
    state.authorsBySentiment = {id: widgetId, data}
  },

  [mutator.SET_OVERALL_TOP_AUTHORS](state, {widgetId, data}) {
    state.overallTopAuthors = {id: widgetId, data}
  },

  [mutator.SET_OVERALL_TOP_SOURCES](state, {widgetId, data}) {
    state.overallTopSources = {id: widgetId, data}
  },

  [mutator.SET_SOURCES_BY_COUNTRY](state, {widgetId, data}) {
    state.sourcesByCountry = {id: widgetId, data}
  },

  [mutator.SET_SOURCES_BY_LANGUAGE](state, {widgetId, data}) {
    state.sourcesByLanguage = {id: widgetId, data}
  },

  [mutator.SET_TOP_SHARING_SOURCES](state, {widgetId, data}) {
    state.topSharingSources = {id: widgetId, data}
  },

  [mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](state, {widgetId, data}) {
    state.topKeywordsByCountryWidget = {id: widgetId, data}
  },

  [mutator.SET_LANGUAGES_BY_COUNTRY](state, {widgetId, data}) {
    state.languagesByCountry = {id: widgetId, data}
  },
}
