<template>
  <WarningModal
    v-if="isWarningModalDisplayed"
    @close="toggleWarningModal"
    @approve="createWorkspaceAndProject"
  />

  <MainLayoutTitleBlock
    title="Define the search"
    description="Define the search (specify keywords and additional criteria that will be used for collecting your project data set)."
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
    <CustomText tag="span" text="Expert mode" />
    <BaseSwitcher label="Expert mode" :value="isExpertMode" />
  </div>

  <ExpertModeTab
    v-if="isExpertMode"
    :filters="filters"
    :module-name="moduleName"
    class="mode-section exprt-mode-section"
    @save-project="toggleWarningModal"
    @show-result="showResults"
    @update-query-filter="updateQueryFilter"
  />

  <SimpleModeTab
    v-else
    :module-name="moduleName"
    class="mode-section"
    @show-result="showResults"
    @update-collection="updateCollection"
    @save-project="toggleWarningModal"
  >
    <div v-if="isAdmin" class="souces-wrapper">
      Main sourses
      <div class="sources">
        <BaseCheckbox
          v-for="(source, index) in mainSources"
          :key="source + index"
          v-model="selectedSources"
          :value="source"
          class="checkbox"
        >
          <CustomText :text="source" />
        </BaseCheckbox>
      </div>
    </div>
  </SimpleModeTab>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {expertModeFilters} from '@/lib/constants'

import MainLayoutTitleBlock from '@components/layout/MainLayoutTitleBlock'
import ProgressBar from '@/components/workspace/WorkspaceProgressBar'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import BaseSwitcher from '@/components/BaseSwitcher'
import ExpertModeTab from '@/components/workspace/ExpertModeTab'
import CustomText from '@/components/CustomText'
import WarningModal from '@/components/modals/WarningModal'
import BaseCheckbox from '@/components/BaseCheckbox2'

export default {
  name: 'CreateSearchScreen',
  components: {
    MainLayoutTitleBlock,
    ProgressBar,
    SimpleModeTab,
    BaseSwitcher,
    ExpertModeTab,
    CustomText,
    WarningModal,
    BaseCheckbox,
  },
  emits: ['create-project', 'create-workspace', 'show-results'],
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
  },
  data() {
    return {
      isWarningModalDisplayed: false,
      searchLoading: false,
      buttonLoading: false,
      isExpertMode: false,
      expertModeQuery: '',
      mainSources: ['RSS', 'Talkwalker'],
      selectedSources: [],
    }
  },
  computed: {
    ...mapGetters({
      additionalFilters: get.ADDITIONAL_FILTERS,
      keywords: get.KEYWORDS,
      newProject: get.NEW_PROJECT,
      newWorkspace: get.NEW_WORKSPACE,
      department: get.DEPARTMENT,
      userInfo: get.USER_INFO,
    }),
    step() {
      return this.$route.name
    },
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
    isAdmin() {
      return this.userInfo.user_profile.role === 'admin'
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

    toggleWarningModal() {
      this.isWarningModalDisplayed = !this.isWarningModalDisplayed
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
          selected_sources: this.selectedSources,
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

.souces-wrapper {
  margin-top: 20px;
}

.sources {
  display: flex;

  gap: 15px;
  margin-top: 10px;
}

.checkbox {
  display: flex;
  align-items: center;

  padding: 12px;
  gap: 10px;

  border: 1px solid var(--border-color);
  border-radius: 10px;

  font-style: normal;
  font-weight: 400;
  font-size: 14px;
  line-height: 20px;
}

@media screen and (max-width: 1000px) {
  .search-settings-wrapper {
    gap: 20px;
  }
}
.switcher {
  display: flex;
  flex-wrap: nowrap;
  justify-content: space-between;

  max-width: 408px;

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

.mode-section {
  width: 100%;
}
</style>

<style lang="scss">
.mode-section {
  .buttons {
    width: auto;
    margin-right: -64px;
  }
}

.exprt-mode-section {
  .buttons {
    margin: 0 -104px 0 -36px;
  }
}
</style>
