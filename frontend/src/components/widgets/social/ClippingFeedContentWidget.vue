<template>
  <ClippingFeedContentWidget
    v-bind="$attrs"
    :title="availableWidgets.clipping_feed_content.title"
    :project-id="projectId"
    :widget-id="widgetId"
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
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
  },
  computed: {
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    clippingFeedContent() {
      return this.socialWidgets.clippingFeedContent
    },
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
