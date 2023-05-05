import {createStore} from 'vuex'
import getters from '@store/getters'
import state from '@store/state'

export const createNewStore = () => {
  return createStore({
    state,
    getters,
    dispatch: jest.fn(),
  })
}
