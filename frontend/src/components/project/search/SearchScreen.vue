<template>
  <div v-if="currentProject">
    <WarningModal
      v-if="isWarningModalDisplayed"
      @close="isWarningModalDisplayed = false"
      @approve="() => updateProjectData(true)"
    >
      <CustomText tag="p" text="Recollect data for the project?" class="text" />
      <CustomText
        tag="p"
        text="If you click ‘Confirm’, the existing posts will be removed and the process of collecting posts will be restarted."
        class="text"
      />
    </WarningModal>

    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routeName: `${moduleName}Workspace`,
      }"
      :should-translate="false"
    >
      <TotalResults :total-results="numberOfPosts" />
    </MainLayoutTitleBlock>

    <div class="search-settings-wrapper">
      <div
        :class="['switcher', isExpertMode && 'switcher__active']"
        @click="switchTrigger"
      >
        <CustomText tag="span" text="Expert mode" />
        <BaseSwitcher label="Expert mode" :value="isExpertMode" />
      </div>
      <div class="search">
        <ExpertModeTab
          v-if="isExpertMode"
          :default-query="currentProject.query_filter"
          :start-date="startDate"
          :filters="filters"
          :is-keywords-fields-disable="!isAdmin"
          :module-name="moduleName"
          :is-current-project-created="isCurrentProjectCreated"
          @save-project="saveProject"
          @show-result="showResults"
          @update-query-filter="updateQueryFilter"
          class="expert-mode"
        />
        <SimpleModeTab
          v-else
          :module-name="moduleName"
          :main-keywords="currentKeywords"
          :exclude-keywords="currentExcludeKeywords"
          :additional-keywords="currentAdditionalKeywords"
          :current-project="currentProject"
          :is-disabled-button="!currentKeywords?.length"
          :expert-mode-test-test="currentProject?.query_filter"
          :is-expert-mode-set="currentProject.expert_mode && !isAdmin"
          :is-keywords-fields-disable="!isAdmin"
          @update-query-filter="updateQueryFilter"
          @save-project="saveProject"
          @show-result="showResults"
          @update-collection="updateKeywordsCollection"
        />
        <SearchResults
          :module-name="moduleName"
          :clipping-content="clippingContent"
          step="step3"
          class="search-section"
          @show-results="showResults"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters, mapActions} from 'vuex'
import moment from 'moment'
import {get, action} from '@store/constants'
import {expertModeFilters} from '@lib/constants'
import {isAllFieldsEmpty, areArraysEqual} from '@lib/utilities'

import CustomText from '@components/CustomText'
import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import SimpleModeTab from '@components/workspace/SimpleModeTab'
import SearchResults from '@components/SearchResults'
import BaseSwitcher from '@components/BaseSwitcher'
import ExpertModeTab from '@components/workspace/ExpertModeTab'
import TotalResults from '@components/TotalResults'
import WarningModal from '@components/modals/WarningModal'

