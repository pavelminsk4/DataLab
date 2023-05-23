<template>
  <div
    :style="`background-color: ${backgroundColor}`"
    class="search-result-card"
  >
    <div class="header">
      <TFSCardStatuses />
      <div class="additional-info">
        <span>{{ date }}</span>
        <span>{{ source }}</span>
      </div>
    </div>

    <div class="body-card">
      <div class="general-information">
        <slot name="title"></slot>

        <div class="description" tabindex="0">
          <slot name="description"></slot>
        </div>

        <div class="type-request">
          <div class="type">
            <slot name="post-type"></slot>
          </div>

          <div :class="['type', `status`]">
            <SentimentChips :chips-type="sentiment" :post-id="postId" />
          </div>

          <div class="type category"><HashtagIcon /> {{ category }}</div>
        </div>
      </div>
    </div>

    <div class="post-card__information">
      <slot name="information"></slot>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import {capitalizeFirstLetter} from '@lib/utilities'

import HashtagIcon from '@/components/icons/HashtagIcon'
import SentimentChips from '@/components/SentimentChips'

import TFSCardStatuses from '@/components/tweny-four-seven/TFSCardStatuses'

export default {
  name: 'TFSPostCardLayout',
  components: {
    SentimentChips,
    HashtagIcon,
    TFSCardStatuses,
  },
  props: {
    postId: {type: Number},
    sentiment: {type: String},
    category: {type: String},
    source: {type: String},
    date: {type: String},
    backgroundColor: {type: String},
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING_WIDGETS}),
    isLoadingClippingWidget() {
      return this.isLoading.clippingWidget
    },
  },
  methods: {
    capitalizeFirstLetter,
  },
}
</script>

<style lang="scss" scoped>
.search-result-card {
  width: 320px;

  border-radius: 8px;
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
  background-color: var(--background-secondary-color);

  color: var(--typography-title-color);

  .header {
    padding: 12px 20px 0;
    .additional-info {
      display: flex;
      gap: 12px;

      margin-top: 12px;

      font-style: normal;
      font-weight: 400;
      font-size: 11px;
      line-height: 12px;
      color: var(--typography-secondary-color);
    }
  }

  .body-card {
    display: flex;

    padding: 0 20px;

    .general-information {
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      width: 100%;

      .description {
        display: -webkit-box;

        margin-bottom: 20px;

        cursor: pointer;
        overflow: hidden;
        text-overflow: ellipsis;

        -webkit-line-clamp: 3;
        -webkit-box-orient: vertical;

        font-weight: 400;
        font-size: 14px;
        line-height: 150%;

        &:focus {
          -webkit-box-orient: revert;
        }
      }

      .type-request {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 8px;

        .type {
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 4px;

          height: 30px;

          padding: 6px 8px;

          border-radius: 2px 12px 12px 2px;
          background-color: var(--chips-background-secondary-color);

          font-style: normal;
          font-weight: 400;
          font-size: 12px;
          line-height: 16px;
          color: var(--typography-secondary-color);
        }

        .category {
          background-color: var(--hashtag-bg-color);
        }

        .status {
          background-color: transparent;
        }
      }
    }
  }
}
</style>

<style lang="scss">
.post-card__information {
  display: flex;

  margin-top: 12px;
  padding: 14px 20px 24px;

  border-top: var(--border-primary);

  &_block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;

    padding-right: 8px;
    margin-right: 8px;

    border-right: var(--border-primary);

    &:last-child {
      padding-right: 0;
      margin-right: 0;

      border-right: none;
    }

    &_name {
      font-weight: 500;
      font-size: 10px;
      color: var(--typography-secondary-color);
    }

    &_value {
      text-decoration: none;
      font-size: 11px;
      color: var(--typography-title-color);
    }
  }
}
</style>
