import {fetch} from './api'

const moduleName = '/account_analysis'

export default {
  async getWorkspaces() {
    return fetch('get', `${moduleName}/workspaces/`)
  },
}
