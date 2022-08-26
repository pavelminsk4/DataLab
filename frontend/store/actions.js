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
    }
}
