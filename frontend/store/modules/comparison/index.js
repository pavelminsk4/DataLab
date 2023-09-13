import state from './state'
import actions from './actions'
import getters from './getters'
import mutations from './mutations'
import widgets from './widgets'

export default {
  namespaced: true,
  state,
  actions,
  getters,
  mutations,
  modules: {
    widgets,
  },
}
