<template>
  <OptimalPostLengthWidget
    v-if="!isAllEmptyFields(optimalNumberOfHashtags)"
    :widget-details="widgetDetails"
    :widget-data="optimalNumberOfHashtags"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import OptimalPostLengthWidget from '@/components/widgets/OptimalPostLengthWidget'
import {isAllEmptyFields} from '@lib/utilities'

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
      return this.accountAnalysisWidgets.optimalNumberOfHashtags.engagement
    },
  },
  created() {
    if (isAllEmptyFields(this.optimalNumberOfHashtags)) {
      this[action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]),
    isAllEmptyFields,
  },
}
</script>
