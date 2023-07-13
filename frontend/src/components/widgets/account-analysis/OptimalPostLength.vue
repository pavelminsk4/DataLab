<template>
  <OptimalPostLengthWidget
    tooltip-Labels="Engagements"
    :widget-details="widgetDetails"
    :widget-data="optimalPostLength"
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
  name: 'FollowerGrowth',
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
    optimalPostLength() {
      return this.accountAnalysisWidgets.optimalPostLength
    },
  },
  created() {
    if (!this.optimalPostLength.length) {
      this[action.GET_OPTIMAL_POST_LENGTH]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_POST_LENGTH]),
  },
}
</script>
