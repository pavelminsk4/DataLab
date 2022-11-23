<template>
  <WidgetsLayout
    v-if="clippingData"
    title="Clipping Feed Content"
    :is-show-settings="false"
  >
    <div class="clipping-wrapper">
      <div v-if="!clippingData.length" class="no-selected">
        Clipping feed content is not selected.
      </div>

      <BaseClippingCard
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
        :post-id="item.post__id"
        :project-id="projectId"
        :is-clipping-widget="true"
      />
    </div>
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import BaseClippingCard from '@/components/BaseClippingCard'

export default {
  name: 'ClippingFeedContentWidget',
  components: {BaseClippingCard, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    if (!this.clippingData.length) {
      this[action.GET_CLIPPING_FEED_CONTENT_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
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

  &::-webkit-scrollbar {
    height: 5px;
    width: 5px;
  }

  &::-webkit-scrollbar-track {
    background: var(--secondary-bg-color);
    border: 1px solid var(--input-border-color);
    border-radius: 0 10px 10px 0;
  }

  &::-webkit-scrollbar-thumb {
    height: 4px;

    background: var(--secondary-text-color);
    border-radius: 10px;
  }
}
</style>
