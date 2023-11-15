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
      :chart-type="chartType"
      :chart-values="chartValues"
      :widget-details="widgetDetails"
      :tooltip-Labels="translatedText('Followers')"
      :is-legend-displayed="!isSettings"
      :is-interactive-data-shown="false"
    />
  </component>
</template>

<script>
import ChartsView from '@components/charts/ChartsView'
import WidgetsLayout from '@components/layout/WidgetsLayout'

import {defaultDate} from '@lib/utilities'
import translate from '@lib/mixins/translate.js'

export default {
  name: 'FollowerGrowthWidget',
  mixins: [translate],
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
    labels() {
      return Object.keys(this.widgetData).map((key) =>
        defaultDate(key.split(',')[0], this.platformLanguage)
      )
    },
    chartValues() {
      return [
        {
          data: Object.values(this.widgetData),
        },
      ]
    },
  },
}
</script>
