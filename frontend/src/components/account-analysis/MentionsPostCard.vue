<template>
  <account-analysis-post-card-layout :post-details="postDetails">
    <div class="card-body">
      <div class="card-body__image">
        <img :src="postImage" class="image" />
      </div>
      <div class="card-body__content">
        <section class="user">
          <UserAvatar
            :avatarUrl="postDetails.user_picture"
            style="--avatar-width: 32px"
          />
          <div class="user__info">
            <span class="user__name">{{ postDetails.user_name }}</span>
            <span class="user__alias">@{{ postDetails.user_alias }}</span>
          </div>
        </section>
        <section class="card-body__text">
          <span class="mention">@Mention</span> {{ postDetails.text }}
        </section>
        <div class="card-body__chips">
          <div class="chips__card-body">
            <SentimentChips
              :chips-type="postDetails.sentiment"
              :post-id="postDetails.id"
            />
          </div>
          <div class="chips__card-body">
            <BaseChips chips-type="topic"> Topic</BaseChips>
          </div>
        </div>
      </div>
    </div>
  </account-analysis-post-card-layout>
</template>

<script>
import AccountAnalysisPostCardLayout from '@components/account-analysis/AccountAnalysisPostCardLayout'
import UserAvatar from '@components/UserAvatar'
import SentimentChips from '@components/SentimentChips'
import BaseChips from '@components/BaseChips'

export default {
  name: 'MentionsPostCard',
  components: {
    AccountAnalysisPostCardLayout,
    UserAvatar,
    SentimentChips,
    BaseChips,
  },
  props: {
    postDetails: {type: Object, required: true},
  },
  computed: {
    postImage() {
      const noPostsImg = require('@assets/no-posts-image.png')
      return this.postDetails.images[0] || noPostsImg
    },
  },
}
</script>

<style lang="scss" scoped>
.card-body {
  display: flex;
  gap: 15px;

  &__image {
    .image {
      height: 170px;
      width: 120px;
      object-fit: cover;
    }
  }

  &__content {
    display: flex;
    flex-direction: column;
    justify-content: space-between;

    .user {
      display: flex;

      &__info {
        display: flex;
        flex-direction: column;
      }

      &__name {
        display: -webkit-box;
        -webkit-line-clamp: 1;
        -webkit-box-orient: vertical;
        overflow: hidden;
      }

      &__alias {
        font-size: 11px;
        color: var(--typography-title-color);
      }
    }
  }

  .mention {
    color: var(--primary-color);
  }

  &__text {
    display: -webkit-box;
    -webkit-line-clamp: 3;
    -webkit-box-orient: vertical;
    overflow: hidden;
  }

  &__chips {
    display: flex;

    gap: 8px;
    .chips__container {
      height: fit-content;
    }
  }
}
</style>
