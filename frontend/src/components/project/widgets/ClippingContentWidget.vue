<template>
  <WidgetsLayout
    v-if="clippingWidget"
    @open-modal="$emit('open-settings-modal')"
    :title="widgets['clipping_widget'].title"
  >
    <div class="clipping-wrapper">
      <div v-if="!clippingWidget.length" class="no-selected">
        Clipping feed content is not selected.
      </div>

      <BaseClippingCard
        v-for="(item, index) in clippingWidget"
        :key="'result' + index"
        :img="cardImg(item)"
        :sentiment="item.sentiment"
        :title="item.entry_title"
        :entry-link="item.entry_links_href"
        :source-link="item.feedlink__sourceurl"
        :summary="item.entry_summary"
        :source="item.feedlink__source1"
        :country="item.feedlink__country"
        :language="item.feed_language__language"
        :published="item.entry_published"
        :post-id="item.id"
        :project-id="projectId"
        :is-clipping-widget="true"
      />
    </div>
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import BaseClippingCard from '@/components/BaseClippingCard'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'ClippingContentWidget',
  components: {BaseClippingCard, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    if (!this.clippingWidget.length) {
      this[action.GET_CLIPPING_WIDGET](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
      clippingWidget: get.CLIPPING_WIDGET,
    }),
  },
  methods: {
    ...mapActions([action.GET_CLIPPING_WIDGET]),
    cardImg(item) {
      let images = [
        item.entry_media_content_url,
        item.entry_media_thumbnail_url,
        item.feed_image_href,
        item.feed_image_link,
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
