<template>
  <div :class="['search-result-wrapper', `${routerName}-page`]">
    <div v-if="loading || searchLoading" class="spinner-wrapper">
      <BaseSpinner :isHaveLabel="true" />
    </div>

    <div
      v-if="!loading && searchData.length"
      class="search-result-cards scroll"
    >
      <social-post-card
        v-for="(item, index) in searchData"
        :key="'result' + index"
        :post-id="item.id"
        :is-clipping-post="selectedClippingElement(item.id)"
        :widget-id="clippingWidgetId"
        :project-id="currentProject.id"
        :img="cardImg(item)"
        :count-favorites="item.count_favorites"
        :count-replies="item.count_replies"
        :count-retweets="item.count_retweets"
        :date="item.creation_date"
        :language="item.language"
        :location-string="item.locationString"
        :sentiment="item.sentiment_vote"
        :text="item.text"
        :user-alias="item.user_alias"
        :user-name="item.user_name"
        class="clipping-card"
      />
    </div>

    <div v-if="!loading && searchData.length" class="pagination-wrapper">
      <BaseDropdown name="posts-on-page" :selected-value="countPosts">
        <div
          v-for="(item, index) in postsOnPage"
          :key="'drop' + index"
          @click="updatePostsCount(item)"
        >
          {{ item }}
        </div>
      </BaseDropdown>

      <VPagination
        v-model="page"
        :pages="this.numberOfPages"
        :range-size="1"
        active-color="#fcedf3"
        :container-class="'pagination'"
        @update:modelValue="pageChangeHandler"
      />
    </div>

    <div v-if="step && !searchData.length" class="no-results">
      <CreateWorkspaceRightSide :step="currentStep" />
      <h3 v-if="this.isSearchPerformed" class="no-results__text">
        No news for your request &#128546;
      </h3>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapState} from 'vuex'
import {get} from '@store/constants'
import {lowerFirstLetter} from '@/lib/utilities'

import VPagination from '@hennge/vue3-pagination'
import '@hennge/vue3-pagination/dist/vue3-pagination.css'

import BaseSpinner from '@/components/BaseSpinner'
import BaseDropdown from '@/components/BaseDropdown'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import SocialPostCard from '@/components/SocialPostCard'

export default {
  name: 'SocialSearchResults',
  components: {
    BaseDropdown,
    CreateWorkspaceRightSide,
    BaseSpinner,
    VPagination,
    SocialPostCard,
  },
  emits: ['update-page', 'update-posts-count', 'add-sorting-value'],
  props: {
    currentProject: {
      type: [Array, Object],
      default: () => [],
    },
    clippingContent: {
      type: [Array, Object],
      default: () => [],
    },
    isShowCalendar: {
      type: Boolean,
      default: true,
    },
    searchLoading: {
      type: Boolean,
      default: false,
    },
    step: {
      type: String,
      default: '',
    },
  },
  data() {
    return {
      isShow: false,
      clippingElements: [],
      isOpenDropdown: false,
      page: 1,
      countPosts: 20,
      postsOnPage: [20, 50, 100],
      clippingValue: [],
    }
  },
  computed: {
    ...mapState(['isSearchPerformed']),
    ...mapGetters({
      searchData: get.SEARCH_DATA,
      loading: get.LOADING,
      additionalFilters: get.ADDITIONAL_FILTERS,
      numberOfPages: get.PAGES_NUMBER,
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    routerName() {
      return this.$route.name.toLowerCase()
    },

    clippingWidgetId() {
      return this.availableWidgets?.clipping_feed_content.id || 0
    },
    currentStep() {
      return this.isSearchPerformed ? `${this.step}preview` : this.step
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    lowerFirstLetter,
    updatePostsCount(val) {
      this.countPosts = val
      this.$emit('show-results', this.page, this.countPosts)
    },
    pageChangeHandler() {
      this.$emit('show-results', this.page, this.countPosts)
    },
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    formatDate(date) {
      return date.toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
    selectedClippingElement(id) {
      return this.clippingContent.some((el) => el.post__id === id)
    },
    cardImg(item) {
      let images = [
        item.entry_media_content_url,
        item.entry_media_thumbnail_url,
        item.feed_image_href,
        item.feed_image_link,
      ]
      return images.filter((el) => el !== 'None')[0] || 'None'
    },
  },
}
</script>

<style lang="scss" scoped>
.search-result-wrapper {
  display: flex;
  flex-direction: column;
  align-items: flex-start;

  width: 100%;
  height: 100%;

  color: var(--typography-title-color);
}

.search-page {
  position: absolute;
  right: 0;
  top: 0;

  border-left: var(--border-primary);

  height: 100%;
  width: 45vw;
  padding: 80px 32px 0 15px;

  color: var(--typography-title-color);
  background-color: var(--background-secondary-color);
}

.analytics-page {
  height: 100%;
}

.pagination-wrapper {
  display: flex;
  justify-content: space-between;

  width: 100%;
  padding: 12px;
}
.spinner-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100%;
  min-height: 100px;
  margin-bottom: 80px;
}

.search-result-cards {
  overflow: auto;

  flex-grow: 1;
  width: 100%;
}

@media screen and (max-width: 1000px) {
  .search-result-wrapper {
    align-items: flex-end;
  }

  .search-result-card {
    margin: 0 0 10px 0;
  }
}

.no-results {
  flex-grow: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  width: 100%;
  height: 100%;

  &__text {
    margin-top: 32px;

    font-weight: 500;
    font-size: 18px;
  }
}
</style>

<style lang="scss">
.pagination {
  display: flex;
  gap: 4px;

  .PaginationControl {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 20px;
    height: 20px;

    background: var(--background-secondary-color);
    border: var(--border-primary);
    border-radius: 6px;

    color: var(--typography-title-color);

    .Control {
      fill: #333333;
    }

    .Control-active {
      fill: var(--typography-primary-color);
    }
  }

  .Page {
    display: flex;
    justify-content: center;
    align-items: center;

    width: 32px;
    height: 22px;

    background: var(--primary-active-color);
    border: var(--border-primary);
    border-radius: 6px;

    color: var(--typography-primary-color);
  }
}

.clipping-card {
  margin-bottom: 10px;

  &:last-child {
    margin-bottom: 0;
  }
}
</style>
