<template>
  <AccountAnalysisModuleScreen
    :workspaces="workspaces"
    :is-project-creation-available="isProjectCreationAvailable"
    @create-workspace="createWorkspace"
  />
</template>

<script>
import {createNamespacedHelpers, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import AccountAnalysisModuleScreen from '@/components/account-analysis/AccountAnalysisModuleScreen'

const {mapActions, mapState: mapAccountAnalytics} =
  createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisModuleView',
  components: {
    AccountAnalysisModuleScreen,
  },
  computed: {
    ...mapAccountAnalytics(['workspaces']),
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
  created() {
    if (!this.workspaces?.length) {
      this[action.GET_WORKSPACES]()
    }

    console.log(this.department?.current_number_of_account_analysis_projects)
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
    createWorkspace() {
      this.$router.push({
        name: 'AccountAnalysisWorkspaceStep1',
        params: {workspaceId: 'new'},
      })
    },
  },
}
</script>
