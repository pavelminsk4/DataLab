import api from '@api/expert-filter-api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_PRESETS_GROUPS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.getPresetsGroups()
      commit(mutator.SET_PRESETS_GROUPS, response)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_PRESETS_GROUP]({commit, dispatch}, {data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createPresetsGroup({data})
      commit(mutator.SET_NEW_PRESETS_GROUP, response)
      await dispatch(action.GET_PRESETS_GROUPS)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.DELETE_PRESETS_GROUP]({commit, dispatch}, {groupId}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.deletePresetsGroup({groupId})
      await dispatch(action.GET_PRESETS_GROUPS)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_PRESETS_GROUP]({commit, dispatch}, {groupId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.updatePresetsGroup({groupId, data})
      await dispatch(action.GET_PRESETS_GROUPS)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },

  async [action.GET_PRESETS]({commit}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.getPresets()
      commit(mutator.SET_PRESETS, response)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.CREATE_PRESET](
    {commit, dispatch},
    {groupId, presetsIds, data}
  ) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.createPreset(data)
      await dispatch(action.UPDATE_PRESETS_GROUP, {
        groupId,
        data: {presets: [...presetsIds, response.id]},
      })
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.DELETE_PRESET]({commit, dispatch}, presetId) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.deletePreset(presetId)
      await dispatch(action.GET_PRESETS_GROUPS)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
  async [action.UPDATE_PRESET]({commit, dispatch}, {presetId, data}) {
    commit(mutator.SET_LOADING, true)
    try {
      const response = await api.updatePreset({presetId, data})
      await dispatch(action.GET_PRESETS_GROUPS)
      return response
    } finally {
      commit(mutator.SET_LOADING, false)
    }
  },
}
