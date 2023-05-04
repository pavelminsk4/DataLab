<template>
  <AccountAnalysisSummaryWidget />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    summary() {
      return this.accountAnalysisWidgets.summary
    },
    labels() {
      return ''
    },
    chartValues() {
      if (!this.summary.length) return
      return ''
    },
  },
  created() {
    if (!this.summary.length) {
      this[action.GET_SUMMARY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY]),
  },
}
</script>
