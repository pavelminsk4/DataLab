import {createStore} from 'vuex'
import getters from '@store/getters'
import mockState from '@store/__mocks__/state'

export const createNewStore = (newState) => {
  return createStore({
    state: {...mockState, ...newState},
    getters,
    dispatch: jest.fn(),
  })
}
