import {createStore} from 'vuex'
import getters from '@store/getters'
import onlineGetters from '@store/modules/online/getters'
import onlineState from '@store/modules/online/state'
import mockState from '@store/__mocks__/state'
import actions from '@store/__mocks__/actions'

export const createNewStore = (newState) => {
  return createStore({
    modules: {
      online: {
        namespaced: true,
        getters: onlineGetters,
        state: onlineState,
      },
    },
    state: {...mockState, ...newState},
    getters,
    actions,
    dispatch: jest.fn(),
  })
}

export const mockmixin = {
  methods: {
    togglePageScroll(isOpen) {
      if (isOpen) {
        document.body.classList.add('overflow-hidden')
      } else {
        document.body.classList.remove('overflow-hidden')
      }
    },
  },
}
