import api from '@api/api'
import {action, mutator} from '@store/constants'

export default {
  async [action.GET_SUMMARY_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const summary = await api.social.getSummaryWidget(projectId, widgetId)
      commit(mutator.SET_SUMMARY_WIDGET, summary)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_CLIPPING_FEED_CONTENT_WIDGET](
    {commit},
    {projectId, widgetId}
  ) {
    commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: true}, {root: true})
    try {
      const clippingFeedContent = await api.social.getClippingFeedContentWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_CLIPPING_FEED_CONTENT_WIDGET, clippingFeedContent)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING_WIDGETS, {clippingWidget: false}, {root: true})
    }
  },

  async [action.GET_CONTENT_VOLUME_WIDGET](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const volume = await api.social.getContentVolumeWidget({
        projectId,
        value,
        widgetId,
      })
      commit(mutator.SET_CONTENT_VOLUME_WIDGET, volume)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  async [action.GET_TOP_LOCATIONS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topLocation = await api.social.getTopLocationsWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_LOCATIONS_WIDGET, topLocation)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_LANGUAGES_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topLanguages = await api.social.getTopLanguagesWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_LANGUAGES_WIDGET, topLanguages)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_TOP_AUTHORS_WIDGET]({commit}, {projectId, widgetId}) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const topAuthors = await api.social.getTopAuthorsWidget(
        projectId,
        widgetId
      )
      commit(mutator.SET_TOP_AUTHORS_WIDGET, topAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },

  // Content Volume
  async [action.GET_CONTENT_VOLUME_TOP_LOCATIONS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopCountries =
        await api.social.getContentVolumeTopLocations({
          projectId,
          value,
          widgetId,
        })
      commit(
        mutator.SET_CONTENT_VOLUME_TOP_LOCATIONS,
        contentVolumeTopCountries
      )
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_CONTENT_VOLUME_TOP_AUTHORS](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopAuthors =
        await api.social.getContentVolumeTopAuthors({
          projectId,
          value,
          widgetId,
        })
      commit(mutator.SET_CONTENT_VOLUME_TOP_AUTHORS, contentVolumeTopAuthors)
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
  async [action.GET_CONTENT_VOLUME_TOP_LANGUAGES](
    {commit},
    {projectId, value, widgetId}
  ) {
    commit(mutator.SET_LOADING, true, {root: true})
    try {
      const contentVolumeTopLanguages =
        await api.social.getContentVolumeTopLanguages({
          projectId,
          value,
          widgetId,
        })
      commit(
        mutator.SET_CONTENT_VOLUME_TOP_LANGUAGES,
        contentVolumeTopLanguages
      )
    } catch (e) {
      console.log(e)
    } finally {
      commit(mutator.SET_LOADING, false, {root: true})
    }
  },
}
