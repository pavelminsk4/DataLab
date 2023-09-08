<template>
  <post-card-layout
    :sentiment="postDetails.sentiment || ''"
    :category="postDetails.category"
    :post-image="img"
    :post-id="postDetails.id"
    :is-clipping-widget="isClippingWidget"
    :is-clipping-post="isClippingPost"
    @add-clipping-post="addClippingFeedPost"
    @delete-clipping-post="deleteClippingFeedPost"
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

    <template #post-type>
      <OnlineIcon class="icon" />
      <CustomText text="Online" />
    </template>

    <template #information>
      <div
        v-for="(item, index) in commonCardItems"
        :key="item.name + index"
        class="post-card__information_block"
      >
        <CustomText
          :text="item.name"
          class="post-card__information_block_name"
        />
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
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import CustomText from '@/components/CustomText'
import OnlineIcon from '@/components/icons/OnlineIcon'
import PostCardLayout from '@/components/layout/PostCardLayout'

const {mapActions, mapGetters} = createNamespacedHelpers('online')

export default {
  name: 'OnlinePostCard',
  components: {
    CustomText,
    OnlineIcon,
    PostCardLayout,
  },
  props: {
    isClippingWidget: {type: Boolean, default: false},
    img: {type: String, required: false},
    isClippingPost: {type: Boolean, default: false},
    postDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      clippingWidgets: get.CLIPPING_WIDGETS_DETAILS,
    }),
    commonCardItems() {
      return [
        {
          name: 'DATE',
          value: this.defaultDate(
            this.postDetails.entry_published,
            this.platformLanguage
          ),
        },
        {name: 'SOURCE', value: this.postDetails.feedlink__sourceurl},
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
    ...mapActions([
      action.CREATE_CLIPPING_FEED_CONTENT_WIDGET,
      action.DELETE_CLIPPING_FEED_CONTENT,
    ]),
    async addClippingFeedPost() {
      await this[action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({
        posts: [
          {
            project: this.projectId,
            post: this.postDetails.id,
          },
        ],
        projectId: this.projectId,
        widgetId: this.clippingWidgets.id,
      })
    },
    async deleteClippingFeedPost() {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.projectId,
        postId: this.postDetails.id,
        widgetId: this.clippingWidgets.id,
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

.icon {
  width: 16px;
  height: 16px;
}
</style>
