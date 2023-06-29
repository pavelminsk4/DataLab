<template>
  <MainLayoutTitleBlock
    title="Define the search"
    description="Search by keywords and phrases"
    :back-page="{
      name: 'main page',
      routeName: `${moduleName}Home`,
    }"
  />

  <ProgressBar />

  <div
    :class="['switcher', isExpertMode && 'switcher__active']"
    @click="switchTrigger"
  >
    <span>Expert mode</span>
    <BaseSwitcher label="Expert mode" :value="isExpertMode" />
  </div>

  <ExpertModeTab
    v-if="isExpertMode"
    :filters="filters"
    @save-project="createWorkspaceAndProject"
    @show-result="showResults"
    @update-query-filter="updateQueryFilter"
  />

  <div v-else class="search-settings-wrapper">
    <SimpleModeTab
      :module-name="moduleName"
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
import ProgressBar from '@/components/workspace/WorkspaceProgressBar'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import BaseSwitcher from '@/components/BaseSwitcher'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import {expertModeFilters} from '@/lib/constants'

export default {
  name: 'CreateSearchScreen',
  components: {
    MainLayoutTitleBlock,
    ProgressBar,
    SimpleModeTab,
    BaseSwitcher,
    ExpertModeTab,
  },
  emits: ['create-project', 'create-workspace', 'show-results'],
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
  },
  data() {
    return {
      searchLoading: false,
      buttonLoading: false,
      isExpertMode: false,
      expertModeQuery: '',
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
      department: get.DEPARTMENT,
    }),
    step() {
      return this.$route.name
    },
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
  },
  created() {
    if (this.defaultDateRange.length) {
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        date_range: this.defaultDateRange,
      })
    }
    this.filters = expertModeFilters[this.moduleName.toLowerCase()]
  },
  watch: {
    keywords() {
      if (!this.keywords.length) {
        this[action.CLEAR_SEARCH_LIST]()
      }
    },
  },
  methods: {
    ...mapActions([
      action.UPDATE_ADDITIONAL_FILTERS,
      action.UPDATE_NEW_WORKSPACE,
      action.UPDATE_PROJECT_STATE,
      action.UPDATE_KEYWORDS_LIST,
      action.GET_WORKSPACES,
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

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
    showResults(pageNumber, numberOfPosts) {
      try {
        this.searchLoading = true

        const project = {
          keywords: this.keywords?.keywords,
          additions: this.keywords?.additional_keywords,
          exceptions: this.keywords?.ignore_keywords || [],
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
          department_id: this.department.id,
          query_filter: this.expertModeQuery,
          expert_mode: this.isExpertMode,
        }

        this[action.UPDATE_PROJECT_STATE]({searchFilters: project})

        this.$emit('show-results', project)
      } catch (e) {
        console.error(e)
      } finally {
        this.searchLoading = false
      }
    },

    async createWorkspaceAndProject() {
      try {
        this.buttonLoading = true

        const project = {
          department_id: this.department.id,
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
          query_filter: this.expertModeQuery,
          expert_mode: this.isExpertMode,
        }

        this[action.UPDATE_PROJECT_STATE](project)

        if (+this.workspaceId) {
          await this.$emit('create-project', this.newProject)
        } else {
          this[action.UPDATE_NEW_WORKSPACE]({
            projects: [this.newProject],
          })
          await this.$emit('create-workspace', this.newWorkspace)
        }

        await this[action.CLEAR_STATE]()
        this.buttonLoading = false
      } catch (e) {
        console.error(e)
      }
    },

    updateQueryFilter(value) {
      this.expertModeQuery = value
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
  justify-content: space-between;
  gap: 108px;

  max-width: 500px;
}

@media screen and (max-width: 1000px) {
  .search-settings-wrapper {
    gap: 20px;
  }
}
.switcher {
  display: flex;
  flex-wrap: nowrap;

  max-width: 45%;

  margin-top: 20px;
  gap: 10px;
  padding: 14px 12px;

  border: 1px solid #dee0e3;
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
