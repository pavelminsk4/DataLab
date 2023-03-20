<template>
  <ClippingFeedContentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :clipping-feed-content-data="clippingFeedContent"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ClippingFeedContentWidget from '@/components/widgets/ClippingFeedContentWidget'

export default {
  name: 'OnlineClippingFeedContentWidget',
  components: {ClippingFeedContentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      clippingFeedContent: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
  },
  created() {
    if (!this.clippingFeedContent.length) {
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
  },
}
</script>
