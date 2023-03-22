<template>
  <component
    v-if="chartValues.length"
    :is="widgetWrapper"
    :title="widgetDetails.title"
    style="--widget-layout-content-padding: 50px 100px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :chart-type="chartType"
      :chart-values="chartValues"
      :chart-labels="labels"
    />
  </component>
</template>

<script>
import {mapState} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'SentimentKeywordsWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    keywordsValues: {type: Object, required: true},
  },
  data() {
    return {
      labels: [],
    }
  },
  computed: {
    ...mapState(['loading']),
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
    chartValues() {
      let neutral = {data: [], labels: []}
      let positive = {data: [], labels: []}
      let negative = {data: [], labels: []}

      const sentimentsKeys = Object.keys(this.keywordsValues)

      sentimentsKeys.forEach((sentiment) => {
        switch (sentiment) {
          case 'neutral':
            return this.keywordsValues.neutral.forEach((data) => {
              neutral.data.push(data.value)
              this.labels.push(data.key)
            })
          case 'positive':
            return this.keywordsValues.positive.forEach((data) => {
              positive.data.push(data.value)
              this.labels.push(data.key)
            })
          case 'negative':
            return this.keywordsValues.negative.forEach((data) => {
              negative.data.push(data.value)
              this.labels.push(data.key)
            })
        }
      })

      return [
        {data: neutral.data, color: '#516BEE'},
        {data: positive.data, color: '#00B884'},
        {data: negative.data, color: '#ED2549'},
      ]
    },
  },
}
</script>
