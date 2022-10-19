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

  async getCountries() {
    return fetch('get', '/api/countries')
  },

  async getLanguages() {
    return fetch('get', '/api/speeches')
  },

  async getSources() {
    return fetch('get', '/api/sources')
  },

  async getAuthors() {
    return fetch('get', '/api/authors')
  },

  async getListOfDisplayedWidgets(projectId) {
    return fetch('get', `/api/projects/${projectId}/widgets_list`)
  },

  async getSummaryWidget(projectId) {
    return fetch('get', `/api/widgets/summary_widget/${projectId}`)
  },

  async getVolumeWidget(projectId) {
    return fetch('get', `/api/widgets/volume_widget/${projectId}`)
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

  async postSearch(request) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch('post', '/api/search', request, config)
  },

  async updateWorkspace({workspaceId, data}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch('put', `/api/workspace/update/${workspaceId}/`, data, config)
  },

  async updateAvailableWidgets({projectId, data}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch(
      'put',
      `/api/projects/${projectId}/widgets_list/update`,
      data,
      config
    )
  },
}
