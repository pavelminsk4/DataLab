<template>
  <div :class="['search-result-wrapper', `${routerName}-page`]">
    <div v-if="loading || searchLoading" class="spinner-wrapper">
      <BaseSpinner :isHaveLabel="true" />
    </div>

    <div
      v-if="!loading && searchData.length"
      class="search-result-cards scroll"
    >
      <ClippingCard
        v-for="(item, index) in searchData"
        :key="'result' + index"
        :id="item.id"
        :img="cardImg(item)"
        :title="item.entry_title"
        :country="item.feedlink__country"
        :entry-link="item.entry_links_href"
        :summary="item.entry_summary"
        :sentiment="item.sentiment"
        :published="item.entry_published"
        :source-link="item.feedlink__sourceurl"
        :source="item.feedlink__source1"
        :language="item.feed_language__language"
        :potential-reach="item.feedlink__alexaglobalrank"
        :is-checkbox-clipping-widget="isCheckboxClippingWidget"
        :current-project="currentProject"
        :clipping-element="selectedClippingElement(item.id)"
        class="clipping-card"
        @add-element="addClippingElement"
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
      <CreateWorkspaceRightSide step="step3" />
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'
import {lowerFirstLetter} from '@/lib/utilities'

import VPagination from '@hennge/vue3-pagination'
import '@hennge/vue3-pagination/dist/vue3-pagination.css'

import BaseSpinner from '@/components/BaseSpinner'
import ClippingCard from '@/components/ClippingCard'
import BaseDropdown from '@/components/BaseDropdown'
import CreateWorkspaceRightSide from '@/components/workspace/CreateWorkspaceRightSide'

export default {
  name: 'SearchResults',
  components: {
    BaseDropdown,
    ClippingCard,
    CreateWorkspaceRightSide,
    BaseSpinner,
    VPagination,
  },
  emits: ['update-page', 'update-posts-count', 'add-sorting-value'],
  props: {
    currentProject: {
      type: [Array, Object],
      default: () => [],
    },
    isCheckboxClippingWidget: {
      type: Boolean,
      default: false,
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
    ...mapState([
      'searchData',
      'loading',
      'additionalFilters',
      'numberOfPages',
    ]),
    routerName() {
      return this.$route.name.toLowerCase()
    },
  },
  created() {
    document.addEventListener('click', this.close)
  },
  methods: {
    lowerFirstLetter,
    updatePostsCount(val) {
      this.countPosts = val
      this.$emit('update-posts-count', this.page, this.countPosts)
    },
    pageChangeHandler() {
      this.$emit('update-page', this.page, this.countPosts)
    },
    ...mapActions([
      action.REFRESH_DISPLAY_CALENDAR,
      action.DELETE_CLIPPING_FEED_CONTENT,
      action.CREATE_CLIPPING_FEED_CONTENT_WIDGET,
    ]),
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
    addClippingElement(postId, checkedElement) {
      if (checkedElement) {
        this.removeSelectedFilter(postId)
      } else {
        this.createClippingWidget({
          project: this.currentProject.id,
          post: postId,
        })
      }
    },
    async removeSelectedFilter(postId) {
      await this[action.DELETE_CLIPPING_FEED_CONTENT]({
        projectId: this.currentProject.id,
        postId: postId,
      })
    },
    async createClippingWidget(newPost) {
      await this[action.CREATE_CLIPPING_FEED_CONTENT_WIDGET]({
        posts: [newPost],
        projectId: this.currentProject.id,
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
  min-height: 100%;

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
