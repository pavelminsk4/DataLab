<template>
  <SimpleModeTab
    :module-name="moduleName"
    @show-result="showResults"
    @update-collection="updateCollection"
    @save-project="saveChanges"
  >
    <template #module-type>
      <div class="module-wrapper">
        <div>Module</div>
        <BaseRadio
          v-for="(item, index) in modulesTypes"
          :key="item + index"
          v-model="selectedModuleType"
          :id="'module' + index"
          :value="item"
          class="radio-wrapper"
        >
          <div class="radio-content">
            <component :is="stringToPascalCase(item) + 'Icon'" class="icon" />
            {{ item }}
          </div>
        </BaseRadio>
      </div>
    </template>
  </SimpleModeTab>
</template>

<script>
import {createNamespacedHelpers, mapState, mapActions, mapGetters} from 'vuex'
import {action as actionTFS, action, get} from '@store/constants'
import {stringToPascalCase} from '@/lib/utilities'

import BaseRadio from '@/components/BaseRadio'
import SimpleModeTab from '@/components/workspace/SimpleModeTab'
import OnlineIcon from '@/components/icons/OnlineIcon'

const {mapActions: mapTFSActions, mapState: mapTFSState} =
  createNamespacedHelpers('twentyFourSeven')

export default {
  name: 'CreateSearchTFS',
  components: {
    BaseRadio,
    SimpleModeTab,
    OnlineIcon,
  },
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
  },
  data() {
    return {
      selectedModuleType: 'Online',
      modulesTypes: ['Online'],
    }
  },
  computed: {
    ...mapState({
      additionalFilters: (state) => state.additionalFilters,
      keywords: (state) => state.keywords,
      newWorkspace: (state) => state.newTFSWorkspace,
      newProject: (state) => state.newTFSProject,
    }),
    ...mapTFSState({
      newProjectId: (state) => state.newProjectId,
      newWorkspaceId: (state) => state.newWorkspaceId,
    }),
    ...mapGetters({department: get.DEPARTMENT}),
    defaultDateRange() {
      return [this.getLastWeeksDate(), new Date()]
    },
    searchFilters() {
      return this.newProject.searchFilters
    },
  },
  created() {
    if (this.defaultDateRange.length) {
      this[action.UPDATE_ADDITIONAL_FILTERS]({
        date_range: this.defaultDateRange,
      })
    }
  },
  methods: {
    stringToPascalCase,
    ...mapTFSActions([
      actionTFS.CREATE_TFS_WORKSPACE,
      actionTFS.CREATE_TFS_PROJECT,
      actionTFS.GET_WORKSPACES,
    ]),
    ...mapActions([
      action.POST_SEARCH,
      action.UPDATE_ADDITIONAL_FILTERS,
      action.UPDATE_KEYWORDS_LIST,
      action.UPDATE_NEW_TFS_PROJECT,
    ]),
    getLastWeeksDate() {
      const now = new Date()

      return new Date(now.getFullYear(), now.getMonth(), now.getDate() - 6)
    },
    updateCollection(name, val) {
      this[action.UPDATE_KEYWORDS_LIST]({
        [name]: val,
      })
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
          sort_posts: [],
          country_dimensions: [],
          language_dimensions: [],
          source_dimensions: [],
          author_dimensions: [],
          sentiment_dimensions: [],
          query_filter: [],
          department_id: this.department.id,
          expert_mode: false,
        })
      } catch (e) {
        console.error(e)
      }
    },
    async saveChanges() {
      await this[action.UPDATE_NEW_TFS_PROJECT]({
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
        project_type: this.selectedModuleType.toLowerCase(),
      })

      if (+this.workspaceId) {
        await this[action.CREATE_TFS_PROJECT]({
          ...this.newProject,
          workspace: +this.workspaceId,
        })
      } else {
        await this[action.CREATE_TFS_WORKSPACE]({
          ...this.newWorkspace,
          tfs_workspace_projects: [
            {
              ...this.newProject,
            },
          ],
        })
      }

      this.$router.push({
        name: 'TFSDashboard',
        params: {
          projectId: this.newProjectId,
          workspaceId: this.newWorkspaceId || this.workspaceId,
        },
      })
    },
  },
  watch: {
    'newProject.searchFilters.page_number'() {
      this.showResults(this.searchFilters.page_number)
    },
    'newProject.searchFilters.posts_per_page'() {
      this.showResults(
        this.searchFilters.page_number,
        this.searchFilters.posts_per_page
      )
    },
  },
}
</script>

<style lang="scss" scoped>
.module-wrapper {
  display: flex;
  flex-direction: column;
  gap: 12px;

  margin: 32px 0 40px 0;

  .radio-wrapper {
    margin: 0;
    .radio-content {
      display: flex;
      align-items: center;
      gap: 4px;

      .icon {
        width: 16px;
        height: 16px;
      }
    }
  }
}
</style>
