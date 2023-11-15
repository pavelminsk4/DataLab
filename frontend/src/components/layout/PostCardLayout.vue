<template>
  <div :class="['search-result-card', `search-result-${sentiment}`]">
    <div class="body-card">
      <div class="result-img">
        <img
          v-if="postImage !== 'None' && isImgLoaded"
          :src="postImage"
          :class="['post-image']"
          alt="post image"
          @error="checkImg"
        />
        <NoImageIcon v-else />
      </div>

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

          <div class="type category">
            <HashtagIcon />
            <CustomText tag="span" :text="category" />
          </div>

          <div v-if="!isClippingWidget" class="clipping-wrapper">
            <ClippingIcon
              :is-clipping-post="isClippingPost"
              :is-loading="isLoadingClippingWidget"
              @click="addPost"
            />
            <BaseTooltip class="tooltip">{{ clippingTooltip }}</BaseTooltip>
          </div>
        </div>
      </div>

      <CloseIcon
        v-if="isClippingWidget"
        @click="$emit('delete-clipping-post')"
        class="delete-clipping-feed-element"
      />
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

import CustomText from '@components/CustomText'
import ClippingIcon from '@components/icons/ClippingIcon'
import BaseTooltip from '@components/BaseTooltip'
import NoImageIcon from '@components/icons/NoImageIcon'
import CloseIcon from '@components/icons/CloseIcon'
import HashtagIcon from '@components/icons/HashtagIcon'
import SentimentChips from '@components/SentimentChips'

export default {
  name: 'PostCardLayout',
  components: {
    SentimentChips,
    CloseIcon,
    NoImageIcon,
    BaseTooltip,
    ClippingIcon,
    HashtagIcon,
    CustomText,
  },
  props: {
    isClippingWidget: {type: Boolean, default: false},
    postImage: {type: String},
    postId: {type: Number},
    sentiment: {type: String},
    category: {type: String},
    isClippingPost: {type: Boolean, default: false},
  },
  data() {
    return {
      isImgLoaded: true,
    }
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING_WIDGETS}),
    isLoadingClippingWidget() {
      return this.isLoading?.clippingWidget
    },
    clippingTooltip() {
      return this.isClippingPost
        ? 'Remove from clipping widget'
        : 'Add to clipping widget'
    },
  },
  methods: {
    checkImg() {
      this.isImgLoaded = false
    },
    capitalizeFirstLetter,
    addPost() {
      if (this.isLoadingClippingWidget) return

      if (this.isClippingPost) {
        this.$emit('delete-clipping-post')
      } else {
        this.$emit('add-clipping-post')
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-card {
  padding: 18px 0;

  border-radius: 8px;
  box-shadow: 1px 4px 16px rgba(135, 135, 135, 0.2);
  background-color: var(--background-secondary-color);

  color: var(--typography-title-color);

  .body-card {
    display: flex;

    padding: 0 20px;

    .result-img {
      width: 120px;
      height: 172px;
      margin-right: 16px;

      .post-image {
        object-fit: cover;

        width: inherit;
        height: 100%;

        border-radius: 4px;
      }
    }

    .general-information {
      display: flex;
      flex-direction: column;
      justify-content: space-between;

      width: 100%;

      .description {
        display: -webkit-box;

        max-width: 27vw;
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

        .clipping-wrapper {
          position: relative;
          display: flex;
          justify-content: center;

          margin-left: auto;

          &:hover {
            .tooltip {
              visibility: visible;
            }
          }

          .tooltip {
            right: 28px;
            visibility: hidden;
          }
        }
      }
    }

    .delete-clipping-feed-element {
      cursor: pointer;

      color: var(--typography-secondary-color);
    }
  }
}

.search-result-neutral {
  border-left: 3px solid var(--neutral-primary-color);
}
.search-result-positive {
  border-left: 3px solid var(--positive-primary-color);
}

.search-result-negative {
  border-left: 3px solid var(--negative-primary-color);
}
</style>

<style lang="scss">
.post-card__information {
  display: flex;

  margin-top: 12px;
  padding: 14px 20px 0;

  border-top: var(--border-primary);

  &_block {
    display: flex;
    flex-direction: column;
    justify-content: center;
    gap: 4px;

    padding-right: 12px;
    margin-right: 12px;

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
