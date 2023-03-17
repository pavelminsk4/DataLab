<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
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
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    sentimentWidgetData: {type: Object, required: true, default: () => {}},
  },
  computed: {
    labels() {
      return Object.keys(this.sentimentWidgetData)
    },
    chartValues() {
      let neutral = []
      let positive = []
      let negative = []

      Object.values(this.sentimentWidgetData).forEach((sentiment) => {
        Object.values(sentiment).filter((data) => {
          switch (data.sentiment) {
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
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
  },
  methods: {
    openInteractiveModal(source, sentiment) {
      this.$emit('open-sentiment-interactive', source, sentiment, this.widgetId)
    },
  },
}
</script>
