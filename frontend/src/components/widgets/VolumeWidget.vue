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
      :is-display-legend="!isSettings"
      @open-sentiment-interactive-modal="openInteractiveModal"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'VolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    labels: {type: Array, required: true},
    chartValues: {type: Array, required: true, default: () => {}},
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
  methods: {
    openInteractiveModal(source, sentiment) {
      this.$emit(
        'open-sentiment-interactive',
        source,
        sentiment,
        this.widgetDetails.id
      )
    },
  },
}
</script>
