<template>
  <BaseModal title="Top Results">
    <ClippingCard
      v-for="(item, index) in posts"
      :key="'result' + index"
      :id="item.id"
      :img="cardImg(item)"
      :title="item.entry_title"
      :country="item.feedlink__country"
      :entry-link="item.entry_links_href"
      :summary="item.entry_summary"
      :sentiment="item.sentiment"
      :published="item.entry_published"
      :source-link="item.feedlink__sourceurl"
      :source="item.feedlink__source1"
      :language="item.feed_language__language"
      :potential-reach="item.feedlink__alexaglobalrank"
      :widget-id="widgetId"
      :currentProject="currentProject"
      class="clipping-card"
    />
  </BaseModal>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import BaseModal from '@/components/modals/BaseModal'
import ClippingCard from '@/components/ClippingCard'

export default {
  name: 'InteractiveWidgetModal',
  components: {ClippingCard, BaseModal},
  props: {
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
      interactiveWidgets: get.INTERACTIVE_DATA,
    }),
    posts() {
      return this.interactiveWidgets.posts
    },
  },
  methods: {
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

<style scoped></style>
