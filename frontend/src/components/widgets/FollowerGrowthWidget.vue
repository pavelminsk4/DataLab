<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :widget-details="widgetDetails"
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

import {defaultDate} from '@/lib/utilities'

export default {
  name: 'FollowerGrowthWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    labels() {
      if (!this.widgetData.length) return
      return this.widgetData.map(
        (el) => defaultDate(Object.keys(el)[0]).split(',')[0]
      )
    },
    chartValues() {
      if (!this.widgetData.length) return
      return [
        {
          data: this.widgetData.map((el) => Object.values(el)[0]),
        },
      ]
    },
  },
}
</script>
