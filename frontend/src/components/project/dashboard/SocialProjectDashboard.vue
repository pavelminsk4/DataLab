<template>
  <div v-if="currentProject" class="project-dashboard-wrapper">
    <InteractiveWidgetModal
      v-if="interactiveDataModal.isShow"
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

    <DownloadInformationModal
      v-if="openModal === 'DownloadReportModal'"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal(null)"
    />

    <ExpertFilterModal
      v-if="openModal === 'ExpertFilterModal'"
      :project-presets="currentProject.expert_presets"
      @add-expert-filter="addExpertFilterToProject"
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
      <TotalResults v-if="searchData.length" :total-results="numberOfPosts" />
    </MainLayoutTitleBlock>

    <SocialDashboardControlPanel
      :downloading-instant-report="downloadingInstantReport"
      @open-modal="toggleWidgetsModal"
      @download-report="downloadReport"
      @set-sorting-value="setSortingValue"
      @open-widgets-list-modal="toggleWidgetsModal('WidgetsListModal')"
    />

    <PresetsBar
      :presets="currentPresets"
      class="presets-chips"
      @cancel-preset="cancelPreset"
      @clear-all-presets="clearAllPresets"
    />

    <div class="dashboard-wrapper">
      <SearchResults
        module-name="Social"
        :search-loading="isLoadingResults"
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

import TotalResults from '@components/TotalResults'
import SearchResults from '@components/SearchResults'
import PresetsBar from '@components/expert-filter/PresetsBar'
import WidgetsListModal from '@components/widgets/modals/WidgetsListModal'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ExpertFilterModal from '@components/expert-filter/ExpertFilterModal'
import InteractiveWidgetModal from '@components/modals/InteractiveWidgetModal'
import SocialFiltersModal from '@components/project/modals/social/SocialFiltersModal'
import DownloadInformationModal from '@components/project/modals/DownloadInformationModal'
import SocialDashboardControlPanel from '@components/project/dashboard/SocialDashboardControlPanel'
import SocialProjectDashboardWidgets from '@components/project/dashboard/SocialProjectDashboardWidgets'

const {mapActions: mapExpertFilterActions, mapState: mapExpertFilterState} =
  createNamespacedHelpers('expertFilter')

const {mapActions: mapSocialActions, mapState} =
  createNamespacedHelpers('social')

export default {
  name: 'SocialProjectDashboard',
  components: {
    PresetsBar,
    TotalResults,
    SearchResults,
    WidgetsListModal,
    ExpertFilterModal,
    SocialFiltersModal,
    MainLayoutTitleBlock,
    InteractiveWidgetModal,
    DownloadInformationModal,
    SocialDashboardControlPanel,
    SocialProjectDashboardWidgets,
  },
  props: {
    currentProject: {type: [Array, Object], required: true},
  },
  data() {
    return {
      openModal: null,
      sortValue: '',
      sortingValue: '',
      widgetId: null,
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
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      searchData: get.SEARCH_DATA,
      numberOfPosts: get.POSTS_NUMBER,
      clippingData: get.CLIPPING_FEED_CONTENT_WIDGET,
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
    currentPresets() {
      return this.presets.filter((item) =>
        this.currentProject.expert_presets.includes(item.id)
      )
    },
  },
  created() {
    this[action.UPDATE_ADDITIONAL_FILTERS]({
      date_range: [
        new Date(this.currentProject.start_search_date),
        new Date(this.currentProject.end_search_date),
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
    ...mapSocialActions([
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
      this.openModal = val
      this.togglePageScroll(this.openModal)
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
          query_filter: this.query || this.currentProject?.query_filter,
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

    async addExpertFilterToProject(presets) {
      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: presets},
      })

      this.toggleWidgetsModal('isOpenExpertFilterModal')
    },

    async cancelPreset(presetId) {
      const presetsIds = this.currentPresets.map(({id}) => id)
      const remainingPresets = presetsIds.filter((id) => id !== presetId)

      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: remainingPresets},
      })
    },

    async clearAllPresets() {
      await this[action.UPDATE_PROJECT]({
        projectId: this.currentProject?.id,
        data: {expert_presets: []},
      })
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

    async downloadReport() {
      if (!this.downloadingInstantReport) {
        try {
          this.toggleWidgetsModal('DownloadReportModal')
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
          this.toggleWidgetsModal(null)
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

.presets-chips {
  margin-top: 24px;
}

.interactive-widgets {
  z-index: 1010;
}
</style>
