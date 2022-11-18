<template>
  <div v-if="currentProject">
    <WidgetsModal
      v-if="isOpenWidgetsModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenWidgetsModal')"
    />

    <AllDimensionsModal
      v-if="isOpenDimensionModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenDimensionModal')"
      @close-modal="toggleWidgetsModal('isOpenDimensionModal')"
    />

    <DownloadReportModal
      v-if="isOpenDownloadReportModal"
      @close="toggleWidgetsModal('isOpenDownloadReportModal')"
      @open-instant-template="
        openInstantTemplate(
          'isOpenDownloadReportModal',
          'isOpenInstantReportModal'
        )
      "
    />

    <InstantReportModal
      v-if="isOpenInstantReportModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenInstantReportModal')"
    />

    <NavigationBar
      v-if="currentProject"
      :title="currentProject.title"
      :hint="'Search by keywords and phrases '"
    >
      <BaseButton
        class="button-upload"
        @click="toggleWidgetsModal('isOpenDownloadReportModal')"
      >
        <ReportsUploadIcon /> Download Report
      </BaseButton>
    </NavigationBar>

    <div class="navigation-bar">
      <div
        class="dimensions-button"
        @click="toggleWidgetsModal('isOpenDimensionModal')"
      >
        <DimensionsIcon />
      </div>

      <BaseButton
        class="button"
        @click="toggleWidgetsModal('isOpenWidgetsModal')"
      >
        <PlusIcon class="icon" />
        Add Widgets
      </BaseButton>
    </div>

    <WidgetsView
      :project-id="currentProject.id"
      :currentProject="currentProject"
      @update-page="showResults"
      @update-posts="showResults"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import NavigationBar from '@/components/navigation/NavigationBar'
import WidgetsView from '@/components/project/widgets/WidgetsView'
import BaseButton from '@/components/buttons/BaseButton'
import PlusIcon from '@/components/icons/PlusIcon'
import WidgetsModal from '@/components/project/modals/WidgetsModal'
import DimensionsIcon from '@/components/icons/DimensionsIcon'
import AllDimensionsModal from '@/components/project/modals/AllDimensionsModal'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import DownloadReportModal from '@/components/project/modals/DownloadReportModal'
import InstantReportModal from '@/components/project/modals/InstantReportModal'

export default {
  name: 'AnalyticsScreen',
  components: {
    InstantReportModal,
    DownloadReportModal,
    ReportsUploadIcon,
    AllDimensionsModal,
    DimensionsIcon,
    WidgetsModal,
    PlusIcon,
    BaseButton,
    WidgetsView,
    NavigationBar,
  },
  props: {
    currentProject: {
      type: [Array, Object],
      required: false,
    },
  },
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenDimensionModal: false,
      isOpenDownloadReportModal: false,
      isOpenInstantReportModal: false,
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
  },
  methods: {
    ...mapActions([action.POST_SEARCH, action.UPDATE_ADDITIONAL_FILTERS]),
    toggleWidgetsModal(val) {
      this[val] = !this[val]
    },
    openInstantTemplate(downloadReportModal, instantModal) {
      this.toggleWidgetsModal(downloadReportModal)
      this.toggleWidgetsModal(instantModal)
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
          language: this.currentProject?.author_filter || [],
          sentiment: this.currentProject?.author_filter || [],
          date_range: [
            this.currentProject?.start_search_date,

            this.currentProject?.end_search_date,
          ],
          source: this.currentProject?.author_filter || [],
          author: this.currentProject?.author_filter || [],
          posts_per_page: numberOfPosts || 20,
          page_number: pageNumber || 1,
        })
      } catch (e) {
        console.log(e)
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.navigation-bar {
  display: flex;
  justify-content: flex-end;

  margin-top: 30px;

  .button {
    width: 155px;

    .icon {
      margin-right: 10px;
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
  display: flex;
  align-items: center;
  justify-content: center;

  cursor: pointer;

  margin-right: 10px;
  width: 40px;
  height: 40px;

  background: #29303d;
  border-radius: 8px;

  &:hover {
    background: var(--secondary-button-color);
  }
}
</style>
