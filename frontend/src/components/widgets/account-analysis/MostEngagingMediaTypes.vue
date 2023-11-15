<template>
  <MostEngagingTypesWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
    :tooltip-Labels="translatedText('Engagements')"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import translate from '@lib/mixins/translate.js'

import MostEngagingTypesWidget from '@components/widgets/MostEngagingTypesWidget'
import {isAllFieldsEmpty} from '@lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MostEngagingMediaTypesWidget',
  mixins: [translate],
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
      return Object.keys(this.mostEngagingMediaTypes).map((type) =>
        this.translatedText(type.split('_')[0])
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
    if (isAllFieldsEmpty(this.mostEngagingMediaTypes)) {
      this[action.GET_MOST_ENGAGING_MEDIA_TYPES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MOST_ENGAGING_MEDIA_TYPES]),
    isAllFieldsEmpty,
  },
}
</script>
