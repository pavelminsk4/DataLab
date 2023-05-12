<template>
  <OptimalPostLengthWidget
    :widget-details="widgetDetails"
    :widget-data="optimalNumberOfHashtags"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import OptimalPostLengthWidget from '@/components/widgets/OptimalPostLengthWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'OptimalNumberOfHashtags',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {
    OptimalPostLengthWidget,
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    optimalNumberOfHashtags() {
      return this.accountAnalysisWidgets.optimalNumberOfHashtags
    },
  },
  created() {
    if (!this.optimalNumberOfHashtags.length) {
      this[action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]),
  },
}
</script>
