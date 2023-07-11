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
import {createNamespacedHelpers, mapState} from 'vuex'
import {action as actionSocial} from '@store/constants'

import CreateSearchScreen from '@/components/workspace/screens/CreateSearchScreen'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'SocialCreateSearchScreen',
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
    ...mapSocialActions([
      actionSocial.CREATE_WORKSPACE,
      actionSocial.CREATE_PROJECT,
      actionSocial.GET_WORKSPACES,
      actionSocial.POST_SEARCH,
    ]),
    showResults(data) {
      try {
        this[actionSocial.POST_SEARCH](data)
      } catch (e) {
        console.error(e)
      }
    },
    async createWorkspace(workspaceData) {
      const newWorkspace = await this[actionSocial.CREATE_WORKSPACE](
        workspaceData
      )

      await this.$router.push({
        name: 'SocialAnalytics',
        params: {
          workspaceId: newWorkspace.id,
          projectId: newWorkspace.projects[0].id,
        },
      })
      await this[actionSocial.GET_WORKSPACES]()
    },
    async createProject(projectData) {
      const newProject = await this[actionSocial.CREATE_PROJECT](projectData)

      await this.$router.push({
        name: 'SocialAnalytics',
        params: {
          workspaceId: this.workspaceId,
          projectId: newProject.id,
        },
      })
      await this[actionSocial.GET_WORKSPACES]()
    },
  },
}
</script>
