<template>
  <SummaryTableWidget
    v-if="widgetData"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-metrics="widgetMetrics"
    :widget-data="widgetData"
  />
</template>

<script>
import {summarySentimentConfig} from '@/lib/configs/widgetsConfigs'

import SummaryTableWidget from '@components/widgets/SummaryTableWidget'

export default {
  name: 'ComparisonSentimentNumberOfResultsWidget',
  components: {SummaryTableWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    widgetData() {
      return this.widgetDetails.widgetData
    },
  },
  created() {
    this.widgetMetrics = summarySentimentConfig.map((sentiment) => ({
      ...sentiment,
      valueName: sentiment.valueName,
    }))
  },
}
</script>
