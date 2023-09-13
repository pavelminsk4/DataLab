<template>
  <WorkspaceView
    v-if="workspace?.title"
    :title="workspace.title"
    :workspace="workspace"
    :back-page="{
      name: 'main page',
      routeName: 'OnlineHome',
    }"
    @create-project="createProject"
    @open-project="goToProjectSettings"
    @delete-project="deleteProject"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import WorkspaceView from '@/components/workspace/WorkspaceView'

const {mapActions, mapGetters} = createNamespacedHelpers('online')

export default {
  name: 'OnlineWorkspaceView',
  components: {WorkspaceView},
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      return this.workspaces.find((el) => el.id === +this.workspaceId)
    },
  },
  async created() {
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES, action.DELETE_PROJECT]),
    createProject() {
      this.$router.push({
        name: 'OnlineWorkspaceStep2',
        params: {workspaceId: this.workspaceId},
      })
    },
    deleteProject(id) {
      this[action.DELETE_PROJECT](id)
    },
    goToProjectSettings(projectId) {
      this.$router.push({
        name: 'OnlineAnalytics',
        params: {
          workspaceId: this.workspaceId,
          projectId,
        },
      })
    },
  },
}
</script>
