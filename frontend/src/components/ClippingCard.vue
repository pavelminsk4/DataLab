<template>
  <div :class="['search-result-card', `search-result-${sentiment}`]">
    <div class="body-card">
      <div class="result-img">
        <img v-if="img !== 'None'" :src="img" :class="['img']" alt="img" />
        <NoImageIcon v-else />
      </div>
      <div class="general-information">
        <a class="title" tabindex="0" :href="entryLink" target="_blank">
          {{ title }}
        </a>
        <div class="description" tabindex="0">{{ summary }}</div>
        <div class="type-request">
          <div class="type"><OnlineIcon /> Online</div>
          <div :class="['type', `status-${sentiment}`]">
            <component :is="capitalizeFirstLetter(sentiment) + 'Icon'" />
            {{ capitalizeFirstLetter(sentiment) }}
          </div>
          <div class="clipping-wrapper">
            <ClippingIcon
              v-if="isCheckboxClippingWidget"
              :isClippingElement="clippingElement"
              :isLoading="isLoadingClippingWidget"
              @click="addPost"
            />
            <BaseTooltip class="tooltip">{{ clippingTooltip }}</BaseTooltip>
          </div>
        </div>
      </div>
      <CloseIcon
        v-if="isClippingWidget"
        @click="deleteClippingFeedPost"
        class="delete-clipping-feed-element"
      />
    </div>

    <div class="common-information">
      <div
        v-for="(item, index) in commonCardItems"
        :key="item.name + index"
        class="item"
      >
        <div class="item-name">{{ item.name }}</div>
        <div class="item-value">{{ item.value }}</div>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {capitalizeFirstLetter, defaultDate} from '@lib/utilities'

import OnlineIcon from '@/components/icons/OnlineIcon'
import NeutralIcon from '@/components/icons/NeutralIcon'
import PositiveIcon from '@/components/icons/PositiveIcon'
import NegativeIcon from '@/components/icons/NegativeIcon'
import ClippingIcon from '@/components/icons/ClippingIcon'
import BaseTooltip from '@/components/BaseTooltip'
import NoImageIcon from '@/components/icons/NoImageIcon'
import CloseIcon from '@/components/icons/CloseIcon'

export default {
  name: 'ClippingCard',
  components: {
    CloseIcon,
    NoImageIcon,
    BaseTooltip,
    ClippingIcon,
    NeutralIcon,
    NegativeIcon,
    PositiveIcon,
    OnlineIcon,
  },
  props: {
    isCheckboxClippingWidget: {
      type: Boolean,
      default: false,
    },
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
    id: {
      type: Number,
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
    clippingElement: {
      type: Boolean,
      default: false,
    },
    currentProject: {
      type: [Array, Object],
      required: true,
    },
  },
  computed: {
    ...mapGetters({isLoading: get.LOADING_WIDGETS}),
    isLoadingClippingWidget() {
      return this.isLoading.clippingWidget
    },
    clippingTooltip() {
      return this.clippingElement
        ? 'Remove from clipping widget'
        : 'Add to clipping widget'
    },
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
    capitalizeFirstLetter,
    defaultDate,
    ...mapActions([action.DELETE_CLIPPING_FEED_CONTENT]),
    async deleteClippingFeedPost() {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.projectId,
        postId: this.postId,
      })
    },
    addPost() {
      if (this.isLoadingClippingWidget) return
      this.$emit('add-element', this.id, this.clippingElement)
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

      .img {
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

          padding: 6px 8px;

          border-radius: 2px 12px 12px 2px;
          background-color: var(--primary-chips-background-color);

          font-style: normal;
          font-weight: 400;
          font-size: 12px;
          line-height: 16px;
          color: var(--typography-secondary-color);
        }

        .status-neutral {
          background-color: var(--neutral-secondary-color);
          color: var(--neutral-primary-color);
        }

        .status-positive {
          background-color: var(--positive-secondary-color);
          color: var(--positive-primary-color);
        }

        .status-negative {
          background-color: var(--negative-secondary-color);
          color: var(--negative-primary-color);
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

  .common-information {
    display: flex;

    margin-top: 12px;
    padding: 14px 20px 0;

    border-top: var(--border-primary);

    .item {
      display: flex;
      flex-direction: column;
      justify-content: flex-start;
      gap: 4px;

      padding-right: 12px;
      margin-right: 12px;

      border-right: var(--border-primary);

      &:last-child {
        padding-right: 0;
        margin-right: 0;

        border-right: none;
      }

      .item-name {
        font-style: normal;
        font-weight: 500;
        font-size: 10px;
        line-height: 10px;
        color: var(--typography-secondary-color);
      }

      .item-value {
        font-style: normal;
        font-weight: 400;
        font-size: 11px;
        line-height: 11px;
        color: var(--typography-title-color);
      }
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
