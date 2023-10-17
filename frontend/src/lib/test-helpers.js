import {createStore} from 'vuex'
import getters from '@store/getters'
import mockState from '@store/__mocks__/state'
import actions from '@store/__mocks__/actions'

export const createNewStore = (newState) => {
  return createStore({
    state: {...mockState, ...newState},
    getters,
    actions,
    dispatch: jest.fn(),
  })
}
