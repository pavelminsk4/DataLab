<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-metrics="widgetMetrics"
    :summary-widget-data="summary"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
// import {isAllFieldsEmpty} from '@lib/utilities'
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
  },
  created() {
    this.widgetMetrics = summaryWidgetConfig

    // if (isAllFieldsEmpty(this.summary)) {
    this[action.GET_SUMMARY_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY_WIDGET]),
  },
}
</script>
