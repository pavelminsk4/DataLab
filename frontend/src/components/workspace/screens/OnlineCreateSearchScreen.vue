<template>
  <CreateSearchScreen
    :workspaceId="workspaceId"
    :moduleName="moduleName"
    @show-results="preview"
    @create-workspace="createWorkspace"
    @create-project="createProject"
  />
</template>

<script>
import {createNamespacedHelpers, mapActions} from 'vuex'
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
  methods: {
    ...mapActions([action.OPEN_FLASH_MESSAGE]),
    ...mapOnlineActions([
      actionOnline.POST_SEARCH,
      actionOnline.CREATE_WORKSPACE,
      actionOnline.CREATE_PROJECT,
      actionOnline.GET_WORKSPACES,
      actionOnline.POSTS_PREVIEW,
    ]),
    preview(filters) {
      try {
        this[actionOnline.POSTS_PREVIEW](filters)
      } catch (e) {
        console.error(e)
      }
    },
    async createWorkspace(workspaceData) {
      const newWorkspace = await this[actionOnline.CREATE_WORKSPACE](
        workspaceData
      )

      await this[actionOnline.GET_WORKSPACES]()

      await this.$router.push({
        name: 'OnlineWorkspace',
        params: {
          workspaceId: newWorkspace.id,
        },
      })

      await this[action.OPEN_FLASH_MESSAGE]({
        type: 'Success',
        message:
          'The data is being collected. Your project will be ready in an hour.',
      })
    },
    async createProject(projectData) {
      await this[actionOnline.CREATE_PROJECT](projectData)

      await this.$router.push({
        name: 'OnlineWorkspace',
        params: {
          workspaceId: this.workspaceId,
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
