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
      :widget-details="widgetDetails"
      :tooltip-Labels="tooltipLabels"
      :is-legend-displayed="false"
    />
  </component>
</template>

<script>
import ChartsView from '@components/charts/ChartsView'
import WidgetsLayout from '@components/layout/WidgetsLayout'

export default {
  name: 'MostEngagingTypesWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true, default: () => {}},
    tooltipLabels: {type: [Array, String], required: false},
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
  },
}
</script>
