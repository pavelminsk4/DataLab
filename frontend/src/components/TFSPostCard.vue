<template>
  <TFSPostCardLayout
    :sentiment="postDetails.sentiment || ''"
    :category="postDetails.category"
    :date="this.defaultDate(this.postDetails.entry_published)"
    :source="this.postDetails.feedlink__sourceurl"
    :post-image="img"
    :post-id="postDetails.id"
    :status="cardStatus"
    :is-related="isRelatedContent"
  >
    <template #header>
      <div class="post-card-header">
        <TFSCardStatuses
          v-if="isStatusShow"
          :status="cardStatus"
          :post-id="postDetails.id"
          :isBack="isBack"
          @change-status-card="changeStatusCard"
        />

        <div v-if="isRelatedContent" class="related">Related</div>
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

    <template #buttons>
      <div
        v-if="isWorkButtonShow"
        class="work-button"
        @click="$emit('open-modal')"
      >
        Take to work
      </div>
    </template>
  </TFSPostCardLayout>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'
import {defaultDate} from '@lib/utilities'

import OnlineIcon from '@/components/icons/OnlineIcon'
import TFSPostCardLayout from '@/components/twenty-four-seven/TFSPostCardLayout'
import TFSCardStatuses from '@/components/twenty-four-seven/TFSCardStatuses'

export default {
  name: 'TFSPostCard',
  components: {
    OnlineIcon,
    TFSPostCardLayout,
    TFSCardStatuses,
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
    changeStatusCard(newStatus) {
      this.$emit('change-status', this.itemId, newStatus, this.cardStatus)
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

.post-card-header {
  display: flex;
  justify-content: space-between;

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

.work-button {
  cursor: pointer;

  font-style: normal;
  font-weight: 500;
  font-size: 14px;
  line-height: 20px;
  color: var(--button-primary-color);
}
</style>
