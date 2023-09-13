<template>
  <div v-if="currentProject" class="project-dashboard-wrapper">
    <InteractiveWidgetModal
      v-if="inreractiveDataModal.isShow"
      :widget-id="widgetId"
      :current-project="currentProject"
      class="interactive-widgets"
      @show-results="updatePageAndCountPosts"
      @close="closeInteractiveModal"
    />

    <WidgetsListModal
      v-if="openModal === 'WidgetsListModal'"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal(null)"
      @update-available-widgets="updateAvailableWidgets"
    />

    <SocialFiltersModal
      v-if="openModal === 'SocialFiltersModal'"
      :project-id="currentProject.id"
      :current-project="currentProject"
      @update-search-results="showResults"
      @close="toggleWidgetsModal(null)"
      @close-modal="toggleWidgetsModal(null)"
    />

    <DownloadReportModal
      v-if="openModal === 'DownloadReportModal'"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal(null)"
    />

    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routeName: 'SocialWorkspace',
      }"
      :should-translate="false"
    >
      <TotalResults :total-results="numberOfPosts" />
    </MainLayoutTitleBlock>

    <div class="analytics-menu">
      <BaseDropdown
        title="Sort by"
        name="sort-posts"
        :selected-value="sortValue"
      >
        <CustomText
          v-for="(item, index) in sortingList"
          :key="item + index"
          :text="item"
          @click="setSortingValue(item)"
        />
      </BaseDropdown>

      <div class="menu-buttons">
        <BaseButton
          :is-not-background="true"
          class="button-upload"
          @click="toggleWidgetsModal('DownloadReportModal')"
        >
          <ReportsUploadIcon />
          <CustomText text="Download Report" />
        </BaseButton>

        <div class="navigation-bar">
          <BaseButton
            class="button"
            @click="toggleWidgetsModal('WidgetsListModal')"
          >
            <PlusIcon class="icon" />
            <CustomText text="Add Widgets" />
          </BaseButton>

          <FiltersIcon
            class="filters-button"
            @click="toggleWidgetsModal('SocialFiltersModal')"
          />
        </div>
      </div>
    </div>

    <div class="analytics-wrapper">
      <SearchResults
        module-name="Social"
        :clipping-content="clippingData"
        :is-checkbox-clipping-widget="true"
        class="search-results"
        @show-results="showResults"
      />

      <SocialProjectDashboardWidgets
        :project-id="currentProject.id"
        :module-name="currentProject.source"
        @update-available-widgets="updateAvailableWidgets"
      />
    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters, createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import CustomText from '@/components/CustomText'
import SearchResults from '@/components/SearchResults'
import SocialProjectDashboardWidgets from '@/components/project/dashboard/SocialProjectDashboardWidgets'
import BaseButton from '@/components/common/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsListModal from '@/components/widgets/modals/WidgetsListModal'
import FiltersIcon from '@/components/icons/FiltersIcon'
import SocialFiltersModal from '@/components/project/modals/social/SocialFiltersModal'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import DownloadReportModal from '@/components/project/modals/social/DownloadReportModal'
import BaseDropdown from '@/components/BaseDropdown'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'
import TotalResults from '@/components/TotalResults'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'SocialProjectDashboard',
  components: {
    InteractiveWidgetModal,
    MainLayoutTitleBlock,
    BaseDropdown,
    DownloadReportModal,
    ReportsUploadIcon,
    SocialFiltersModal,
    FiltersIcon,
    WidgetsListModal,
    PlusIcon,
    BaseButton,
    SocialProjectDashboardWidgets,
    SearchResults,
    TotalResults,
    CustomText,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      openModal: null,
      sortValue: '',
      sortingValue: '',
      widgetId: null,
    }
  },
  computed: {
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      searchData: get.SEARCH_DATA,
      numberOfPosts: get.POSTS_NUMBER,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
      inreractiveDataModal: get.INTERACTIVE_DATA_MODAL,
      department: get.DEPARTMENT,
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
  created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject.start_search_date),
        new Date(this.currentProject.end_search_date),
      ],
    })

    this.showResults()
  },
  methods: {
    ...mapActions([
      action.UPDATE_ADDITIONAL_FILTERS,
      action.CLEAR_INTERACTIVE_DATA,
    ]),
    ...mapSocialActions([
      action.POST_SEARCH,
      action.POST_INTERACTIVE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
    ]),
    setSortingValue(item) {
      this.sortValue = item
      this.showResults()
    },
    toggleWidgetsModal(val) {
      this.openModal = val
      this.togglePageScroll(this.openModal)
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
          query_filter: this.query || this.currentProject?.query_filter,
          department_id: this.department.id,
          expert_mode: this.currentProject.expert_mode,
        })
      } catch (e) {
        console.error(e)
      }
    },
    openInteractiveWidgetModal(val, widgetId, fieldName) {
      this.widgetId = widgetId

      this.toggleWidgetsModal('InteractiveWidgetModal')

      this[action.POST_INTERACTIVE_WIDGETS]({
        projectId: this.currentProject.id,
        widgetId: widgetId,
        data: {
          [fieldName]: val,
          page_number: 1,
          posts_per_page: 20,
        },
      })
    },
    async updateAvailableWidgets(data) {
      await this[action.UPDATE_AVAILABLE_WIDGETS](data)
      this.toggleWidgetsModal(null)
    },

    closeInteractiveModal() {
      this.togglePageScroll(false)
      this[action.CLEAR_INTERACTIVE_DATA]()
    },

    updatePageAndCountPosts(page, countPosts) {
      this[action.POST_INTERACTIVE_WIDGETS]({
        projectId: this.inreractiveDataModal.projectId,
        widgetId: this.inreractiveDataModal.widgetId,
        data: {
          ...this.inreractiveDataModal.data,
          page_number: page,
          posts_per_page: countPosts,
        },
      })
    },
  },
}
</script>

<style lang="scss" scoped>
.project-dashboard-wrapper {
  display: flex;
  flex-direction: column;

  height: 100%;
  margin-top: 20px;
}

.analytics-wrapper {
  display: flex;
  gap: 40px;

  height: 100%;
  margin-top: 20px;

  .search-results {
    width: 100%;
    height: calc(100vh - 255px);
  }
}

.interactive-widgets {
  z-index: 1010;
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

.filters-button {
  cursor: pointer;

  &:hover {
    color: var(--primary-color);
  }
}
</style>
