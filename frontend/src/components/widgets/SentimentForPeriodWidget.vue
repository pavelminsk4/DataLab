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
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import {defaultDate} from '@/lib/utilities'

import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SentimentForPeriodWidget',
  components: {WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    widgetData: {type: Array, required: true},
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
    labels() {
      let labelsCollection = []

      this.sentimentForPeriod.forEach((el) => {
        Object.keys(el).forEach((i) => {
          labelsCollection.push(i)
        })
      })

      return labelsCollection.map((el) => this.defaultDate(el))
    },
    sentiments() {
      let neutral = []
      let positive = []
      let negative = []

      this.sentimentForPeriod.forEach((el) => {
        Object.values(el).forEach((i) => {
          neutral.push(i.neutral)
          positive.push(i.positive)
          negative.push(i.negative)
        })
      })

      return {
        neutral: [...neutral],
        positive: [...positive],
        negative: [...negative],
      }
    },
    isLineChart() {
      return this.labels?.length > 7
    },
    chartDatasets() {
      return [
        {
          borderColor: '#F6AA37',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F6AA37',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.neutral,
          skipNull: true,
        },
        {
          borderColor: '#30F47E',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#30F47E',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.positive,
          skipNull: true,
        },
        {
          borderColor: '#F94747',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F94747',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.negative,
          skipNull: true,
        },
      ]
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: this.chartDatasets,
      }
    },
  },
  methods: {
    defaultDate,
    openInteractiveModal(source, sentiment) {
      this.$emit(
        'open-sentiment-interactive-data',
        source,
        sentiment,
        this.widgetDetails.id
      )
    },
  },
}
</script>
