<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @open-modal="$emit('open-settings-modal')"
  >
    <div :class="['clipping-wrapper', 'scroll', isSettings && 'widget-view']">
      <div v-if="!clippingFeedContentData.length" class="no-selected">
        Clipping feed content is not selected.
      </div>

      <ClippingCard
        v-for="(item, index) in clippingFeedContentData"
        :key="'result' + index"
        :img="cardImg(item)"
        :sentiment="item.post__sentiment"
        :title="item.post__entry_title"
        :entry-link="item.post__entry_links_href"
        :source-link="item.post__feedlink__sourceurl"
        :summary="item.post__entry_summary"
        :source="item.post__feedlink__source1"
        :country="item.post__feedlink__country"
        :language="item.post__feed_language__language"
        :published="item.post__entry_published"
        :potential-reach="item.post__feedlink__alexaglobalrank"
        :post-id="item.post__id"
        :project-id="widgetDetails.projectId"
        :is-clipping-widget="true"
        :widget-id="widgetDetails.id"
      />
    </div>
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ClippingCard from '@/components/ClippingCard'

export default {
  name: 'ClippingFeedContentWidget',
  components: {ClippingCard, WidgetsLayout},
  props: {
    clippingFeedContentData: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
  methods: {
    cardImg(item) {
      let images = [
        item.post__entry_media_content_url,
        item.post__entry_media_thumbnail_url,
        item.post__feed_image_href,
        item.post__feed_image_link,
      ]
      return images.filter((el) => el !== 'None')[0] || 'None'
    },
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
