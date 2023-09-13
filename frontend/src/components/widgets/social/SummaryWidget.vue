<template>
  <SummaryWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-metrics="widgetMetrics"
    :summary-widget-data="summary"
  />
</template>

<script>
import {mapGetters, createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'
import {socialSummaryWidgetConfig} from '@/lib/configs/widgetsConfigs'

import SummaryWidget from '@/components/widgets/SummaryWidget'

const {mapActions, mapGetters: mapGettersSocial} =
  createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialSummaryWidget',
  components: {SummaryWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGettersSocial({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
    }),
    summary() {
      return this.widgetDetails.widgetData || this.socialWidgets.summary.data
    },
    widgetId() {
      return this.socialWidgets.summary?.id
    },
  },
  async created() {
    this.widgetMetrics = socialSummaryWidgetConfig

    const hasCurrentData =
      !isAllFieldsEmpty(this.summary) && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      await this[action.GET_SUMMARY_WIDGET]({
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
