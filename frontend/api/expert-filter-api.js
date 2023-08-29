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

  async getPresets({groupId}) {
    return fetch('get', `/groups/${groupId}/presets/`)
  },
  async createPreset({groupId, data}) {
    return fetch('post', `/groups/${groupId}/presets/`, data)
  },
  async deletePreset({groupId, presetId}) {
    return fetch('delete', `/groups/${groupId}/presets/${presetId}/`)
  },
  async updatePreset({groupId, presetId, data}) {
    return fetch('patch', `/groups/${groupId}/presets/${presetId}/`, data)
  },
}
