<template>
  <MainLayoutTitleBlock
    title="Define the search"
    description="Search by keywords and phrases"
    :back-page="{
      name: 'main page',
      routName: 'Home',
    }"
  />

  <ProgressBar />

  <div class="search-settings-wrapper">
    <SimpleModeTab
      @show-result="showResults"
      @update-collection="updateCollection"
      @save-project="createWorkspaceAndProject"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@/components/workspace/ProgressBar'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'

export default {
  name: 'CreateSearchScreen',
  components: {
    MainLayoutTitleBlock,
    ProgressBar,
    SimpleModeTab,
  },
  props: {
    workspaceId: {
      type: Number,
      default: null,
    },
  },
  data() {
    return {
      searchLoading: false,
      buttonLoading: false,
    }
  },
  created() {
    if (this.defaultDateRange.length) {
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        date_range: this.defaultDateRange,
      })
    }
  },
  computed: {
    ...mapGetters({
      searchData: get.SEARCH_DATA,
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      workspaces: get.WORKSPACES,
      currentStep: get.CURRENT_STEP,
      newProject: get.NEW_PROJECT,
      newWorkspace: get.NEW_WORKSPACE,
      newProjectId: get.NEW_PROJECT_ID,
      newWorkspaceId: get.NEW_WORKSPACE_ID,
    }),
    step() {
      return this.$route.name
    },
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_ADDITIONAL_FILTERS,
      action.UPDATE_NEW_WORKSPACE,
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_KEYWORDS_LIST,
      action.CREATE_WORKSPACE,
      action.CREATE_PROJECT,
      action.GET_WORKSPACES,
      action.POST_SEARCH,
      action.CLEAR_STATE,
      action.CLEAR_SEARCH_LIST,
    ]),
    updateCollection(name, val) {
      this[action.UPDATE_KEYWORDS_LIST]({
        [name]: val,
      })
    },
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 7)
    },
    showResults(pageNumber, numberOfPosts) {
      try {
        this.searchLoading = true
        this[action.POST_SEARCH]({
          keywords: this.keywords?.keywords,
          additions: this.keywords?.additional_keywords,
          exceptions: this.keywords?.ignore_keywords,
          country: this.additionalFilters?.country || [],
          language: this.additionalFilters?.language || [],
          sentiment: this.additionalFilters?.sentiment || [],
          date_range: this.additionalFilters?.date_range,
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
      } catch (e) {
        console.log(e)
      } finally {
        this.searchLoading = false
      }
    },

    async createWorkspaceAndProject() {
      try {
        this.buttonLoading = true
        this[action.UPDATE_PROJECT_STATE]({
          keywords: this.keywords?.keywords,
          additional_keywords: this.keywords?.additional_keywords,
          ignore_keywords: this.keywords?.ignore_keywords,
          start_search_date: this.additionalFilters?.date_range[0],
          end_search_date: this.additionalFilters?.date_range[1],
          source_filter: this.additionalFilters?.source || null,
          author_filter: this.additionalFilters?.author || null,
          language_filter: this.additionalFilters?.language || null,
          sentiment_filter: this.additionalFilters?.sentiment || null,
          country_filter: this.additionalFilters?.country || null,
        })

        if (this.workspaceId) {
          await this[action.CREATE_PROJECT](this.newProject)
        } else {
          this[action.UPDATE_NEW_WORKSPACE]({
            projects: [this.newProject],
          })
          await this[action.CREATE_WORKSPACE](this.newWorkspace)
        }

        await this[action.CLEAR_STATE]()
        this.buttonLoading = false
        await this.$router.push({
          name: 'Analytics',
          params: {
            workspaceId: this.workspaceId || this.newWorkspaceId,
            projectId: this.newProjectId,
          },
        })
        await this[action.GET_WORKSPACES]()
      } catch (e) {
        console.log(e)
      }
    },
  },
  watch: {
    keywords() {
      if (!this.keywords.length) {
        this[action.CLEAR_SEARCH_LIST]()
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.search-settings-wrapper {
  display: flex;
  justify-content: space-between;
  gap: 108px;

  max-width: 500px;
}

@media screen and (max-width: 1000px) {
  .search-settings-wrapper {
    gap: 20px;
  }
}
</style>
