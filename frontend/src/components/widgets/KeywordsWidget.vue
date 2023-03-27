<template>
  <component
    :is="widgetWrapper"
    :title="widgetDetails.title"
    style="--widget-layout-content-padding: 50px 100px"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
    />
  </component>
</template>

<script>
import {mapState} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/charts/ChartsView'

export default {
  name: 'KeywordsWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    keywordsValues: {type: Array, required: true},
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
    labels() {
      return this.keywordsValues.map((item) => item.key)
    },
    values() {
      return this.keywordsValues.map((item) => item.value * 100)
    },
    chartValues() {
      return [{data: this.values}]
    },
  },
}
</script>
