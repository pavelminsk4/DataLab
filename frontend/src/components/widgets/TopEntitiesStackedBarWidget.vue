<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="customTitle || widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :chart-values="chartValues"
      :labels="labels"
      :chart-type="chartType"
      :widget-details="widgetDetails"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'TopEntitiesStackedBarWidget',
  components: {
    ChartsView,
    WidgetsLayout,
  },
  props: {
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true},
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
  },
  computed: {
    chartType() {
      return (
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType ||
        'TopEntitiesBarChart'
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>
