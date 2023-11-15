<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-metrics="widgetMetrics"
    :summary-widget-data="summaryData"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import {summaryWidgetConfig} from '@lib/configs/widgetsConfigs'

import SummaryWidget from '@components/widgets/SummaryWidget'

const {mapActions, mapGetters: mapGettersOnline} =
  createNamespacedHelpers('online/widgets')

export default {
  name: 'OnlineSummaryWidget',
  components: {SummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGettersOnline({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    summaryData() {
      return this.widgetDetails.widgetData || this.onlineWidgets.summary.data
    },
    widgetId() {
      return this.onlineWidgets.summary?.id
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
