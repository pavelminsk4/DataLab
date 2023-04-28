import {mutator} from '@store/constants'

const initialAlert = {
  step: 1,
  title: '',
  description: '',
  user: [],
  department: null,
  creator: null,
  alert_condition: '',
  triggered_on_every_n_new_posts: '',
  how_many_posts_to_send: '',
}

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },
  // Alerts
  [mutator.SET_NEW_ALERT](state, data) {
    if (data) {
      state.newAlert = {...state.newAlert, ...data}
    } else {
      state.newAlert = initialAlert
    }
  },

  [mutator.SET_ALERTS](state, data) {
    state.alerts = data
  },
}
