<template>
  <WidgetsLayout
    v-if="clippingData"
    @open-modal="$emit('open-settings-modal')"
    :title="widgets['clipping_feed_content_widget'].title"
  >
    <div class="clipping-wrapper scroll">
      <div v-if="!clippingData.length" class="no-selected">
        Clipping feed content is not selected.
      </div>

      <ClippingCard
        v-for="(item, index) in clippingData"
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
        :project-id="projectId"
        :is-clipping-widget="true"
        :widget-id="widgetId"
        :current-project="currentProject"
      />
    </div>
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ClippingCard from '@/components/ClippingCard'

export default {
  name: 'ClippingFeedContentWidget',
  components: {ClippingCard, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    ...mapGetters({
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
      widgets: get.AVAILABLE_WIDGETS,
    }),
  },
  created() {
    this[action.GET_CLIPPING_FEED_CONTENT_WIDGET]({
      projectId: this.projectId,
      widgetId: this.widgetId,
    })
  },
  methods: {
    ...mapActions([action.GET_CLIPPING_FEED_CONTENT_WIDGET]),
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
.clipping-wrapper {
  overflow: auto;

  max-width: 100%;

  .no-selected {
    margin-top: 20px;
  }
}
</style>
