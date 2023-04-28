<template>
  <AccountAnalysisModuleScreen @create-workspace="createWorkspace" />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import AccountAnalysisModuleScreen from '@/components/account-analysis/AccountAnalysisModuleScreen'

const {mapActions, mapGetters} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisModuleView',
  components: {
    AccountAnalysisModuleScreen,
  },
  computed: {
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
  },
  created() {
    if (!this.workspaces?.length) {
      this[action.GET_WORKSPACES]()
    }
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
