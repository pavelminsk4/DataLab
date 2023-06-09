import {fetch} from './api'

const moduleName = '/comparison'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/projects_list`)
  },

  async updateWorkspace({workspaceId, data}) {
    return fetch('put', `${moduleName}/workspaces/${workspaceId}/`, data)
  },
}
