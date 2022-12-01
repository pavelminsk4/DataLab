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

  async getCountries(word) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch('get', `/api/countries/countries?search=${word}`, config)
  },

  async getLanguages(word) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch('get', `/api/speeches/speeches?search=${word}`, config)
  },

  async getSources(word) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch('post', '/api/sources', word, config)
  },

  async getAuthors(word) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch('post', '/api/authors', word, config)
  },

  async getListOfDisplayedWidgets(projectId) {
    return fetch('get', `/api/projects/${projectId}/widgets_list`)
  },

  async getSummaryWidget(projectId) {
    return fetch('get', `/api/widgets/summary_widget/${projectId}`)
  },

  async getClippingFeedContentWidget(projectId) {
    return fetch(
      'get',
      `/api/widgets/clipping_feed_content_widget/${projectId}`
    )
  },

  async getVolumeWidget({projectId, value}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch(
      'put',
      `/api/widgets/volume_widget/${projectId}`,
      value,
      config
    )
  },

  async getTopAuthors(projectId) {
    return fetch('get', `/api/widgets/top_10_authors_by_volume/${projectId}`)
  },

  async getDimensions() {
    return fetch('get', '/api/dimensions/')
  },

  async getTemplates() {
    return fetch('get', '/api/templates/')
  },

  async getSelectedDimensions(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimensions`)
  },

  async getDimensionAuthors(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_authors`)
  },

  async getDimensionLanguages(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_languages`)
  },

  async getDimensionCountries(projectId) {
    return fetch('get', `/api/projects/${projectId}/dimension_countries`)
  },

  async getAlerts(projectId) {
    return fetch('get', `/api/projects/${projectId}/alerts/`)
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
    return fetch('post', '/api/projects/', newProject, config)
  },

  async createClippingFeedContent(data) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch(
      'post',
      '/api/clipping_feed_content_widget/create',
      data,
      config
    )
  },

  async createAlert(data) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch('post', '/api/alerts/', data, config)
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

  async postDimensions({projectId, data}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }

    return fetch(
      'post',
      `/api/projects/${projectId}/dimensions_create`,
      data,
      config
    )
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

  async updateProject({projectId, data}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch('patch', `/api/projects/${projectId}/`, data, config)
  },

  async updateAvailableWidgets({projectId, data}) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch(
      'patch',
      `/api/projects/${projectId}/widgets_list/update`,
      data,
      config
    )
  },

  async deleteClippingFeedContentPost(projectId, postId) {
    const config = {
      headers: {
        'content-type': 'application/json',
        'X-CSRFToken': CSRF_TOKEN,
      },
    }
    return fetch(
      'delete',
      `/api/projects/${projectId}/clipping_feed_content_widget/delete/${postId}`,
      config
    )
  },
}
