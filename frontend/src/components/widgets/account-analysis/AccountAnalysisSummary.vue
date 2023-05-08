<template>
  <AccountAnalysisSummaryWidget :widget-data="summary" />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import AccountAnalysisSummaryWidget from '@/components/widgets/AccountAnalysisSummaryWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  components: {
    AccountAnalysisSummaryWidget,
  },
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
