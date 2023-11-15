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
      :chart-type="chartType"
      :widget-details="widgetDetails"
    />
  </component>
</template>

<script>
import {sortSentiment} from '@lib/utilities'

import ChartsView from '@components/charts/ChartsView'
import WidgetsLayout from '@components/layout/WidgetsLayout'
import {GENDER_COLORS} from '@lib/constants'

export default {
  name: 'GenderColumnsStackedBarsWidget',
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
    widgetData() {
      const {widgetData} = this.widgetDetails

      const results = widgetData.map(({data, project}) => {
        const labels = Object.keys(data)
        const values = labels.map((label) => {
          const sumValues = data[label].reduce(
            (currSum, currValue) => currSum + currValue.count,
            0
          )

          const sortedSentiment = sortSentiment(data[label])
          const results = sortedSentiment.map(({gender, count}) => {
            if (count) {
              return {
                data: [Math.trunc((count / sumValues) * 100)],
                tooltipValue: count,
                backgroundColor: GENDER_COLORS[gender],
                borderRadius: 12,
                barThickness: 'flex',
                label: gender,
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
