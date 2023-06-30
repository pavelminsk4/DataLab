<template>
  <div :class="['search-result-wrapper', `${routerName}-page`]">
    <div v-if="loading || searchLoading" class="spinner-wrapper">
      <BaseSpinner :isHaveLabel="true" />
    </div>

    <div
      v-if="!loading && searchData.length"
      :class="['search-result-cards scroll', `${routerName}-cards`]"
    >
      <component
        :is="postCard"
        v-for="(item, index) in searchData"
        :key="'result' + index"
        :is-clipping-post="selectedClippingElement(item.id)"
        :img="cardImg(item)"
        :post-details="item"
        :item-id="item.id"
        :is-status-show="false"
        class="clipping-card"
      />
    </div>

    <div v-if="!loading && searchData.length" class="pagination-wrapper">
      <PaginationControlPanel
        v-model="currentPage"
        :pages="numberOfPages"
        :posts-on-page="postsOnPage"
        :count-posts="countPosts"
        @update-page="updatePage"
      />
    </div>

    <div v-if="step && !searchData.length" class="no-results">
      <CreateWorkspaceRightSide :step="currentStep" />
      <h3 v-if="isSearchPerformed" class="no-results__text">
        No news for your request &#128546;
      </h3>
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import {action, get} from '@store/constants'
import {lowerFirstLetter} from '@/lib/utilities'

import BaseSpinner from '@/components/BaseSpinner'
import OnlinePostCard from '@/components/OnlinePostCard'
import SocialPostCard from '@/components/SocialPostCard'
import TFSPostCard from '@/components/TFSPostCard'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'
import PaginationControlPanel from '@/components/PaginationControlPanel'

export default {
  name: 'SearchResults',
  components: {
    OnlinePostCard,
    SocialPostCard,
    TFSPostCard,
    PaginationControlPanel,
    CreateWorkspaceRightSide,
    BaseSpinner,
  },
  emits: ['show-results'],
  props: {
    clippingContent: {type: [Array, Object], default: () => []},
    searchLoading: {type: Boolean, default: false},
    step: {type: String, default: ''},
    moduleName: {type: String, default: 'Online'},
  },
  data() {
    return {
      isShow: false,
      clippingElements: [],
      isOpenDropdown: false,
      clippingValue: [],
      currentPage: 1,
      countPosts: 20,
      postsOnPage: [20, 50, 100],
    }
  },
  computed: {
    ...mapState(['isSearchPerformed', 'newProject']),
    ...mapGetters({
      searchData: get.SEARCH_DATA,
      loading: get.LOADING,
      additionalFilters: get.ADDITIONAL_FILTERS,
      numberOfPages: get.PAGES_NUMBER,
    }),
    postCard() {
      return this.moduleName + 'PostCard'
    },
    routerName() {
      return this.$route.name.toLowerCase()
    },

    currentStep() {
      return this.isSearchPerformed ? `${this.step}preview` : this.step
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    ...mapActions([
      action.UPDATE_PROJECT_STATE,
      action.REFRESH_DISPLAY_CALENDAR,
    ]),
    lowerFirstLetter,
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
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
    updatePage(page, countPosts) {
      this.countPosts = countPosts
      this.$emit('show-results', page, countPosts)
      this[action.UPDATE_PROJECT_STATE]({
        searchFilters: {
          ...this.newProject.searchFilters,
          page_number: page,
          posts_per_page: countPosts,
        },
      })
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

.tfsworkspacestep3-cards {
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  gap: 32px;

  margin: 15px 0;
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

  height: 1000px;
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
}

.clipping-card {
  margin-bottom: 10px;

  &:last-child {
    margin-bottom: 0;
  }
}
</style>
