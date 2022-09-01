import axios from 'axios'
import CSRF_TOKEN from '../csrf_token'

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
  },

  async getWorkspaces() {
    return fetch('get', '/api/workspaces/')
  },

  async getLoggedUser() {
    return fetch('get', '/api/logged_in_user')
  },

  async createWorkspace(workspace) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch('post', '/api/workspace/create/', workspace, config)
  },

  async createNewProject(newProject) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch('post', '/api/project/create/', newProject, config)
  },
}
