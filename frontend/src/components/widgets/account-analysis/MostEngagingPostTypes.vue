<template>
  <MostEngagingTypesWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
    tooltip-Labels="Engagements"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import MostEngagingTypesWidget from '@/components/widgets/MostEngagingTypesWidget'
import {isAllFieldsEmpty} from '@/lib/utilities'

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
      return Object.keys(this.mostEngagingPostTypes).map(
        (type) => type.split('_')[0]
      )
    },
    chartValues() {
      return [
        {
          color: ['#551EB9', '#01A4EE', '#FFBB01'],
          data: Object.values(this.mostEngagingPostTypes),
        },
      ]
    },
  },
  created() {
    if (isAllFieldsEmpty(this.mostEngagingPostTypes)) {
      this[action.GET_MOST_ENGAGING_POST_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_ENGAGING_POST_TYPES]),
    isAllFieldsEmpty,
  },
}
</script>
