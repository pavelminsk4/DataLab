<template>
  <post-card-layout
    :sentiment="sentiment"
    :post-image="img"
    :is-clipping-widget="isClippingWidget"
    :is-clipping-post="isClippingPost"
    @add-clipping-post="addClippingFeedPost"
    @delete-clipping-post="deleteClippingFeedPost"
  >
    <template #title>
      <a class="title" tabindex="0" :href="entryLink" target="_blank">
        {{ title }}
      </a>
    </template>

    <template #description>{{ summary }}</template>

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
  </post-card-layout>
</template>

<script>
import {mapActions} from 'vuex'
import {action} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import OnlineIcon from '@/components/icons/OnlineIcon'
import PostCardLayout from '@/components/layout/PostCardLayout'

export default {
  name: 'OnlinePostCard',
  components: {
    OnlineIcon,
    PostCardLayout,
  },
  props: {
    isClippingWidget: {
      type: Boolean,
      default: false,
    },
    title: {
      type: String,
      required: false,
    },
    entryLink: {
      type: String,
      required: false,
    },
    summary: {
      type: String,
      required: false,
    },
    source: {
      type: String,
      required: false,
    },
    sourceLink: {
      type: String,
      required: false,
    },
    country: {
      type: String,
      required: false,
    },
    language: {
      type: String,
      required: false,
    },
    potentialReach: {
      type: Number,
      required: false,
    },
    published: {
      type: String,
      required: false,
    },
    img: {
      type: String,
      required: false,
    },
    sentiment: {
      type: String,
      required: false,
    },
    postId: {
      type: Number,
      required: false,
    },
    projectId: {
      type: Number,
      required: false,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    isClippingPost: {
      type: Boolean,
      default: false,
    },
  },
  computed: {
    commonCardItems() {
      return [
        {name: 'DATE', value: this.defaultDate(this.published)},
        {name: 'SOURCE', value: this.sourceLink},
        {name: 'LOCATION', value: this.country},
        {name: 'LANGUAGE', value: this.language},
        {name: 'POTENTIAL REACH', value: this.potentialReach},
      ]
    },
  },
  methods: {
    defaultDate,
    ...mapActions([
      action.CREATE_CLIPPING_FEED_CONTENT_WIDGET,
      action.DELETE_CLIPPING_FEED_CONTENT,
    ]),
    async addClippingFeedPost() {
      await this[action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({
        posts: [
          {
            project: this.projectId,
            post: this.postId,
          },
        ],
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    },
    async deleteClippingFeedPost() {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.projectId,
        postId: this.postId,
        widgetId: this.widgetId,
      })
    },
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