export default {
  name: 'SearchScreen',
  components: {
    SearchResults,
    SimpleModeTab,
    MainLayoutTitleBlock,
    BaseSwitcher,
    ExpertModeTab,
    TotalResults,
    CustomText,
    WarningModal,
  },
  props: {
    moduleName: {type: String, default: 'Online'},
    currentProject: {type: [Array, Object], required: true},
    additionalFilters: {type: Object, required: true},
    keywords: {type: Object, required: true},
    clippingContent: {type: Array, required: true},
    numberOfPosts: {type: Number, required: true},
  },
  data() {
    return {
      query: '',
      isExpertMode: false,
      isWarningModalDisplayed: false,
    }
  },
  computed: {
    ...mapGetters({
      department: get.DEPARTMENT,
      user: get.USER_INFO,
    }),
    isAdmin() {
      return this.user.user_profile.role === 'admin'
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
    isCurrentProjectCreated() {
      return !isAllFieldsEmpty(this.currentProject)
    },
    startDate() {
      return (
        this.currentProject.start_date || this.currentProject.start_search_date
      )
    },
  },
  mounted() {
    this.isExpertMode = this.currentProject.expert_mode
    this.showResults()
    this.filters = expertModeFilters[this.moduleName.toLowerCase()]
  },
  methods: {
    ...mapActions([action.OPEN_FLASH_MESSAGE]),
    showResults(pageNumber, numberOfPosts) {
      const project = {
        keywords: this.keywords?.keywords || this.currentKeywords,
        additions:
          this.keywords?.additional_keywords || this.currentAdditionalKeywords,
        exceptions:
          this.keywords?.ignore_keywords || this.currentExcludeKeywords,
        country:
          this.additionalFilters?.country || this.currentProject.country_filter,
        language:
          this.additionalFilters?.language ||
          this.currentProject.language_filter,
        sentiment: this.additionalFilters?.sentiment || [],
        date_range: [
          this.additionalFilters?.date_range[0] ||
            this.currentProject?.start_search_date,

          this.additionalFilters?.date_range[1] ||
            this.currentProject?.end_search_date,
        ],
        start_date:
          this.additionalFilters?.start_date || this.currentProject?.start_date,
        source:
          this.additionalFilters?.source || this.currentProject.source_filter,
        author:
          this.additionalFilters?.author || this.currentProject.author_filter,
        posts_per_page: numberOfPosts || 20,
        page_number: pageNumber || 1,
        sort_posts: [],
        country_dimensions: [],
        language_dimensions: [],
        source_dimensions: [],
        author_dimensions: [],
        sentiment_dimensions: [],
        query_filter: this.query || this.currentProject?.query_filter,
        department_id: this.department?.id,
        expert_mode: this.isExpertMode,
        project_pk: this.currentProject.id,
      }

      if (this.moduleName === 'Social') {
        this.$emit('show-results', project)
      }

      if (this.moduleName === 'Online') {
        this.$emit('show-results', {
          posts_per_page: numberOfPosts || 20,
          page_number: pageNumber || 1,
          project_pk: this.currentProject.id,
          sort_posts: [],
        })
      }
    },
    saveProject() {
      if (!this.isAdmin) {
        this.updateProjectData()
        return
      }

      const isKeywordsUpdated = this.checkKeywordUpdates(this.keywords)
      const isStartDateUpdated = this.checkStartDateUpdates(
        this.additionalFilters?.start_date
      )
      const isExpertQueryUpdated =
        this.query && this.query !== this.currentProject?.query_filter

      if (isKeywordsUpdated || isStartDateUpdated || isExpertQueryUpdated) {
        this.isWarningModalDisplayed = true
      } else {
        this.updateProjectData()
      }
    },
    updateProjectData(recollect = false) {
      const project = {
        title: this.currentProject?.title,
        note: this.currentProject?.note || '',
        keywords: this.keywords?.keywords || this.currentKeywords,
        additional_keywords:
          this.keywords?.additional_keywords || this.currentAdditionalKeywords,
        ignore_keywords:
          this.keywords?.ignore_keywords || this.currentExcludeKeywords,
        max_items: '',
        image: null,
        arabic_name: '',
        english_name: '',
        creator: this.currentProject?.creator,
        source: this.currentProject?.source,
        sources: this.additionalFilters.sources || this.currentProject.sources,
        workspace: this.currentProject?.workspace,
        start_date:
          this.additionalFilters?.start_date || this.currentProject?.start_date,
        start_search_date:
          this.additionalFilters?.date_range[0] ||
          this.currentProject?.start_search_date,
        end_search_date:
          this.additionalFilters?.date_range[1] ||
          this.currentProject?.end_search_date,
        source_filter: this.additionalFilters?.source || null,
        author_filter: this.additionalFilters?.author || null,
        language_filter: this.additionalFilters?.language || null,
        sentiment_filter: this.additionalFilters?.sentiment,
        country_filter: this.additionalFilters?.country || null,
        sort_posts: [],
        query_filter: this.query || this.currentProject?.query_filter,
        expert_mode: this.isExpertMode,
        project_pk: this.currentProject.id,
        recollect,
      }

      this.$emit('update-project', project)

      if (this.moduleName === 'Social') {
        this.showResults()
      }
      this.isWarningModalDisplayed = false

      this[action.OPEN_FLASH_MESSAGE]({
        type: 'Success',
        message: 'Project settings have been saved.',
      })
    },

    checkKeywordUpdates(newKeywords) {
      if (isAllFieldsEmpty(newKeywords)) return false

      const {keywords, additional_keywords, ignore_keywords} = newKeywords
      const isMainUpdated =
        keywords && !areArraysEqual(keywords, this.currentKeywords)
      const isAdditionalUpdated =
        additional_keywords &&
        !areArraysEqual(additional_keywords, this.currentAdditionalKeywords)
      const isExcludeUpdated =
        ignore_keywords &&
        !areArraysEqual(ignore_keywords, this.currentExcludeKeywords)
      return isMainUpdated || isAdditionalUpdated || isExcludeUpdated
    },
    checkStartDateUpdates(newStartDate) {
      if (!newStartDate) return false

      const format = 'YYYY-MM-DD'
      const currentStartDate = moment(this.currentProject?.start_date).format(
        format
      )
      return moment(newStartDate).format(format) !== currentStartDate
    },

    updateKeywordsCollection(name, value) {
      this.$emit('update-collection', name, value)
    },
    updateQueryFilter(value) {
      this.query = value
    },

    switchTrigger() {
      this.isExpertMode = !this.isExpertMode
    },
  },
}
</script>

<style lang="scss" scoped>
.search-settings-wrapper {
  display: flex;
  flex-direction: column;

  width: 100%;

  .search {
    display: flex;
    gap: 5px;
  }
}

.switcher {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;

  max-width: 408px;
  gap: 10px;
  padding: 14px 12px;

  border: var(--border-primary);
  border-radius: 8px;

  cursor: pointer;
  user-select: none;

  &__active {
    background-color: var(--primary-active-color);
    border: 1px solid var(--primary-color);
    border-radius: 8px;
  }
}

.search-section {
  position: absolute;
  top: 0;
  right: 0;

  width: 50%;
  padding: 80px 32px 0 16px;

  border: 1px solid var(--border-color);
  background-color: var(--background-secondary-color);
}

.expert-mode {
  width: 50%;
}
</style>

<style lang="scss">
.expert-mode {
  width: 50%;

  .buttons {
    padding: 0;
    margin: 0 -40px 0 -34px;
  }
}
</style>
