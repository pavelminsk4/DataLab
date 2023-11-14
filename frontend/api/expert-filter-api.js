import {fetch} from './api'

export default {
  async getPresetsGroups() {
    return fetch('get', '/groups/')
  },
  async createPresetsGroup({data}) {
    return fetch('post', `/groups/`, data)
  },
  async deletePresetsGroup({groupId}) {
    return fetch('delete', `/groups/${groupId}/`)
  },
  async updatePresetsGroup({groupId, data}) {
    return fetch('patch', `/groups/${groupId}/`, data)
  },

  async getPresets() {
    return fetch('get', `/presets/`)
  },
  async createPreset(data) {
    return fetch('post', `/presets/`, data)
  },
  async deletePreset(presetId) {
    return fetch('delete', `/presets/${presetId}/`)
  },
  async updatePreset({presetId, data}) {
    return fetch('patch', `/presets/${presetId}/`, data)
  },
}
