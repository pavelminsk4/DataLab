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
  [mutator.SET_TOP_LOCATIONS_WIDGET](state, locations) {
    state.topLocations = locations
  },
  [mutator.SET_TOP_LANGUAGES_WIDGET](state, languages) {
    state.topLanguages = languages
  },
  [mutator.SET_TOP_AUTHORS_WIDGET](state, authors) {
    state.topAuthors = authors
  },

  [mutator.SET_CONTENT_VOLUME_TOP_LOCATIONS](state, data) {
    state.contentVolumeTopLocations = data
  },
  [mutator.SET_CONTENT_VOLUME_TOP_AUTHORS](state, data) {
    state.contentVolumeTopAuthors = data
  },
  [mutator.SET_CONTENT_VOLUME_TOP_LANGUAGES](state, data) {
    state.contentVolumeTopLanguages = data
  },
}
