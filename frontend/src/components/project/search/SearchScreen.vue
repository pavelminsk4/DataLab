<template>
  <div v-if="currentProject">
    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routeName: `${moduleName}Workspace`,
      }"
    >
      <div class="search-results-count">{{ numberOfPosts }} results</div>
    </MainLayoutTitleBlock>

    <div class="search-settings-wrapper">
      <div
        :class="['switcher', isExpertMode && 'switcher__active']"
        @click="switchTrigger"
      >
        <span>Expert mode</span>
        <BaseSwitcher label="Expert mode" :value="isExpertMode" />
      </div>
      <div class="search">
        <ExpertModeTab
          v-if="isExpertMode"
          :default-query="currentProject.query_filter"
          :filters="filters"
          @save-project="updateProjectData"
          @show-result="showResults"
          @update-query-filter="updateQueryFilter"
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
          @update-query-filter="updateQueryFilter"
          @save-project="updateProjectData"
          @show-result="showResults"
          @update-collection="updateKeywordsCollection"
        />
        <SearchResults
          :module-name="moduleName"
          :clipping-content="clippingContent"
          @show-results="showResults"
        />
      </div>
    </div>
  </div>
</template>

<script>
import {mapGetters} from 'vuex'
import {get} from '@store/constants'

import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import SearchResults from '@/components/SearchResults'
import BaseSwitcher from '@/components/BaseSwitcher'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import {expertModeFilters} from '@/lib/constants'

export default {
  name: 'SearchScreen',
  components: {
    SearchResults,
    SimpleModeTab,
    MainLayoutTitleBlock,
    BaseSwitcher,
    ExpertModeTab,
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
    }
  },
  computed: {
    ...mapGetters({
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
  },
  mounted() {
    this.isExpertMode = this.currentProject.expert_mode
    this.showResults()
    this.filters = expertModeFilters[this.moduleName.toLowerCase()]
  },
  methods: {
    showResults(pageNumber, numberOfPosts) {
      const project = {
        keywords: this.keywords?.keywords || this.currentKeywords,
        additions:
          this.keywords?.additional_keywords || this.currentAdditionalKeywords,
        exceptions:
          this.keywords?.ignore_keywords || this.currentExcludeKeywords,
        country: this.additionalFilters?.country || [],
        language: this.additionalFilters?.language || [],
        sentiment: this.additionalFilters?.sentiment || [],
        date_range: [
          this.additionalFilters?.date_range[0] ||
            this.currentProject?.start_search_date,

          this.additionalFilters?.date_range[1] ||
            this.currentProject?.end_search_date,
        ],
        source: this.additionalFilters?.source || [],
        author: this.additionalFilters?.author || [],
        posts_per_page: numberOfPosts || 20,
        page_number: pageNumber || 1,
        sort_posts: [],
        country_dimensions: [],
        language_dimensions: [],
        source_dimensions: [],
        author_dimensions: [],
        sentiment_dimensions: [],
        query_filter: this.query || this.currentProject?.query_filter,
        department_id: this.department.id,
        expert_mode: this.isExpertMode,
      }

      this.$emit('show-results', project)
    },
    updateProjectData() {
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
        workspace: this.currentProject?.workspace,
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
        department_id: this.department.id,
        expert_mode: this.isExpertMode,
      }

      this.$emit('update-project', project)

      this.showResults()
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

  max-width: 45%;
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
</style>
