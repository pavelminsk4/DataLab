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
import {defaultDate} from '@/lib/utilities'
import translate from '@/lib/mixins/translate.js'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'SentimentForPeriodWidget',
  mixins: [translate],
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    newChartType: {type: String, default: ''},
    sentimentForPeriod: {type: Array, required: true},
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

      return labelsCollection.map((el) =>
        this.defaultDate(el, this.platformLanguage)
      )
    },
    chartValues() {
      let neutral = []
      let positive = []
      let negative = []

      this.sentimentForPeriod.forEach((sentiment) => {
        Object.values(sentiment).forEach((data) => {
          neutral.push(data.neutral)
          positive.push(data.positive)
          negative.push(data.negative)
        })
      })

      return [
        {
          label: this.translatedText('Neutral'),
          color: '#516BEE',
          data: neutral,
        },
        {
          label: this.translatedText('Positive'),
          color: '#00B884',
          data: positive,
        },
        {
          label: this.translatedText('Negative'),
          color: '#ED2549',
          data: negative,
        },
      ]
    },
  },
  methods: {
    defaultDate,
  },
}
</script>
