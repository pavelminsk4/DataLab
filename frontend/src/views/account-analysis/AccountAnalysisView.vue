<template>
  <AccountAnalysisFeaturesView
    v-if="workspaces.length"
    :current-project="currentProject"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import AccountAnalysisFeaturesView from '@views/account-analysis/AccountAnalysisFeaturesView'

const {mapState, mapActions} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisView',
  components: {AccountAnalysisFeaturesView},
  computed: {
    ...mapState(['workspaces', 'loading']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      const existingWorkspace = this.workspaces.find(
        (el) => el.id === +this.workspaceId
      )
      if (!existingWorkspace && !this.loading) return this.goToNotFoundPage()

      return existingWorkspace
    },
    currentProject() {
      const existingProject = this.currentWorkspace?.projects.find(
        (el) => el.id === +this.projectId
      )
      if (!existingProject && !this.loading) return this.goToNotFoundPage()

      return existingProject
    },
  },
  async created() {
    if (!this.workspaces?.length) {
      await this[action.GET_WORKSPACES]()
    }
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
  },
}
</script>
