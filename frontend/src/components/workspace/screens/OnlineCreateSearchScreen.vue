<template>
  <CreateSearchScreen
    :workspaceId="workspaceId"
    :moduleName="moduleName"
    @show-results="showResults"
    @create-workspace="createWorkspace"
    @create-project="createProject"
  />
</template>

<script>
import {mapState, mapActions} from 'vuex'
import {action} from '@store/constants'

import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'

export default {
  name: 'OnlineCreateSearchScreen',
  components: {
    CreateSearchScreen,
  },
  props: {
    workspaceId: {
      type: String,
      default: null,
    },
    moduleName: {
      type: String,
      default: '',
    },
  },
  computed: {
    ...mapState(['newProject']),
    searchFilters() {
      return this.newProject.searchFilters
    },
  },
  watch: {
    'newProject.searchFilters.page_number'() {
      this.showResults(this.searchFilters)
    },
    'newProject.searchFilters.posts_per_page'() {
      this.showResults(this.searchFilters)
    },
  },
  methods: {
    ...mapActions([
      action.POST_SEARCH,
      action.CREATE_WORKSPACE,
      action.CREATE_PROJECT,
      action.GET_WORKSPACES,
    ]),
    showResults(data) {
      try {
        this[action.POST_SEARCH](data)
      } catch (e) {
        console.error(e)
      }
    },
    async createWorkspace(workspaceData) {
      const newWorkspace = await this[action.CREATE_WORKSPACE](workspaceData)

      await this.$router.push({
        name: 'OnlineAnalytics',
        params: {
          workspaceId: newWorkspace.id,
          projectId: newWorkspace.projects[0].id,
        },
      })
      await this[action.GET_WORKSPACES]()
    },
    async createProject(projectData) {
      const newProject = await this[action.CREATE_PROJECT](projectData)

      await this.$router.push({
        name: 'OnlineAnalytics',
        params: {
          workspaceId: this.workspaceId,
          projectId: newProject.id,
        },
      })
      await this[action.GET_WORKSPACES]()
    },
  },
}
</script>
