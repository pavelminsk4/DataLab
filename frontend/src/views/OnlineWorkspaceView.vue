<template>
  <WorkspaceView
    v-if="workspace?.title"
    :title="workspace.title"
    :workspace="workspace"
    :table-header="tableHeader"
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
      loading: get.LOADING,
      workspaces: get.WORKSPACES,
    }),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    workspace() {
      const existingWorkspace = this.workspaces.find(
        (el) => el.id === +this.workspaceId
      )
      if (!existingWorkspace && !this.loading) return this.goToNotFoundPage()

      return existingWorkspace
    },
  },
  created() {
    this.tableHeader = [
      {name: 'project name', width: ''},
      {name: 'status', width: ''},
      {name: 'keywords', width: '20%'},
      {name: 'creator', width: '16%'},
      {name: 'assigned user', width: '11%'},
      {name: 'date', width: '11%'},
    ]
  },
  methods: {
    ...mapActions([action.DELETE_PROJECT]),
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
