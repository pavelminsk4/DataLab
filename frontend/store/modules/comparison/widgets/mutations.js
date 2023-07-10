import {mutator} from '@store/constants'

export default {
  [mutator.SET_SUMMARY_WIDGETS](state, data) {
    state.summary.widgets = data
  },
  [mutator.SET_SUMMARY_WIDGETS_LOADING](state, loading) {
    state.summary.isLoading = loading
  },

  [mutator.SET_SENTIMENT_WIDGETS](state, data) {
    state.sentiment.widgets = data
  },
  [mutator.SET_SENTIMENT_WIDGETS_LOADING](state, loading) {
    state.sentiment.isLoading = loading
  },
}
