<template>
  <ReportsScreen
    :reports="workspace"
    :back-page="{name: 'main page', routName: 'MainView'}"
    @create-report="createReports"
    @open-report="goToReport"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ReportsScreen from '@/components/reports/ReportsScreen'

export default {
  name: 'ReportsView',
  components: {ReportsScreen},
  computed: {
    //change
    ...mapGetters({
      workspaces: get.WORKSPACES,
    }),
  },
  async created() {
    //change
    if (!this.workspaces.length) {
      await this[action.GET_WORKSPACES]()
    }

    this[action.CLEAR_STATE]()
  },
  methods: {
    //change
    ...mapActions([action.GET_WORKSPACES, action.CLEAR_STATE]),
    createReports() {
      this.$router.push({
        name: 'ReportStep1',
      })
    },
    goToReport(reportId) {
      return reportId
      // this.$router.push({
      //   name: 'OnlineAnalytics',
      //   params: {
      //     workspaceId: this.workspaceId,
      //     reportId,
      //   },
      // })
    },
  },
}
</script>
