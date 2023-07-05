<template>
  <TopEntitiesStackedBarWidget
    v-if="widgetDetails.widgetData"
    :chart-values="widgetData.values"
    :labels="widgetData.labels"
    :widgetDetails="widgetDetails"
    v-bind:bar-height="'55px'"
  />
</template>

<script>
import {SENTIMENT_COLORS} from '@/lib/constants'

import TopEntitiesStackedBarWidget from '@/components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'SentimentWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '55px',
  },
  computed: {
    widgetData() {
      const {widgetData} = this.widgetDetails
      const [labels, values] = [[], []]

      widgetData.forEach((project) => {
        const sumValues = Object.values(project.data).reduce(
          (currSum, currValue) => currSum + currValue
        )

        labels.push(project.project)
        values.push(
          Object.entries(project.data).map((entry) => {
            return {
              data: [+((entry[1] / sumValues) * 100).toFixed()],
              backgroundColor: SENTIMENT_COLORS[entry[0]],
              borderRadius: 12,
              barThickness: 'flex',
              label: entry[0],
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
