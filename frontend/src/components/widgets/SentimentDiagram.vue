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
      :chart-values="chartValues"
      :chart-type="chartType"
      :widget-details="widgetDetails"
      :is-legend-displayed="!isSettings"
    />
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'
import {capitalizeFirstLetter} from '@lib/utilities'

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
      return Object.keys(this.sentimentDiagram).map(
        (el) => capitalizeFirstLetter(el) + ' posts'
      )
    },
    chartValues() {
      const colors = {
        positive: '#00b884',
        negative: '#ed2549',
        neutral: '#516bee',
      }
      return [
        {
          data: Object.values(this.sentimentDiagram),
          colors: this.labels.map(
            (label) => colors[label.toLowerCase().split(' ')[0]]
          ),
        },
      ]
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>
