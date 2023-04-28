import {createStore} from 'vuex'
import state from '@store/state'
import actions from '@store/actions'
import mutations from '@store/mutations'
import getters from '@store/getters'

import social from '@store/modules/social'
import alerts from '@store/modules/alerts'

const store = createStore({
  state() {
    return {
      ...state,
    }
  },
  mutations: {
    ...mutations,
  },
  actions: {
    ...actions,
  },
  getters: {
    ...getters,
  },
  modules: {
    social,
    alerts,
  },
})

export default store
