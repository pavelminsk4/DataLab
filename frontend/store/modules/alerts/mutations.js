import {mutator} from '@store/constants'
import {newAlert} from './state'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_NEW_ALERT](state, data) {
    if (data) {
      state.newAlert = {...state.newAlert, ...data}
    } else {
      state.newAlert = newAlert
    }
  },

  [mutator.SET_ALERTS](state, data) {
    state.alerts = data
  },
}
