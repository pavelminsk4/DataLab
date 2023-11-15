<template>
  <ClippingFeedContentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :clipping-feed-content-data="clippingFeedContent"
    @delete-clipping-post="deleteClippingPost"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import ClippingFeedContentWidget from '@components/widgets/ClippingFeedContentWidget'

const {mapActions} = createNamespacedHelpers('online')
const {mapActions: mapOnlineWidgetsAction, mapGetters: mapGettersOnline} =
  createNamespacedHelpers('online/widgets')

export default {
  name: 'OnlineClippingFeedContentWidget',
  components: {ClippingFeedContentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGettersOnline({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    clippingFeedContent() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.clippingFeedContent.data
      )
    },
    widgetId() {
      return this.onlineWidgets.clippingFeedContent?.id
    },
  },
  created() {
    const hasCurrentData =
      this.clippingFeedContent.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.DELETE_CLIPPING_FEED_CONTENT]),
    ...mapOnlineWidgetsAction([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
    async deleteClippingPost(postId) {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.widgetDetails.projectId,
        postId,
        widgetId: this.widgetDetails.id,
      })
    },
  },
}
</script>
