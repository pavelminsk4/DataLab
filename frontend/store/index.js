import { createStore } from 'vuex'
import state from './state'
import actions from './actions'
import mutations from './mutations'
import getters from './getters'

const store = createStore({
    state() {
        return {
            ...state
        }
    },
    mutations: {
        ...mutations
    },
    actions: {
        ...actions
    },
    getters: {
        ...getters
    }
})

export default store
