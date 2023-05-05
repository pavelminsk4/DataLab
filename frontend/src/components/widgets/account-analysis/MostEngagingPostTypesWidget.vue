<template>
  <MostEngagingTypesWidget
    v-if="mostEngagingPostTypes.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import MostEngagingTypesWidget from '@/components/widgets/MostEngagingTypesWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MostEngagingPostTypesWidget',
  components: {
    MostEngagingTypesWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mostEngagingPostTypes() {
      return this.accountAnalysisWidgets.mostEngagingPostTypes
    },
    labels() {
      return ['Replies', 'Retweets', 'Tweets']
    },
    chartValues() {
      return [
        {color: '#551EB9', data: this.mostEngagingPostTypes.count_replies},
        {color: '#01A4EE', data: this.mostEngagingPostTypes.count_retweets},
        {color: '#FFBB01', data: this.mostEngagingPostTypes.count_tweets},
      ]
    },
  },
  created() {
    if (!this.mostEngagingPostTypes.length) {
      this[action.GET_MOST_ENGAGING_POST_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_ENGAGING_POST_TYPES]),
  },
}
</script>
