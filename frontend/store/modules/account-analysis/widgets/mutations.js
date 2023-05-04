import {mutator} from '@store/constants'

export default {
  [mutator.SET_PROFILE_TIMELINE](state, data) {
    state.profileTimeline = data
  },
}
