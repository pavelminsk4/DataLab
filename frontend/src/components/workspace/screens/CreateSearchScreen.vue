<template>
  <NavigationBar
    v-if="this.currentStep === 'Step3'"
    :step="step"
    title="Define the search"
    hint="Search by keywords and phrases"
    :button-width="141"
    button-name="Save Project"
    @next-step="createWorkspaceAndProject"
  />

  <NavigationBar
    v-else
    :step="step"
    title="Define the search"
    hint="Search by keywords and phrases"
    :is-existing-workspace="true"
    :button-width="141"
    button-name="Create Project"
    @next-step="createProject"
  />

  <div class="search-settings-wrapper">
    <ProjectKeywords
      @show-result="showResults"
      @update-collection="updateCollection"
    />

    <SearchResults
      @update-page="showResults"
      @update-posts-count="showResults"
    />
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import NavigationBar from '@/components/navigation/NavigationBar'

import SearchResults from '@/components/SearchResults'
import ProjectKeywords from '@/components/workspace/ProjectKeywords'

export default {
  name: 'CreateSearchScreen',
  components: {
    ProjectKeywords,
    SearchResults,
    NavigationBar,
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
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      workspaces: get.WORKSPACES,
      currentStep: get.CURRENT_STEP,
      newProject: get.NEW_PROJECT,
      newWorkspace: get.NEW_WORKSPACE,
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
        })
      } catch (e) {
        console.log(e)
      }
    },

    async createWorkspaceAndProject() {
      try {
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
        this[action.UPDATE_NEW_WORKSPACE]({
          projects: [this.newProject],
        })
        this[action.CREATE_WORKSPACE](this.newWorkspace)
        this[action.CLEAR_STATE]()
        await this.$router.push({
          name: 'Home',
        })
        await this[action.GET_WORKSPACES]()
      } catch (e) {
        console.log(e)
      }
    },
    async createProject() {
      try {
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
        this[action.CREATE_PROJECT](this.newProject)
        this[action.CLEAR_STATE]()
        await this.$router.push({
          name: 'Workspace',
          params: {
            workspaceId: this.$route.params.workspaceId,
          },
        })
        await this[action.GET_WORKSPACES]()
      } catch (e) {
        console.log(e)
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
}

.radio-btn {
  display: flex;

  margin-right: 25px;

  color: var(--primary-text-color);

  cursor: pointer;
}

.not-check {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 20px;
  height: 20px;
  margin-right: 7px;

  border: 1px solid var(--secondary-text-color);
  border-radius: 50px;

  cursor: pointer;
}

.radio-wrapper {
  display: flex;
  justify-content: space-between;

  margin: 10px 0 25px;
}

.back-button {
  cursor: pointer;

  color: var(--secondary-text-color);
}

.arrow-back {
  margin-right: 6px;
}

.title {
  margin: 5px 0 2px;

  color: var(--primary-text-color);

  font-size: 36px;
}

.create-project-title {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.progress-bar-wrapper {
  display: flex;
  align-items: center;
  justify-content: center;
}

.progress-bar {
  display: flex;
  align-items: center;

  margin-right: 40px;
}

.progress-item {
  display: flex;
  align-items: center;
  justify-content: center;

  width: 24px;
  height: 24px;

  border-radius: 100%;
  border: 1px solid var(--primary-button-color);
  box-shadow: 0 0 3px var(--box-shadow-color);

  color: var(--primary-text-color);
  background-color: var(--primary-bg-color);
}

.progress-line {
  width: 34px;
  height: 2px;

  background-color: var(--progress-line);
}

.hint {
  color: var(--secondary-text-color);

  font-size: 14px;
}

@media screen and (max-width: 1000px) {
  .search-settings-wrapper {
    gap: 20px;
  }
}
</style>
