<template>
  <OptimalPostLengthWidget
    v-if="!isAllFieldsEmpty(averageEngagementsByDay)"
    :widget-details="widgetDetails"
    :widget-data="averageEngagementsByDay"
    :colors="colors"
    tooltip-Labels="Engagements"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import OptimalPostLengthWidget from '@/components/widgets/OptimalPostLengthWidget'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'AverageEngagemntsByDay',
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
    averageEngagementsByDay() {
      return this.accountAnalysisWidgets.averageEngagementsByDay
    },
  },
  created() {
    this.colors = ['#FF0099']
    if (isAllFieldsEmpty(this.averageEngagementsByDay)) {
      this[action.GET_AVERAGE_ENGAGEMENTS_BY_DAY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AVERAGE_ENGAGEMENTS_BY_DAY]),
    isAllFieldsEmpty,
  },
}
</script>
