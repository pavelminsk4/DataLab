<template>
  <post-card-layout
    :sentiment="postDetails.sentiment"
    :post-image="img"
    :is-clipping-widget="isClippingWidget"
    :is-clipping-post="isClippingPost"
    @add-clipping-post="addClippingFeedPost"
    @delete-clipping-post="deleteClippingFeedPost"
  >
    <template #title>
      <div class="title">
        <div class="user-avatar">
          <img
            :src="postDetails.user_picture"
            alt="user picture"
            class="user-img"
          />
        </div>
        <div>
          <h3 class="user-name">{{ postDetails.user_name }}</h3>
          <div class="user-account">@{{ postDetails.user_alias }}</div>
        </div>
      </div>
    </template>

    <template #description>{{ postDetails.text }}</template>

    <template #post-type><TwitterIcon class="icon-size" /> Twitter</template>

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
import {action, get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import LikeIcon from '@/components/icons/LikeIcon'
import RepliesIcon from '@/components/icons/RepliesIcon'
import RetweetsIcon from '@/components/icons/RetweetsIcon'
import TwitterIcon from '@/components/icons/TwitterIcon'

import PostCardLayout from '@/components/layout/PostCardLayout'

const {mapActions, mapGetters} = createNamespacedHelpers('social')

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
    isClippingPost: {type: Boolean, default: false},
    img: {type: String, default: ''},
    isClippingWidget: {type: Boolean, default: false},
    postDetails: {type: Object, required: true},
  },

  computed: {
    ...mapGetters({
      clippingWidgets: get.CLIPPING_WIDGETS_DETAILS,
    }),
    projectId() {
      return this.$router.params.projectId
    },
    commonCardItems() {
      return [
        {name: 'DATE', value: this.defaultDate(this.postDetails.date)},
        {name: 'LOCATION', value: this.postDetails.locationString},
        {name: 'LANGUAGE', value: this.postDetails.language},
        {
          name: 'LikeIcon',
          value: this.postDetails.count_favorites,
          isIcon: true,
        },
        {
          name: 'RepliesIcon',
          value: this.postDetails.count_replies,
          isIcon: true,
        },
        {
          name: 'RetweetsIcon',
          value: this.postDetails.count_retweets,
          isIcon: true,
        },
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

  .user-img {
    width: 32px;
    height: 32px;

    border-radius: 50%;
  }
}

.information-block-wrapper {
  display: flex;
  align-items: center;
  gap: 4px;
}

.icon-size {
  height: 16px;
}
</style>
