<template>
  <ReportsScreen
    :reports="reports"
    :back-page="{name: 'main page', routeName: 'MainView'}"
    @create-report="createReports"
    @open-report="goToReport"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import ReportsScreen from '@components/reports/ReportsScreen'

export default {
  name: 'ReportsView',
  components: {ReportsScreen},
  computed: {
    ...mapGetters({
      reports: get.REGULAR_REPORTS,
    }),
  },
  async created() {
    if (!this.reports.length) {
      await this[action.GET_REGULAR_REPORTS]()
    }
  },
  methods: {
    ...mapActions([action.GET_REGULAR_REPORTS]),
    createReports() {
      this.$router.push({
        name: 'ReportStep1',
      })
    },
    goToReport(reportId) {
      return reportId
    },
  },
}
</script>
