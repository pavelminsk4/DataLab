<template>
  <AccountAnalysisFeaturesView
    v-if="currentProject"
    :current-project="currentProject"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import AccountAnalysisFeaturesView from '@/views/account-analysis/AccountAnalysisFeaturesView'

const {mapState, mapActions} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisView',
  components: {AccountAnalysisFeaturesView},
  computed: {
    ...mapState(['workspaces']),
    workspaceId() {
      return this.$route.params.workspaceId
    },
    projectId() {
      return this.$route.params.projectId
    },
    currentWorkspace() {
      return this.workspaces.filter((el) => el.id === +this.workspaceId)
    },
    currentProject() {
      return this.currentWorkspace[0]?.projects.find(
        (el) => el.id === +this.projectId
      )
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
