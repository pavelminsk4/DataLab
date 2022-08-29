import { mutator } from '@store/constants'

export default {
    [mutator.SET_LOADING](state, loading) {
        state.loading = loading
    },

    [mutator.SET_PROJECTS](state, projects) {
        state.projects = projects
    },

    [mutator.SET_WORKSPACES](state, workspaces) {
        state.workspaces = workspaces
    }
}
