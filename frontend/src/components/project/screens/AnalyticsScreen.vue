<template>
  <div class="analytics-wrapper">
    <InteractiveWidgetModal
      v-if="isOpenInteractiveModal"
      :widget-id="widgetId"
      :current-project="currentProject"
      class="interactive-widgets"
      @update-page="updatePageAndCountPosts"
      @update-posts-count="updatePageAndCountPosts"
      @close="closeInteractiveModal"
    />

    <WidgetsListModal
      v-if="isOpenWidgetsModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenWidgetsModal')"
      @update-available-widgets="updateAvailableWidgets"
    />

    <OnlineDimensionsModal
      v-if="isOpenDimensionModal"
      :project-id="currentProject.id"
      :current-project="currentProject"
      @update-search-results="showResults"
      @close="toggleWidgetsModal('isOpenDimensionModal')"
      @close-modal="toggleWidgetsModal('isOpenDimensionModal')"
    />

    <DownloadReportModal
      v-if="isOpenDownloadReportModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenDownloadReportModal')"
    />

    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routName: 'OnlineWorkspace',
      }"
    >
      <div class="search-results">{{ numberOfPosts }} results</div>
    </MainLayoutTitleBlock>

    <div class="analytics-menu">
      <BaseDropdown
        title="Sort by"
        name="sort-posts"
        :selected-value="sortValue"
      >
        <div
          v-for="(item, index) in sortingList"
          :key="item + index"
          @click="setSortingValue(item)"
        >
          {{ item }}
        </div>
      </BaseDropdown>

      <div class="menu-buttons">
        <BaseButton
          :is-not-background="true"
          class="button-upload"
          @click="toggleWidgetsModal('isOpenDownloadReportModal')"
        >
          <ReportsUploadIcon /> Download Report
        </BaseButton>

        <div class="navigation-bar">
          <BaseButton
            class="button"
            @click="toggleWidgetsModal('isOpenWidgetsModal')"
          >
            <PlusIcon class="icon" />
            Add Widgets
          </BaseButton>

          <DimensionsIcon
            class="dimensions-button"
            @click="toggleWidgetsModal('isOpenDimensionModal')"
          />
        </div>
      </div>
    </div>

    <WidgetsView
      :project-id="currentProject.id"
      :currentProject="currentProject"
      @update-page="showResults"
      @open-interactive-widget="openInteractiveWidgetModal"
      @open-sentiment-interactive-widget="openSentimentInteractiveWidgetModal"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsView from '@/components/project/widgets/WidgetsView'
import BaseButton from '@/components/common/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsListModal from '@/components/widgets/modals/WidgetsListModal'
import DimensionsIcon from '@/components/icons/DimensionsIcon'
import OnlineDimensionsModal from '@/components/project/modals/online/OnlineDimensionsModal'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import DownloadReportModal from '@/components/project/modals/DownloadReportModal'
import BaseDropdown from '@/components/BaseDropdown'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

