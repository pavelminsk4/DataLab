<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="customTitle || widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :chart-values="widgetData"
      :labels="legends"
      :chart-type="chartType"
      :widget-details="widgetDetails"
    />
  </component>
</template>

<script>
import {SENTIMENT_COLORS, SENTIMENT} from '@/lib/constants'
import {sortSentiment} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'SentimentColumnsStackedBarsWidget',
  components: {
    ChartsView,
    WidgetsLayout,
  },
  props: {
    widgetDetails: {type: Object, required: true},
    isSettings: {type: Boolean, default: false},
    customTitle: {type: String, default: ''},
  },
  computed: {
    chartType() {
      return (
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType ||
        'MultiTopEntitiesBarChart'
      )
    },
    widgetWrapper() {
      return this.isSettings ? 'div' : 'WidgetsLayout'
    },
    legends() {
      const {NEUTRAL, POSITIVE, NEGATIVE} = SENTIMENT
      return [
        {name: NEUTRAL, color: SENTIMENT_COLORS[NEUTRAL]},
        {name: POSITIVE, color: SENTIMENT_COLORS[POSITIVE]},
        {name: NEGATIVE, color: SENTIMENT_COLORS[NEGATIVE]},
      ]
    },
    widgetData() {
      const {widgetData} = this.widgetDetails

      const results = widgetData.map(({data, project}) => {
        const labels = Object.keys(data)
        const values = labels.map((label) => {
          const sumValues = data[label].reduce(
            (currSum, currValue) => currSum + currValue.sentiment_count,
            0
          )

          const sortedSentiment = sortSentiment(data[label])
          const results = sortedSentiment.map(
            ({sentiment, sentiment_count}) => {
              if (sentiment_count) {
                return {
                  data: [Math.trunc((sentiment_count / sumValues) * 100)],
                  tooltipValue: sentiment_count,
                  backgroundColor: SENTIMENT_COLORS[sentiment],
                  borderRadius: 12,
                  barThickness: 'flex',
                  label: sentiment,
                }
              }
            }
          )

          return results.filter((item) => item)
        })

        return {columnsLabels: project, labels, values}
      })

      return results
    },
  },
}
</script>
