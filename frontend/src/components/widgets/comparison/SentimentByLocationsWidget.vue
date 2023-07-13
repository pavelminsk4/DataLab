<template>
  <SentimentColumnsStackedBarsWidget
    v-if="widgetDetails.widgetData"
    :widget-data="widgetData"
    :legends="legends"
    :widget-details="widgetDetails"
  />
</template>

<script>
import {SENTIMENT_COLORS, SENTIMENT} from '@/lib/constants'

import SentimentColumnsStackedBarsWidget from '@/components/widgets/SentimentColumnsStackedBarsWidget'

export default {
  name: 'SentimentByLocationsWidget',
  components: {SentimentColumnsStackedBarsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '32px',
  },
  computed: {
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
          const results = data[label].map(({sentiment, sentiment_count}) => {
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
          })

          return results.filter((item) => item)
        })

        return {columnsLabels: project, labels, values}
      })

      return results
    },
  },
}
</script>
