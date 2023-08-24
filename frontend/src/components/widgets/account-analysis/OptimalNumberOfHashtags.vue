<template>
  <OptimalPostLengthWidget
    :widget-details="widgetDetails"
    :widget-data="optimalNumberOfHashtags"
    :colors="colors"
    :tooltip-Labels="translatedText('Engagements')"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import translate from '@/lib/mixins/translate.js'

import OptimalPostLengthWidget from '@/components/widgets/OptimalPostLengthWidget'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'OptimalNumberOfHashtags',
  mixins: [translate],
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
      return (
        this.accountAnalysisWidgets.optimalNumberOfHashtags.engagement || []
      )
    },
  },
  created() {
    this.colors = ['#5A12B3']
    if (isAllFieldsEmpty(this.optimalNumberOfHashtags)) {
      this[action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_NUMBER_OF_HASHTAGS]),
    isAllFieldsEmpty,
  },
}
</script>
