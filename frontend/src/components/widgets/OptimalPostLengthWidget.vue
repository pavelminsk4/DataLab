<template>
  <component
    :is="'WidgetsLayout'"
    :isShowDeleteBtn="isShowDeleteBtn"
    :isShowSettingsBtn="isShowSettingsBtn"
    :title="widgetDetails.title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :widget-details="widgetDetails"
      :is-display-legend="false"
    />
  </component>
</template>

<script>
import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'OptimalPostLengthWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    widgetData: {type: Object, required: true},
    newChartType: {type: String, default: ''},
  },
  computed: {
    chartType() {
      return (
        this.newChartType ||
        this.widgetDetails.chart_type ||
        this.widgetDetails.defaultChartType
      )
    },
    labels() {
      return Object.keys(this.widgetData)
    },
    chartValues() {
      return [
        {
          color: ['#FFBB00'],
          data: Object.values(this.widgetData),
        },
      ]
    },
  },
}
</script>
