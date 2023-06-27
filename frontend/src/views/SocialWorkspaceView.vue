<template>
  <WorkspaceView
    module-name="Social"
    :workspace="workspace"
    :back-page="{
      name: 'main page',
      routeName: 'SocialHome',
    }"
    @create-project="createProject"
    @open-project="goToProjectSettings"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import WorkspaceView from '@/components/workspace/WorkspaceView'

const {mapActions, mapGetters} = createNamespacedHelpers('social')

export default {
  name: 'SocialWorkspaceView',
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
    ...mapActions([action.GET_WORKSPACES]),
    createProject() {
      this.$router.push({
        name: 'SocialWorkspaceStep2',
        params: {workspaceId: this.workspaceId},
      })
    },
    goToProjectSettings(projectId) {
      this.$router.push({
        name: 'SocialDashboard',
        params: {
          workspaceId: this.workspaceId,
          projectId,
        },
      })
    },
  },
}
</script>
