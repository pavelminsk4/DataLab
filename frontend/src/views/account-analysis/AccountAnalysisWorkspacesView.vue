<template>
  <AccountAnalysisModuleScreen
    :workspaces="workspaces"
    :is-project-creation-available="isProjectCreationAvailable"
    @create-workspace="createWorkspace"
    @open-workspace="openWorkspace"
    @add-new-project="addNewProject"
  />
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {get} from '@store/constants'

import AccountAnalysisModuleScreen from '@components/account-analysis/screens/AccountAnalysisModuleScreen'

const {mapState: mapAccountAnalyticsState} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisWorkspacesView',
  components: {
    AccountAnalysisModuleScreen,
  },
  computed: {
    ...mapAccountAnalyticsState(['workspaces']),
    ...mapGetters({
      department: get.DEPARTMENT,
    }),
    isProjectCreationAvailable() {
      return (
        this.department?.current_number_of_account_analysis_projects >=
        this.department?.max_projects_account_analysis
      )
    },
  },
  methods: {
    createWorkspace() {
      this.$router.push({
        name: 'AccountAnalysisWorkspaceStep1',
        params: {workspaceId: 'new'},
      })
    },
    openWorkspace(workspaceId) {
      this.$router.push({
        name: 'AccountAnalysisWorkspace',
        params: {workspaceId},
      })
    },
    addNewProject(workspaceId) {
      this.$router.push({
        name: 'AccountAnalysisWorkspaceStep2',
        params: {workspaceId},
      })
    },
  },
}
</script>
