import {mutator} from '@store/constants'

export default {
  [mutator.SET_PROFILE_TIMELINE](state, data) {
    state.profileTimeline = data
  },
  [mutator.SET_SUMMARY](state, data) {
    state.summary = data
  },
}
