<template>
  <OptimalPostLengthWidget
    :widget-details="widgetDetails"
    :widget-data="averageEngagementsByDayForMentions"
    :colors="colors"
    :tooltip-Labels="translatedText('Engagements')"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import translate from '@/lib/mixins/translate.js'
import OptimalPostLengthWidget from '@/components/widgets/OptimalPostLengthWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'AverageEngagementsByDayForMentions',
  mixins: [translate],
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {OptimalPostLengthWidget},
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),

    averageEngagementsByDayForMentions() {
      return this.accountAnalysisWidgets.averageEngagementsByDayForMentions
    },
  },
  created() {
    this.colors = ['#FF0099']
    if (isAllFieldsEmpty(this.averageEngagementsByDayForMentions)) {
      this[action.GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AVERAGE_ENGAGEMENTS_BY_DAY_FOR_MENTIONS]),
    isAllFieldsEmpty,
  },
}
</script>

<style lang="scss" scoped></style>
