import {get} from '@store/constants'
import {createStore, mapGetters} from 'vuex'
import getters from '@store/getters'
import mockState from '@store/__mocks__/state'
import actions from '@store/__mocks__/actions'

import onlineState from '@store/modules/online/state'
import onlineGetters from '@store/modules/online/getters'

import socialState from '@store/modules/social/state'
import socialGetters from '@store/modules/social/getters'

import accountAnalysisState from '@store/modules/account-analysis/state'
import accountAnalysisGetters from '@store/modules/account-analysis/getters'

export const createNewStore = (newState) => {
  return createStore({
    modules: {
      online: {
        namespaced: true,
        actions,
        getters: onlineGetters,
        state: onlineState,
      },
      social: {
        namespaced: true,
        actions,
        getters: socialGetters,
        state: socialState,
      },
      accountAnalysis: {
        namespaced: true,
        actions,
        getters: accountAnalysisGetters,
        state: accountAnalysisState,
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
