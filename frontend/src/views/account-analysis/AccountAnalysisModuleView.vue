<template>
  <router-view></router-view>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

const {mapActions} = createNamespacedHelpers('accountAnalysis')

export default {
  name: 'AccountAnalysisModuleView',
  created() {
    if (!this.workspaces?.length) {
      this[action.GET_WORKSPACES]()
    }

    console.log(this.department?.current_number_of_account_analysis_projects)
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
  },
}
</script>
