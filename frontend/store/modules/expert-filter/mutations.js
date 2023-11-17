import {mutator} from '@store/constants'

export default {
  [mutator.SET_LOADING](state, loading) {
    state.loading = loading
  },

  [mutator.SET_PRESETS_GROUPS](state, groups) {
    state.groups = groups
  },
  [mutator.SET_NEW_PRESETS_GROUP](state, data) {
    state.newGroup = {...data}
  },

  [mutator.SET_PRESETS](state, presets) {
    state.presets = presets
  },
  [mutator.SET_NEW_PRESET](state, data) {
    state.newPreset = {...data}
  },
}