export default {
  name: 'AnalyticsScreen',
  components: {
    InteractiveWidgetModal,
    MainLayoutTitleBlock,
    BaseDropdown,
    DownloadReportModal,
    ReportsUploadIcon,
    OnlineDimensionsModal,
    DimensionsIcon,
    WidgetsListModal,
    PlusIcon,
    BaseButton,
    WidgetsView,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  emits: ['update-page', 'update-posts-count'],
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenDimensionModal: false,
      isOpenDownloadReportModal: false,
      sortValue: '',
      sortingValue: '',
      isOpenInteractiveModal: false,
      widgetId: null,
      page: 1,
      countPosts: 4,
      fieldName: null,
      value: null,
      sentiment: null,
      source: null,
    }
  },
  created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject.start_search_date),
        new Date(this.currentProject.end_search_date),
      ],
    })

    this.showResults()
  },
  computed: {
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      searchData: get.SEARCH_DATA,
      numberOfPosts: get.POSTS_NUMBER,
    }),
    currentKeywords() {
      return this.currentProject?.keywords
    },
    currentAdditionalKeywords() {
      return this.currentProject?.additional_keywords
    },
    currentExcludeKeywords() {
      return this.currentProject?.ignore_keywords
    },
    sortingList() {
      return ['country', 'language', 'source']
    },
    sortingValueProxy: {
      get() {
        return this.sortingValue
      },
      set(value) {
        this.sortingValue = value
      },
    },
  },
  methods: {
    ...mapActions([
      action.POST_SEARCH,
      action.UPDATE_ADDITIONAL_FILTERS,
      action.POST_INTERACTIVE_WIDGETS,
      action.CLEAR_INTERACTIVE_DATA,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    setSortingValue(item) {
      this.sortValue = item
      this.showResults()
    },
    toggleWidgetsModal(val) {
      this.togglePageScroll(false)
      this[val] = !this[val]
    },
    showResults(pageNumber, numberOfPosts) {
      try {
        this[action.POST_SEARCH]({
          keywords: this.currentKeywords || this.keywords?.keywords,
          additions:
            this.currentAdditionalKeywords ||
            this.keywords?.additional_keywords,
          exceptions:
            this.currentExcludeKeywords || this.keywords?.ignore_keywords,
          country: this.currentProject?.country_filter || [],
          language: this.currentProject?.language_filter || [],
          sentiment: this.currentProject?.sentiment_filter || [],
          date_range: [
            this.currentProject?.start_search_date,

            this.currentProject?.end_search_date,
          ],
          source: this.currentProject?.source_filter || [],
          author: this.currentProject?.author_filter || [],
          posts_per_page: numberOfPosts || 20,
          page_number: pageNumber || 1,
          sort_posts: this.sortValue || [],
          country_dimensions: this.currentProject.country_dimensions,
          language_dimensions: this.currentProject.language_dimensions,
          source_dimensions: this.currentProject.source_dimensions,
          author_dimensions: this.currentProject.author_dimensions,
          sentiment_dimensions: this.currentProject.sentiment_dimensions,
        })
      } catch (e) {
        console.log(e)
      }
    },
    showInteractiveData(widgetId, data) {
      this.widgetId = widgetId

      this.isOpenInteractiveModal = true

      this[action.POST_INTERACTIVE_WIDGETS]({
        projectId: this.currentProject.id,
        widgetId: widgetId,
        data: {
          ...data,
          page_number: this.page,
          posts_per_page: this.countPosts,
        },
      })
    },

    openInteractiveWidgetModal(val, widgetId, fieldName) {
      this.fieldName = fieldName
      this.value = val
      this.showInteractiveData(widgetId, {
        [fieldName]: val,
      })
    },

    openSentimentInteractiveWidgetModal(source, sentiment, widgetId) {
      this.source = source
      this.sentiment = sentiment

      this.showInteractiveData(widgetId, {
        s_value: source,
        sentiment: sentiment,
      })
    },

    closeInteractiveModal() {
      this.togglePageScroll(false)
      this.isOpenInteractiveModal = false
      this[action.CLEAR_INTERACTIVE_DATA]()
    },

    updatePageAndCountPosts(page, countPosts) {
      this.page = page
      this.countPosts = countPosts

      this.showInteractiveData(this.widgetId, {
        [this.fieldName]: this.value,
        s_value: this.source,
        sentiment: this.sentiment,
        page_number: page,
        posts_per_page: countPosts,
      })
    },

    async updateAvailableWidgets(data) {
      await this[action.UPDATE_AVAILABLE_WIDGETS](data)
      this.toggleWidgetsModal('isOpenWidgetsModal')
    },
  },
}
</script>

<style lang="scss" scoped>
.analytics-wrapper {
  display: flex;
  flex-direction: column;

  height: 100%;
  margin-top: 20px;
}

.interactive-widgets {
  z-index: 1010;
}

.search-results {
  font-style: normal;
  font-weight: 600;
  font-size: 14px;
  line-height: 20px;
  color: var(--typography-secondary-color);
}

.analytics-menu {
  display: flex;
  justify-content: space-between;

  width: 100%;

  .menu-buttons {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 40px;

    .navigation-bar {
      display: flex;
      justify-content: flex-end;
      align-items: center;
      gap: 22px;

      .button {
        width: 155px;

        .icon {
          margin-right: 10px;
        }
      }
    }
  }
}

.button-upload {
  gap: 15px;
  padding: 0 20px;

  font-size: 14px;
  line-height: 20px;
}

.dimensions-button {
  cursor: pointer;

  &:hover {
    color: var(--primary-color);
  }
}
</style>
