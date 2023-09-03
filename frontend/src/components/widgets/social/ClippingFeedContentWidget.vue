<template>
  <ClippingFeedContentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :clipping-feed-content-data="clippingFeedContent"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get} from '@store/constants'
import {action} from '@store/constants'

import ClippingFeedContentWidget from '@/components/widgets/ClippingFeedContentWidget'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialClippingFeedContentWidget',
  components: {ClippingFeedContentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    clippingFeedContent() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.clippingFeedContent.data
      )
    },
    widgetId() {
      return this.socialWidgets.clippingFeedContent?.id
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
    ...mapActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
  },
}
</script>

<style lang="scss" scoped>
.widget-view {
  padding: 24px;
}

.clipping-wrapper {
  overflow: auto;

  max-width: 100%;

  .no-selected {
    margin-top: 20px;
  }
}
</style>
