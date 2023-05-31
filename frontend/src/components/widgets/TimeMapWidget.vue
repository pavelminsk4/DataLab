<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      v-if="labels.length"
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :widget-details="widgetDetails"
      :is-display-legend="false"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'TimeMapWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    newChartType: {type: String, default: ''},
    colors: {type: Array, default: () => []},
  },
  computed: {
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    labels() {
      return Object.keys(this.widgetData)
    },
    chartValues() {
      const series = []
      Object.entries(this.widgetData).map((value) => {
        series.push({
          name: value[0],
          data: value[1].map((el) => el.engagements),
        })
      })
      return series
    },
  },
}
</script>
