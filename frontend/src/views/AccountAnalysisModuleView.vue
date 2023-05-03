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
  },
  methods: {
    ...mapActions([action.GET_WORKSPACES]),
  },
}
</script>
