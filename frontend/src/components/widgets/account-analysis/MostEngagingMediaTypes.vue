<template>
  <MostEngagingTypesWidget
    v-if="Object.values(mostEngagingMediaTypes)"
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
  name: 'MostEngagingMediaTypesWidget',
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
    mostEngagingMediaTypes() {
      return this.accountAnalysisWidgets.mostEngagingMediaTypes
    },
    labels() {
      return Object.keys(this.mostEngagingMediaTypes).map(
        (type) => type.split('_')[0]
      )
    },
    chartValues() {
      return [
        {
          color: ['#551EB9', '#01A4EE', '#FFBB01'],
          data: Object.values(this.mostEngagingMediaTypes),
        },
      ]
    },
  },
  created() {
    if (!Object.values(this.mostEngagingMediaTypes).length) {
      this[action.GET_MOST_ENGAGING_MEDIA_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_ENGAGING_MEDIA_TYPES]),
  },
}
</script>
