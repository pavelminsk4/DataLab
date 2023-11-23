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
      :is-legend-displayed="!isSettings"
      :tooltip-Labels="tooltipLabels"
    />
  </component>
</template>

<script>
import WidgetsLayout from '@components/layout/WidgetsLayout'
import ChartsView from '@components/charts/ChartsView'

export default {
  name: 'EngagementsTimelineWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true, default: () => {}},
    tooltipLabels: {type: Array, required: false},
  },
  computed: {
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    chartType() {
      return (
        this.widgetDetails.chart_type || this.widgetDetails.defaultChartType
      )
    },
  },
}
</script>

<style lang="scss" scoped></style>
