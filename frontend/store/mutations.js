import { mutator } from './constants'

export default {
    [mutator.SET_LOADING](state, loading) {
        state.loading = loading
    }
}
