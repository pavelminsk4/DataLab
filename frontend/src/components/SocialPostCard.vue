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
      <div class="title">
        <div class="user-avatar"></div>
        <div>
          <h3 class="user-name"></h3>
          <div class="user-account"></div>
        </div>
      </div>
    </template>

    <template #description>{{ text }}</template>

    <template #post-type><TwitterIcon /> Twitter</template>

    <template #information>
      <div
        v-for="(item, index) in commonCardItems"
        :key="item.name + index"
        class="post-card__information_block"
      >
        <div v-if="item.isIcon" class="information-block-wrapper">
          <component :is="item.name" />
          <div class="post-card__information_block_value">
            {{ item.value }}
          </div>
        </div>
        <template v-else>
          <div class="post-card__information_block_name">{{ item.name }}</div>
          <div class="post-card__information_block_value">
            {{ item.value }}
          </div>
        </template>
      </div>
    </template>
  </post-card-layout>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/modules/social/constants'
import {defaultDate} from '@lib/utilities'

import LikeIcon from '@/components/icons/LikeIcon'
import RepliesIcon from '@/components/icons/RepliesIcon'
import RetweetsIcon from '@/components/icons/RetweetsIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'

import PostCardLayout from '@/components/layout/PostCardLayout'

const {mapActions} = createNamespacedHelpers('social')

export default {
  name: 'SocialPostCard',
  components: {
    LikeIcon,
    PostCardLayout,
    RepliesIcon,
    RetweetsIcon,
    TwitterIcon,
  },
  props: {
    isClippingWidget: {
      type: Boolean,
      default: false,
    },
    countFavorites: {
      type: Number,
      default: 0,
    },
    countReplies: {
      type: Number,
      default: 0,
    },
    countRetweets: {
      type: Number,
      default: 0,
    },
    date: {
      type: String,
      default: '',
    },
    language: {
      type: String,
      default: '',
    },
    locationString: {
      type: String,
      default: '',
    },
    sentiment: {
      type: String,
      default: '',
    },
    text: {
      type: String,
      default: '',
    },
    userAlias: {
      type: String,
      default: '',
    },
    userName: {
      type: String,
      default: '',
    },
    img: {
      type: String,
      default: '',
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
        {name: 'DATE', value: this.defaultDate(this.date)},
        {name: 'LOCATION', value: this.locationString},
        {name: 'LANGUAGE', value: this.language},
        {name: 'LikeIcon', value: this.countFavorites, isIcon: true},
        {name: 'RepliesIcon', value: this.countReplies, isIcon: true},
        {name: 'RetweetsIcon', value: this.countRetweets, isIcon: true},
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
  },
}
</script>

<style lang="scss" scoped>
.title {
  display: flex;
  gap: 8px;

  margin-bottom: 8px;

  .user-name {
    font-weight: 500;
    font-size: 16px;
    line-height: 20px;
  }

  .user-account {
    font-size: 11px;
    line-height: 12px;
    color: var(--typography-title-color);
  }
}

.information-block-wrapper {
  display: flex;
  align-items: center;
  gap: 4px;
}
</style>
