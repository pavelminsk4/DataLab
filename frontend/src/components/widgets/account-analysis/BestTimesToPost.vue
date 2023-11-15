<template>
  <BestTimesToPostWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="bestTimesToPost"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import BestTimesToPostWidget from '@components/widgets/BestTimesToPostWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'BestTimesToPost',
  components: {BestTimesToPostWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    bestTimesToPost() {
      return this.accountAnalysisWidgets.bestTimesToPost
    },
  },
  created() {
    if (!this.bestTimesToPost.length) {
      this[action.GET_BEST_TIMES_TO_POST]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_BEST_TIMES_TO_POST]),
  },
}
</script>
