import {get} from '@store/constants'
import {createStore, mapGetters} from 'vuex'
import getters from '@store/getters'
import mockState from '@store/__mocks__/state'
import actions from '@store/__mocks__/actions'

import onlineState from '@store/modules/online/state'
import onlineGetters from '@store/modules/online/getters'

import socialState from '@store/modules/social/state'
import socialGetters from '@store/modules/social/getters'

export const createNewStore = (newState) => {
  return createStore({
    modules: {
      online: {
        namespaced: true,
        getters: onlineGetters,
        state: onlineState,
      },
      social: {
        namespaced: true,
        getters: socialGetters,
        state: socialState,
      },
    },
    state: {...mockState, ...newState},
    getters,
    actions,
    dispatch: jest.fn(),
  })
}

export const mockmixin = {
  computed: {
    ...mapGetters({platformLanguage: get.PLATFORM_LANGUAGE}),
  },
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
