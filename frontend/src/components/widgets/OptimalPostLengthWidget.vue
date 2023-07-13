<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :tooltip-Labels="tooltipLabels"
      :widget-details="widgetDetails"
      :is-legend-displayed="false"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'OptimalPostLengthWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    newChartType: {type: String, default: ''},
    colors: {type: Array, default: () => []},
    tooltipLabels: {type: [Array, String], required: false},
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
      return [
        {
          color: this.colors.length ? this.colors : ['#FFBB00'],
          data: Object.values(this.widgetData).map((value) =>
            value ? value.toFixed() : 0
          ),
        },
      ]
    },
  },
}
</script>
