import api from '@api/api'
import { action, mutator } from '@store/constants'

export default {
    async [action.LOGOUT]({ commit }) {
        commit(mutator.SET_LOADING, true)
        try {
            await api.logout()
            window.location.href = 'accounts/login'
        } catch (e) {
            console.log(e)
        } finally {
            commit(mutator.SET_LOADING, false)
        }
    },
    async [action.GET_PROJECTS]({ commit }) {
        commit(mutator.SET_LOADING, true)
        try {
            const projects = await api.getProjects()
            commit(mutator.SET_PROJECTS, projects)
        } catch (e) {
            console.log(e)
        } finally {
            commit(mutator.SET_LOADING, false)
        }
    },
    async [action.CREATE_WORKSPACE]({ commit }, workspace) {
        commit(mutator.SET_LOADING, true)
        try {
            await api.createWorkspace(workspace)
        } catch (e) {
            console.log(e)
        } finally {
            commit(mutator.SET_LOADING, false)
        }
    }
}
