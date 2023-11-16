import {get} from '@store/constants'

export default {
  [get.PRESET_GROUPS](state) {
    return state.groups.sort(
      (a, b) => new Date(b.created_at) - new Date(a.created_at)
    )
  },

  [get.NEW_GROUP_ID](state) {
    return state.newGroup.id
  },
}
