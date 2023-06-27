import {mutator} from '@store/constants'

export default {
  [mutator.SET_SUMMARY_WIDGET](state, data) {
    state.summary = data
  },
  [mutator.SET_CLIPPING_FEED_CONTENT_WIDGET](state, data) {
    state.clippingFeedContent = data
  },
  [mutator.SET_CONTENT_VOLUME_WIDGET](state, data) {
    state.contentVolume = data
  },
  [mutator.SET_GENDER_VOLUME_WIDGET](state, data) {
    state.genderVolume = data
  },

  [mutator.SET_GENDER_BY_LOCATION](state, data) {
    state.genderByLocation = data
  },

  // Top
  [mutator.SET_TOP_LOCATIONS_WIDGET](state, locations) {
    state.topLocations = locations
  },
  [mutator.SET_TOP_LANGUAGES_WIDGET](state, languages) {
    state.topLanguages = languages
  },
  [mutator.SET_TOP_AUTHORS_WIDGET](state, authors) {
    state.topAuthors = authors
  },
  [mutator.SET_TOP_KEYWORDS_WIDGET](state, data) {
    state.topKeywords = data
  },
  [mutator.SET_TOP_KEYWORDS_BY_COUNTRY_WIDGET](state, data) {
    state.topKeywordsByCountry = data
  },
  [mutator.SET_TOP_SHARING_SOURCES](state, data) {
    state.topSharingSources = data
  },
  [mutator.SET_OVERALL_TOP_AUTHORS](state, data) {
    state.overallTopAuthors = data
  },
  [mutator.SET_TOP_AUTHORS_BY_GENDER](state, data) {
    state.topAuthorsByGender = data
  },

  // Content volume
  [mutator.SET_CONTENT_VOLUME_TOP_LOCATIONS](state, data) {
    state.contentVolumeTopLocations = data
  },
  [mutator.SET_CONTENT_VOLUME_TOP_AUTHORS](state, data) {
    state.contentVolumeTopAuthors = data
  },
  [mutator.SET_CONTENT_VOLUME_TOP_LANGUAGES](state, data) {
    state.contentVolumeTopLanguages = data
  },
  [mutator.SET_AUTHORS_BY_LANGUAGE](state, data) {
    state.authorsByLanguage = data
  },
  [mutator.SET_AUTHORS_BY_LOCATION](state, data) {
    state.authorsByLocation = data
  },
  [mutator.SET_AUTHORS_BY_SENTIMENT](state, data) {
    state.authorsBySentiment = data
  },
  [mutator.SET_AUTHORS_BY_GENDER](state, data) {
    state.authorsByGender = data
  },
  [mutator.SET_LANGUAGES_BY_LOCATION](state, data) {
    state.languagesByLocation = data
  },

  // Sentiment
  [mutator.SET_SENTIMENT_TOP_LOCATIONS](state, data) {
    state.sentimentTopLocations = data
  },
  [mutator.SET_SENTIMENT_TOP_LANGUAGES](state, data) {
    state.sentimentTopLanguages = data
  },
  [mutator.SET_SENTIMENT_TOP_AUTHORS](state, data) {
    state.sentimentTopAuthors = data
  },
  [mutator.SET_SENTIMENT_FOR_PERIOD](state, data) {
    state.sentimentForPeriod = data
  },
  [mutator.SET_SENTIMENT_DIAGRAM](state, data) {
    state.sentimentDiagram = data
  },
  [mutator.SET_SENTIMENT_NUMBER_OF_RESULT](state, data) {
    state.sentimentNumberOfResult = data
  },
  [mutator.SET_SENTIMENT_TOP_KEYWORDS](state, data) {
    state.sentimentTopKeywords = data
  },
  [mutator.SET_SENTIMENT_BY_GENDER](state, data) {
    state.sentimentByGender = data
  },
}
