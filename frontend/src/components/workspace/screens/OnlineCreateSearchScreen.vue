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
import {createNamespacedHelpers, mapState, mapActions} from 'vuex'
import {action, action as actionOnline} from '@store/constants'

import CreateSearchScreen from '@components/workspace/screens/CreateSearchScreen'

const {mapActions: mapOnlineActions} = createNamespacedHelpers('online')

export default {
  name: 'OnlineCreateSearchScreen',
  components: {
    CreateSearchScreen,
  },
  props: {
    workspaceId: {type: String, default: null},
    moduleName: {type: String, default: ''},
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
    ...mapActions([action.OPEN_FLASH_MESSAGE]),
    ...mapOnlineActions([
      actionOnline.POST_SEARCH,
      actionOnline.CREATE_WORKSPACE,
      actionOnline.CREATE_PROJECT,
      actionOnline.GET_WORKSPACES,
    ]),
    showResults(data) {
      try {
        this[actionOnline.POST_SEARCH](data)
      } catch (e) {
        console.error(e)
      }
    },
    async createWorkspace(workspaceData) {
      const newWorkspace = await this[actionOnline.CREATE_WORKSPACE](
        workspaceData
      )

      await this.$router.push({
        name: 'OnlineAnalytics',
        params: {
          workspaceId: newWorkspace.id,
          projectId: newWorkspace.projects[0].id,
        },
      })
      await this[actionOnline.GET_WORKSPACES]()

      await this[action.OPEN_FLASH_MESSAGE]({
        type: 'Success',
        message:
          'The data is being collected. Your project will be ready in an hour.',
      })
    },
    async createProject(projectData) {
      const newProject = await this[actionOnline.CREATE_PROJECT](projectData)

      await this.$router.push({
        name: 'OnlineAnalytics',
        params: {
          workspaceId: this.workspaceId,
          projectId: newProject.id,
        },
      })
      await this[actionOnline.GET_WORKSPACES]()

      await this[action.OPEN_FLASH_MESSAGE]({
        type: 'Success',
        message:
          'The data is being collected. Your project will be ready in an hour.',
      })
    },
  },
}
</script>
