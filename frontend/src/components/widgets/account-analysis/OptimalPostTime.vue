<template>
  <TimeMapWidget
    :widget-details="widgetDetails"
    :widget-data="optimalPostTime"
    :tooltip-Labels="translatedText('Engagements')"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import translate from '@lib/mixins/translate.js'

import TimeMapWidget from '@components/widgets/TimeMapWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'OptimalPostTime',
  mixins: [translate],
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {TimeMapWidget},
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    optimalPostTime() {
      return this.accountAnalysisWidgets.optimalPostTime
    },
  },
  created() {
    if (isAllFieldsEmpty(this.optimalPostTime)) {
      this[action.GET_OPTIMAL_POST_TIME]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_OPTIMAL_POST_TIME]),
    isAllFieldsEmpty,
  },
}
</script>
