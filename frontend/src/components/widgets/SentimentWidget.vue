<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView2
      :labels="labels"
      :chart-type="chartType"
      :charts-data="widgetData"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
    />
  </component>
</template>

<script>
import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView2 from '@/components/charts/ChartsView2'
export default {
  name: 'SentimentWidget',
  components: {ChartsView2, WidgetsLayout},
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
    sentiment() {
      let neutral = []
      let positive = []
      let negative = []

      Object.values(this.sentimentWidgetData).forEach((el) => {
        Object.values(el).filter((i) => {
          switch (i.sentiment) {
            case 'neutral':
              return neutral.push(i.sentiment_count)
            case 'positive':
              return positive.push(i.sentiment_count)
            case 'negative':
              return negative.push(i.sentiment_count)
          }
        })
      })
      return {
        neutral: [...neutral],
        positive: [...positive],
        negative: [...negative],
      }
    },
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
    widgetData() {
      return [
        {label: 'Neutral', color: '#516BEE', data: this.sentiment.neutral},
        {label: 'Positive', color: '#00B884', data: this.sentiment.positive},
        {label: 'Negative', color: '#ED2549', data: this.sentiment.negative},
      ]
    },
  },
  methods: {
    openInteractiveModal(source, sentiment) {
      this.$emit('open-sentiment-interactive', source, sentiment, this.widgetId)
    },
  },
}
</script>

<style scoped></style>
