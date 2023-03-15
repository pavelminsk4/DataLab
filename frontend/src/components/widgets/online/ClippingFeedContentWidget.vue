<template>
  <ClippingFeedContentWidget
    v-bind="$attrs"
    :title="availableWidgets.clipping_feed_content_widget.title"
    :project-id="projectId"
    :widget-id="widgetId"
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
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
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
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
  },
}
</script>
