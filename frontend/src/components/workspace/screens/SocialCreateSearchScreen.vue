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
import {action, action as actionSocial} from '@store/constants'

import CreateSearchScreen from '@components/workspace/screens/CreateSearchScreen'

const {mapActions: mapSocialActions} = createNamespacedHelpers('social')

export default {
  name: 'SocialCreateSearchScreen',
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

      await this[actionSocial.GET_WORKSPACES]()

      await this.$router.push({
        name: 'SocialWorkspace',
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
      await this[actionSocial.CREATE_PROJECT](projectData)

      await this.$router.push({
        name: 'SocialWorkspace',
        params: {
          workspaceId: this.workspaceId,
        },
      })
      await this[actionSocial.GET_WORKSPACES]()

      await this[action.OPEN_FLASH_MESSAGE]({
        type: 'Success',
        message:
          'The data is being collected. Your project will be ready in an hour.',
      })
    },
  },
}
</script>
