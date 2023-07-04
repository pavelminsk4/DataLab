import state from './state'
import actions from './actions'
import mutations from './mutations'
import widgets from './widgets'

export default {
  namespaced: true,
  state,
  actions,
  mutations,
  modules: {
    widgets,
  },
}
