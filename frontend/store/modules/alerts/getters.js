import {get} from '@store/constants'

export default {
  [get.ALERTS](state) {
    return state.alerts
  },
  [get.SET_ALERT_STEP](state) {
    return state.newAlert.step
  },
}
