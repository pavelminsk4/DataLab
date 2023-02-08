<template>
  <div class="analytics" v-if="currentProject">
    <WidgetsListModal
      v-if="isOpenWidgetsModal"
      :project-id="currentProject.id"
      @close="toggleWidgetsModal('isOpenWidgetsModal')"
    />

    <AllDimensionsModal
      v-if="isOpenDimensionModal"
      :project-id="currentProject.id"
      :current-project="currentProject"
      @update-search-results="showResults"
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
      :hint="currentProject.note"
      :search-results="numberOfPosts"
    >
      <div class="analytics-menu">
        <BaseDropdown title="Sort by" id="sortBy" :selected-value="sortValue">
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
    </NavigationBar>

    <WidgetsView
      :project-id="currentProject.id"
      :currentProject="currentProject"
      @update-page="showResults"
      @update-posts-count="showResults"
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
import WidgetsListModal from '@/components/project/modals/WidgetsListModal'
import DimensionsIcon from '@/components/icons/DimensionsIcon'
import AllDimensionsModal from '@/components/project/modals/AllDimensionsModal'
import ReportsUploadIcon from '@/components/icons/ReportsUploadIcon'
import DownloadReportModal from '@/components/project/modals/DownloadReportModal'
import InstantReportModal from '@/components/project/modals/InstantReportModal'
import BaseDropdown from '@/components/BaseDropdown'

export default {
  name: 'AnalyticsScreen',
  components: {
    BaseDropdown,
    InstantReportModal,
    DownloadReportModal,
    ReportsUploadIcon,
    AllDimensionsModal,
    DimensionsIcon,
    WidgetsListModal,
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
  emits: ['update-page', 'update-posts-count'],
  data() {
    return {
      isOpenWidgetsModal: false,
      isOpenDimensionModal: false,
      isOpenDownloadReportModal: false,
      isOpenInstantReportModal: false,
      sortValue: '',
      sortingValue: '',
    }
  },
  created() {
    this[action.GET_AVAILABLE_WIDGETS](this.currentProject.id)

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
      console.log(this.numberOfPosts)
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
      action.GET_AVAILABLE_WIDGETS,
    ]),
    setSortingValue(item) {
      this.sortValue = item
      this.showResults()
    },
    toggleWidgetsModal(val) {
      this.togglePageScroll(false)
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
  },
}
</script>

<style lang="scss" scoped>
.analytics {
  margin: 24px 0 0 20px;
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
