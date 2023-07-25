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
import {
  socialSummaryWidgetConfig,
  summaryWidgetConfig,
} from '@/lib/configs/widgetsConfigs'

import SummaryTableWidget from '@components/widgets/SummaryTableWidget'

export default {
  name: 'ComparisonSummaryWidget',
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
    this.widgetMetrics =
      this.widgetData[0].data.likes !== undefined
        ? socialSummaryWidgetConfig
        : summaryWidgetConfig
  },
}
</script>
