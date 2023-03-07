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
import {createNamespacedHelpers} from 'vuex'
import {action as actionSocial} from '@store/modules/social/constants'

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
        console.log(e)
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
