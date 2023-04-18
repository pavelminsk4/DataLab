<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-values="chartValues"
      :chart-type="chartType"
      :widget-details="widgetDetails"
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'SentimentDiagram',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    sentimentDiagram: {type: Object, required: true},
  },
  computed: {
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    labels() {
      return ['Positive', 'Negative', 'Neutral'].map((el) => el + ' posts')
    },
    chartValues() {
      return [
        {
          data: Object.values(this.sentimentDiagram),
          colors: ['#00b884', '#ed2549', '#516bee'],
        },
      ]
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>
