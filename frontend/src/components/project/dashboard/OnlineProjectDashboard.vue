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

    <DownloadInformationModal
      v-if="isOpenDownloadReportModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenDownloadReportModal')"
    />

    <ExpertFilterModal
      v-if="isOpenExpertFilterModal"
      :project-presets="currentProject.expert_presets"
      @add-expert-filter="addExpertFilterToProject"
      @close="toggleWidgetsModal('isOpenExpertFilterModal')"
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

    <OnlineDashboardControlPanel
      :sort-value="sortValue"
      :downloading-instant-report="downloadingInstantReport"
      @open-modal="toggleWidgetsModal"
      @download-report="downloadReport"
      @set-sorting-value="setSortingValue"
      @open-widgets-list-modal="toggleWidgetsModal('isOpenWidgetsModal')"
    />

    <PresetsBar
      :presets="currentPresets"
      class="presets-chips"
      @cancel-preset="cancelPreset"
      @clear-all-presets="clearAllPresets"
    />

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

import TotalResults from '@/components/TotalResults'
import SearchResults from '@/components/SearchResults'
import PresetsBar from '@components/expert-filter/PresetsBar'
import WidgetsListModal from '@/components/widgets/modals/WidgetsListModal'
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'
import OnlineFiltersModal from '@/components/project/modals/online/OnlineFiltersModal'
import DownloadInformationModal from '@/components/project/modals/DownloadInformationModal'
import OnlineDashboardControlPanel from '@/components/project/dashboard/OnlineDashboardControlPanel'
import OnlineProjectDashboardWidgets from '@/components/project/dashboard/OnlineProjectDashboardWidgets'

const {mapActions: mapExpertFilterActions, mapState: mapExpertFilterState} =
  createNamespacedHelpers('expertFilter')

const {mapActions: mapOnlineActions, mapState} =
  createNamespacedHelpers('online')

const {mapGetters: mapOnlineWidgetsGetters} =
  createNamespacedHelpers('online/widgets')
import ExpertFilterModal from '@/components/expert-filter/ExpertFilterModal'

export default {
  name: 'OnlineProjectDashboard',
  components: {
    PresetsBar,
    TotalResults,
    SearchResults,
    MainLayoutTitleBlock,
    WidgetsListModal,
    ExpertFilterModal,
    OnlineFiltersModal,
    InteractiveWidgetModal,
    DownloadInformationModal,
    OnlineDashboardControlPanel,
    OnlineProjectDashboardWidgets,
  },
  props: {
    currentProject: {type: [Array, Object], required: false},
  },
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenFilterModal: false,
      isOpenDownloadReportModal: false,
      isOpenExpertFilterModal: false,
      sortValue: 'Latest',
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
    ...mapExpertFilterState({
      presets: (state) => state.presets,
      newGroupId: (state) => state.newGroup.id,
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

    currentPresets() {
      return this.presets.filter((item) =>
        this.currentProject.expert_presets.includes(item.id)
      )
    },
    currentKeywords() {
      return this.currentProject?.keywords
    },
    currentAdditionalKeywords() {
      return this.currentProject?.additional_keywords
    },
    currentExcludeKeywords() {
      return this.currentProject?.ignore_keywords
    },
  },
  created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject?.start_search_date),
        new Date(this.currentProject?.end_search_date),
      ],
    })

    this[action.GET_PRESETS]()

    this.showResults()
  },
  methods: {
    ...mapActions([
      action.UPDATE_ADDITIONAL_FILTERS,
      action.CLEAR_INTERACTIVE_DATA,
    ]),
    ...mapOnlineActions([
      action.POST_SEARCH,
      action.UPDATE_PROJECT,
      action.POST_INTERACTIVE_WIDGETS,
      action.UPDATE_AVAILABLE_WIDGETS,
      action.GET_INSTANT_REPORT,
    ]),
    ...mapExpertFilterActions([action.GET_PRESETS, action.CREATE_PRESET]),
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
          project_pk: this.currentProject.id,
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
          ...this.interactiveDataModal?.data,
          page_number: page,
          posts_per_page: countPosts,
        },
      })
    },

    async updateAvailableWidgets(data) {
      await this[action.UPDATE_AVAILABLE_WIDGETS](data)
      this.toggleWidgetsModal('isOpenWidgetsModal')
    },

    async addExpertFilterToProject(presets) {
      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: presets},
      })

      this.toggleWidgetsModal('isOpenExpertFilterModal')
    },

    async clearAllPresets() {
      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: []},
      })
    },

    async cancelPreset(presetId) {
      const presetsIds = this.currentPresets.map(({id}) => id)
      const remainingPresets = presetsIds.filter((id) => id !== presetId)

      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: remainingPresets},
      })
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

.presets-chips {
  margin-top: 24px;
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
</style>
