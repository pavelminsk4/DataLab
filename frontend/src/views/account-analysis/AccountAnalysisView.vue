<template>
  <AccountAnalysisFeaturesView :current-project="currentProject" />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'

import AccountAnalysisFeaturesView from '@/views/account-analysis/AccountAnalysisFeaturesView'

const {mapState} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisView',
  components: {AccountAnalysisFeaturesView},
  computed: {
    ...mapState(['workspaces', 'currentProjectId']),
  },
  created() {
    this.currentProject = null
    this.workspaces.forEach((workspace) => {
      const result = workspace.projects.find((project) => {
        if (project.id === this.currentProjectId) return project
      })
      if (result) this.currentProject = result
    })
  },
}
</script>
