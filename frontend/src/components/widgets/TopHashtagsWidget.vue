<template>
  <component
    :is="widgetWrapper"
    :widget-id="widgetDetails.id"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="chartValues.labels"
      :chart-type="chartType"
      :chart-values="chartValues.data"
      :widget-details="widgetDetails"
      :tooltip-Labels="tooltipLabels"
      :is-legend-displayed="!isSettings"
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
    tooltipLabels: {type: [Array, String], required: false},
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
      const widgetValues = []

      this.widgetData.forEach((el) => {
        widgetValues.push({label: el[0], value: el[1]})
      })

      widgetValues.sort((a, b) => a.value - b.value)

      const labels = widgetValues.map((widgetVal) => widgetVal.label)
      const values = widgetValues.map((widgetVal) => widgetVal.value)

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
