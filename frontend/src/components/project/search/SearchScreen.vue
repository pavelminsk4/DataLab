<template>
  <div v-if="currentProject">
    <MainLayoutTitleBlock
      :title="currentProject.title"
      :description="currentProject.note"
      :back-page="{
        name: 'workspace',
        routName: 'SocialWorkspace',
      }"
    >
      <div class="search-results-count">{{ numberOfPosts }} results</div>
    </MainLayoutTitleBlock>

    <div class="search-settings-wrapper">
      <SimpleModeTab
        :module-name="moduleName"
        :main-keywords="currentKeywords"
        :exclude-keywords="currentExcludeKeywords"
        :additional-keywords="currentAdditionalKeywords"
        :current-project="currentProject"
        :is-disabled-button="!currentKeywords.length"
        @save-project="updateProjectData"
        @show-result="showResults"
        @update-collection="$emit('update-collection', $event)"
      />
      <SearchResults
        :module-name="moduleName"
        :clipping-content="clippingContent"
        @update-page="showResults"
        @update-posts-count="showResults"
      />
    </div>
  </div>
</template>

<script>
import MainLayoutTitleBlock from '@/components/layout/MainLayoutTitleBlock'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import SearchResults from '@/components/SearchResults'

export default {
  name: 'SearchScreen',
  components: {SearchResults, SimpleModeTab, MainLayoutTitleBlock},
  props: {
    moduleName: {type: String, default: 'Online'},
    currentProject: {type: [Array, Object], required: true},
    additionalFilters: {type: Object, required: true},
    keywords: {type: Object, required: true},
    clippingContent: {type: Array, required: true},
    numberOfPosts: {type: Number, required: true},
  },
  computed: {
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
    this.showResults()
  },
  methods: {
    showResults(pageNumber, numberOfPosts) {
      this.$emit('show-results', {
        keywords: this.currentKeywords || this.keywords?.keywords,
        additions:
          this.currentAdditionalKeywords || this.keywords?.additional_keywords,
        exceptions:
          this.currentExcludeKeywords || this.keywords?.ignore_keywords,
        country: this.additionalFilters?.country || [],
        language: this.additionalFilters?.language || [],
        sentiment:
          this.additionalFilters?.sentiment ||
          this.currentProject?.sentiment_filter ||
          [],
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
      })
    },
    updateProjectData() {
      this.$emit('update-project', {
        title: this.currentProject?.title,
        note: this.currentProject?.note || '',
        keywords: this.currentKeywords || this.keywords?.keywords,
        additional_keywords:
          this.currentAdditionalKeywords || this.keywords?.additional_keywords,
        ignore_keywords:
          this.currentExcludeKeywords || this.keywords?.ignore_keywords,
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
        sentiment_filter:
          this.additionalFilters?.sentiment ||
          this.currentProject?.sentiment_filter ||
          null,
        country_filter: this.additionalFilters?.country || null,
        sort_posts: [],
      })

      this.showResults()
    },
  },
}
</script>

<style scoped>
.search-settings-wrapper {
  display: flex;

  width: 100%;
}
</style>
