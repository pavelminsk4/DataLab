import {get} from '@store/constants'

export default {
  [get.LOADING](state) {
    return state.loading
  },
}
