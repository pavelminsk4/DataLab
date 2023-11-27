<template>
  <TFSPostCardLayout
    :sentiment="postDetails.sentiment || ''"
    :category="postDetails.category"
    :date="this.defaultDate(postDetails.entry_published, platformLanguage)"
    :source="this.postDetails.feedlink__sourceurl"
    :post-image="img"
    :post-id="postDetails.id"
    :status="cardStatus"
    :is-related="isRelatedContent"
  >
    <template #header>
      <div class="post-card-header">
        <div class="post-controls">
          <BaseCheckbox
            v-if="isCheckboxShow"
            v-model="relatedPost"
            :id="itemId"
            :value="itemId"
          />

          <TFSCardStatuses
            v-if="isStatusShow"
            :status="cardStatus"
            :post-id="postDetails.id"
            :isBack="isBack"
            :isShowDropdown="isShowStatusesDropdown"
            @change-status-card="changeStatusCard"
          />
        </div>

        <CustomText v-if="isRelatedContent" text="Related" class="related" />
      </div>
    </template>

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

    <template #post-type><OnlineIcon /> <CustomText text="Online" /></template>

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

    <template #buttons>
      <div
        v-if="isLinkedButtonShow"
        class="linked-button"
        @click="$emit('open-linked-modal')"
      >
        <PlusIcon />
        <CustomText tag="span" text="Add link to report" />
      </div>

      <CustomText
        v-if="isWorkButtonShow"
        text="Take to work"
        class="work-button"
        @click="$emit('open-modal')"
      />
    </template>
  </TFSPostCardLayout>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import CustomText from '@components/CustomText'
import PlusIcon from '@components/icons/PlusIcon'
import OnlineIcon from '@components/icons/OnlineIcon'
import BaseCheckbox from '@components/BaseCheckbox2'
import TFSPostCardLayout from '@components/twenty-four-seven/TFSPostCardLayout'
import TFSCardStatuses from '@components/twenty-four-seven/TFSCardStatuses'

export default {
  name: 'TFSPostCard',
  components: {
    OnlineIcon,
    TFSPostCardLayout,
    TFSCardStatuses,
    BaseCheckbox,
    PlusIcon,
    CustomText,
  },
  props: {
    img: {type: String, required: false},
    itemId: {type: Number, required: true},
    isBack: {type: Boolean, default: true},
    isRelatedContent: {type: Boolean, default: false},
    isWorkButtonShow: {type: Boolean, default: false},
    cardStatus: {type: String, required: false},
    postDetails: {type: Object, required: true},
    isStatusShow: {type: Boolean, default: true},
    isShowStatusesDropdown: {type: Boolean, default: true},
    isCheckboxShow: {type: Boolean, default: false},
    isLinkedButtonShow: {type: Boolean, default: false},
    selectedPost: {type: [Array, Boolean], required: false},
  },
  data() {
    return {
      selectedRelatedPosts: [],
    }
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
          value: this.postDetails.feedlink__alexaglobalrank.toLocaleString(),
        },
      ]
    },
    relatedPost: {
      get() {
        return this.selectedPost || this.selectedRelatedPosts
      },
      set(val) {
        this.selectedRelatedPosts = val
        this.$emit('add-related-content', val, this.itemId)
      },
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
    changeStatusCard(newStatus) {
      this.$emit('change-status', this.itemId, newStatus, this.cardStatus)
    },
  },
}
</script>

<style lang="scss" scoped>
.title {
  display: -webkit-box;

  margin-bottom: 8px;

  cursor: pointer;
  overflow: hidden;
  text-overflow: ellipsis;

  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;

  text-decoration: none;
  white-space: pre-wrap;
  font-weight: 600;
  font-size: 20px;
  color: var(--typography-title-color);

  &:hover {
    color: var(--primary-hover-color);
  }
}

.post-card-header {
  display: flex;
  justify-content: space-between;

  .post-controls {
    display: flex;
    gap: 16px;
  }

  .related {
    padding: 6px 8px;

    border-radius: 4px;
    background-color: var(--background-secondary-color);

    font-style: normal;
    font-weight: 400;
    font-size: 11px;
    line-height: 12px;
    color: var(--typography-primary-color);
  }
}

.linked-button {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 8px;

  cursor: pointer;

  font-weight: 500;
  color: var(--typography-primary-color);

  &:hover {
    color: var(--primary-hover-color);
  }
}

.post-card__information {
  &_block {
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    gap: 2px;

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

.work-button {
  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--button-primary-color);
}
</style>
