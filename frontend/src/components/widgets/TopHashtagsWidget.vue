<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="chartValues.labels"
      :chart-type="chartType"
      :chart-values="chartValues.data"
      :widget-details="widgetDetails"
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'TopHashtagsWidget',
  components: {ChartsView, WidgetsLayout},

  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
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
    chartValues() {
      const labels = []
      const values = []
      this.widgetData.forEach((el) => {
        labels.push(el[0])
        values.push(el[1])
      })

      return {
        labels,
        data: [
          {
            color: ['#516BEE'],
            data: values,
          },
        ],
      }
    },
  },
}
</script>
