<template>
  <TFSPostCardLayout
    :sentiment="postDetails.sentiment"
    :category="postDetails.category"
    :date="this.defaultDate(this.postDetails.entry_published)"
    :source="this.postDetails.feedlink__sourceurl"
    :post-image="img"
    :post-id="postDetails.id"
    background-color="#EFFCFE"
  >
    <template #title>
      <a
        class="title"
        tabindex="0"
        :href="postDetails.entry_links_href"
        target="_blank"
      >
        {{ postDetails.entry_title }}
      </a>
    </template>

    <template #description>{{ postDetails.entry_summary }}</template>

    <template #post-type><OnlineIcon /> Online</template>

    <template #information>
      <div
        v-for="(item, index) in commonCardItems"
        :key="item.name + index"
        class="post-card__information_block"
      >
        <div class="post-card__information_block_name">{{ item.name }}</div>
        <a
          v-if="item.name === 'SOURCE'"
          :href="getUrl(item.value)"
          target="_blank"
          class="post-card__information_block_value"
        >
          {{ item.value }}
        </a>
        <div v-else class="post-card__information_block_value">
          {{ item.value }}
        </div>
      </div>
    </template>
  </TFSPostCardLayout>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import OnlineIcon from '@/components/icons/OnlineIcon'
import TFSPostCardLayout from '@/components/tweny-four-seven/TFSPostCardLayout'

export default {
  name: 'TFSPostCard',
  components: {
    OnlineIcon,
    TFSPostCardLayout,
  },
  props: {
    img: {type: String, required: false},
    postDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      clippingWidgets: get.CLIPPING_WIDGETS_DETAILS,
    }),
    commonCardItems() {
      return [
        {name: 'LOCATION', value: this.postDetails.feedlink__country},
        {name: 'LANGUAGE', value: this.postDetails.feed_language__language},
        {
          name: 'POTENTIAL REACH',
          value: this.postDetails.feedlink__alexaglobalrank,
        },
      ]
    },
    projectId() {
      return this.$route.params.projectId
    },
  },
  methods: {
    defaultDate,
    getUrl(source) {
      if (!source) return ''
      return source.includes('http') ? source : `http://${source}`
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  margin-bottom: 8px;

  cursor: pointer;

  text-decoration: none;
  white-space: pre-wrap;
  font-style: normal;
  font-weight: 600;
  font-size: 20px;
  line-height: 28px;
  color: var(--typography-title-color);

  &:hover {
    color: var(--primary-hover-color);
  }
}
</style>
