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
    />
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'SentimentWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    sentimentWidgetData: {type: Object, required: true, default: () => {}},
    isSocial: {type: Boolean, default: false},
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
      return Object.keys(this.sentimentWidgetData)
    },
    chartValues() {
      let neutral = []
      let positive = []
      let negative = []

      Object.values(this.sentimentWidgetData).forEach((sentiment) => {
        Object.values(sentiment).filter((data) => {
          switch (data?.sentiment) {
            case 'neutral':
              return neutral.push(data.sentiment_count)
            case 'positive':
              return positive.push(data.sentiment_count)
            case 'negative':
              return negative.push(data.sentiment_count)
          }
        })
      })

      return [
        {label: 'Neutral', color: '#516BEE', data: neutral},
        {label: 'Positive', color: '#00B884', data: positive},
        {label: 'Negative', color: '#ED2549', data: negative},
      ]
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
  },
}
</script>
