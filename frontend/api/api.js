import axios from 'axios'

const endpoint = (resource) => `${resource}`

const fetch = async (action, resource, payload = null, config = null) => {
    const response = await axios[action](endpoint(resource), payload, config)
    return response.data
}

export default {
    async logout() {
        return fetch('get', '/accounts/logout/')
    },

    async getProjects() {
        return fetch('get', '/api/projects/')
    }
}
