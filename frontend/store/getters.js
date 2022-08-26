import { get } from '@store/constants'

export default {
    [get.LOADING](state) {
        return state.loading
    },
    [get.PROJECTS](state) {
        return state.projects
    }
}
