<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-metrics="widgetMetrics"
    :summary-widget-data="summaryData"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import {summaryWidgetConfig} from '@/lib/configs/widgetsConfigs'

import SummaryWidget from '@/components/widgets/SummaryWidget'

export default {
  name: 'OnlineSummaryWidget',
  components: {SummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      summary: get.SUMMARY_WIDGET,
    }),
    summaryData() {
      return this.widgetDetails.widgetData || this.summary.data
    },
    widgetId() {
      return this.summary?.id
    },
  },
  created() {
    this.widgetMetrics = summaryWidgetConfig

    const hasCurrentData =
      !isAllFieldsEmpty(this.summary) && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SUMMARY_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET]),
  },
}
</script>
