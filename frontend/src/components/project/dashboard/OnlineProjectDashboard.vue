<template>
  <div v-if="currentProject" class="project-dashboard-wrapper">
    <InteractiveWidgetModal
      v-if="interactiveDataModal.isShow"
      :widget-id="widgetId"
      :current-project="currentProject"
      :module-name="currentProject.source"
      :clipping-content="clippingData.data"
      class="interactive-widgets"
      @show-results="updatePageAndCountPosts"
      @close="closeInteractiveModal"
    />

    <WidgetsListModal
      v-if="isOpenWidgetsModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenWidgetsModal')"
      @update-available-widgets="updateAvailableWidgets"
    />

    <OnlineFiltersModal
      v-if="isOpenFilterModal"
      :project-id="currentProject.id"
      :current-project="currentProject"
      @update-search-results="showResults"
      @close="toggleWidgetsModal('isOpenFilterModal')"
      @close-modal="toggleWidgetsModal('isOpenFilterModal')"
    />

    <!-- <DownloadReportModal
      v-if="isOpenDownloadReportModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenDownloadReportModal')"
    /> -->

    <DownloadInformationModal
      v-if="isOpenDownloadReportModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenDownloadReportModal')"
    />

    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routeName: 'OnlineWorkspace',
      }"
      :should-translate="false"
    >
      <TotalResults v-if="searchData.length" :total-results="numberOfPosts" />
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
          @click="downloadReport"
        >
          <component
            :is="downloadReportButtonIcon"
            style="--spinner-width: 16px"
          ></component>
          <CustomText text="Download Report" />
        </BaseButton>

        <div class="navigation-bar">
          <BaseButton
            class="button"
            @click="toggleWidgetsModal('isOpenWidgetsModal')"
          >
            <PlusIcon class="icon" />
            <CustomText text="Add Widgets" />
          </BaseButton>

          <FiltersIcon
            class="filters-button"
            @click="toggleWidgetsModal('isOpenFilterModal')"
          />
        </div>
      </div>
    </div>

    <div class="dashboard-wrapper">
      <SearchResults
        module-name="Online"
        :search-loading="isLoadingResults"
        :is-checkbox-clipping-widget="true"
        :clipping-content="clippingData.data"
        class="search-results"
        @show-results="showResults"
      />

      <OnlineProjectDashboardWidgets
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

import OnlineProjectDashboardWidgets from '@/components/project/dashboard/OnlineProjectDashboardWidgets'
import BaseButton from '@/components/common/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsListModal from '@/components/widgets/modals/WidgetsListModal'
import FiltersIcon from '@/components/icons/FiltersIcon'
import OnlineFiltersModal from '@/components/project/modals/online/OnlineFiltersModal'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
// import DownloadReportModal from '@/components/project/modals/online/DownloadReportModal'
import BaseDropdown from '@/components/BaseDropdown'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'
import TotalResults from '@/components/TotalResults'
import CustomText from '@/components/CustomText'
import SearchResults from '@/components/SearchResults'
import DownloadInformationModal from '@/components/project/modals/DownloadInformationModal'
import BaseButtonSpinner from '@/components/BaseButtonSpinner'

const {mapActions: mapOnlineActions, mapState} =
  createNamespacedHelpers('online')

const {mapGetters: mapOnlineWidgetsGetters} =
  createNamespacedHelpers('online/widgets')

export default {
  name: 'OnlineProjectDashboard',
  components: {
    OnlineProjectDashboardWidgets,
    InteractiveWidgetModal,
    MainLayoutTitleBlock,
    BaseDropdown,
    // DownloadReportModal,
    ReportsUploadIcon,
    OnlineFiltersModal,
    FiltersIcon,
    WidgetsListModal,
    PlusIcon,
    BaseButton,
    TotalResults,
    CustomText,
    SearchResults,
    DownloadInformationModal,
    BaseButtonSpinner,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenFilterModal: false,
      isOpenDownloadReportModal: false,
      sortValue: '',
      sortingValue: '',
      widgetId: null,
      page: 1,
      countPosts: 4,
      fieldName: null,
      value: null,
      sentiment: null,
      source: null,
      isLoadingResults: false,
    }
  },
  computed: {
    ...mapState({
      downloadingInstantReport: (state) => state.downloadingInstantReport,
    }),
    ...mapOnlineWidgetsGetters({
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
    }),
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      searchData: get.SEARCH_DATA,
      numberOfPosts: get.POSTS_NUMBER,
      interactiveDataModal: get.INTERACTIVE_DATA_MODAL,
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

    downloadReportButtonIcon() {
      return this.downloadingInstantReport
        ? 'BaseButtonSpinner'
        : 'ReportsUploadIcon'
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
    ...mapOnlineActions([
      action.POST_SEARCH,
      action.POST_INTERACTIVE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_INSTANT_REPORT,
    ]),
    setSortingValue(item) {
      this.sortValue = item
      this.showResults()
    },
    toggleWidgetsModal(val) {
      this.togglePageScroll(false)
      this[val] = !this[val]
    },
    async showResults(pageNumber, numberOfPosts) {
      this.isLoadingResults = true
      try {
        await this[action.POST_SEARCH]({
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
          query_filter: this.currentProject.query_filter,
          department_id: this.department.id,
          expert_mode: this.currentProject.expert_mode,
        })
      } catch (e) {
        console.error(e)
      } finally {
        this.isLoadingResults = false
      }
    },

    closeInteractiveModal() {
      this.togglePageScroll(false)
      this[action.CLEAR_INTERACTIVE_DATA]()
    },

    updatePageAndCountPosts(page, countPosts) {
      this[action.POST_INTERACTIVE_WIDGETS]({
        projectId: this.interactiveDataModal.projectId,
        widgetId: this.interactiveDataModal.widgetId,
        data: {
          ...this.interactiveDataModal.data,
          page_number: page,
          posts_per_page: countPosts,
        },
      })
    },

    async updateAvailableWidgets(data) {
      await this[action.UPDATE_AVAILABLE_WIDGETS](data)
      this.toggleWidgetsModal('isOpenWidgetsModal')
    },

    async downloadReport() {
      if (!this.downloadingInstantReport) {
        try {
          this.toggleWidgetsModal('isOpenDownloadReportModal')
          const res = await this[action.GET_INSTANT_REPORT]({
            projectId: this.currentProject.id,
          })

          const anchor = document.createElement('a')
          anchor.href = res
          anchor.download = 'instant_report.pdf'

          document.body.appendChild(anchor)
          anchor.click()
          document.body.removeChild(anchor)
        } catch (error) {
          console.error(error)
        } finally {
          this.toggleWidgetsModal('isOpenDownloadReportModal')
        }
      }
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

.dashboard-wrapper {
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
