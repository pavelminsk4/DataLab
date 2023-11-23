<template>
  <SearchScreen
    module-name="Online"
    :current-project="currentProject"
    :additional-filters="additionalFilters"
    :keywords="keywords"
    :clippingContent="clippingContent"
    :numberOfPosts="numberOfPosts"
    @show-results="showResults"
    @update-project="updateProject"
    @update-collection="updateCollection"
  />
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import SearchScreen from '@components/project/search/SearchScreen'

const {mapActions: mapOnlineActions, mapState} =
  createNamespacedHelpers('online')

const {mapActions: mapOnlineWidgetsActions} =
  createNamespacedHelpers('online/widgets')

export default {
  name: 'OnlineSearch',
  components: {SearchScreen},
  props: {
    currentProject: {type: [Array, Object], required: true},
  },
  computed: {
    ...mapState({
      clippingContent: (state) => state.widgets.clippingFeedContent.data,
    }),
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      numberOfPosts: get.POSTS_NUMBER,
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
  },
  async created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject.start_search_date),
        new Date(this.currentProject.end_search_date),
      ],
    })

    if (!this.availableWidgets) {
      await this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)
    }

    if (!this.clippingContent.length) {
      await this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.currentProject.id,
        widgetId: this.availableWidgets.clipping_feed_content.id,
      })
    }
  },
  methods: {
    ...mapActions([
      action.CLEAR_STATE,
      action.UPDATE_KEYWORDS_LIST,
      action.UPDATE_ADDITIONAL_FILTERS,
    ]),
    ...mapOnlineActions([
      action.POST_SEARCH,
      action.GET_WORKSPACES,
      action.UPDATE_PROJECT,
      action.GET_AVAILABLE_WIDGETS,
    ]),
    ...mapOnlineWidgetsActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
    showResults(filters) {
      try {
        this[action.POST_SEARCH](filters)
      } catch (e) {
        console.error(e)
      }
    },
    updateProject(data) {
      try {
        this[action.UPDATE_PROJECT]({
          projectId: this.currentProject?.id,
          data,
        })

        this[action.CLEAR_STATE]()

        this[action.GET_WORKSPACES]()
      } catch (e) {
        console.error(e)
      }
    },
    updateCollection(name, val) {
      this[action.UPDATE_KEYWORDS_LIST]({
        [name]: val,
      })
    },
  },
}
</script>
