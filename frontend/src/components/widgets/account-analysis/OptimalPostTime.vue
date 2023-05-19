<template>
  <OptimalPostTimeWidget
    v-if="!isAllEmptyFields(optimalPostTime)"
    :widget-details="widgetDetails"
    :widget-data="optimalPostTime"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllEmptyFields} from '@lib/utilities'

import OptimalPostTimeWidget from '@/components/widgets/OptimalPostTimeWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'OptimalPostTime',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {OptimalPostTimeWidget},
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    optimalPostTime() {
      return this.accountAnalysisWidgets.optimalPostTime
    },
  },
  created() {
    if (isAllEmptyFields(this.optimalPostTime)) {
      this[action.GET_OPTIMAL_POST_TIME]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_POST_TIME]),
    isAllEmptyFields,
  },
}
</script>
