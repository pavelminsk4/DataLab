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
      :is-display-legend="!isSettings"
    />
  </component>
</template>

<script>
import {defaultDate} from '@/lib/utilities'

import ChartsView from '@/components/charts/ChartsView'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'ContentVolumeWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    widgetDetails: {type: Object, required: true},
    newChartType: {type: String, default: ''},
    isSettings: {type: Boolean, default: false},
    colors: {type: Array, default: () => []},
    contentVolumeWidgetData: {type: Array, required: true, default: () => {}},
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
      let labelsCollection = []
      let keys = []

      Object.values(this.contentVolumeWidgetData).forEach((el) => {
        keys.push(Object.keys(el))
        labelsCollection.push(el[keys[0]])
      })

      return labelsCollection[0]?.map((el) => this.defaultDate(el.date))
    },
    chartValues() {
      let datasetsValue = []
      const defaultLineColors = [
        '#7C59ED',
        '#CDC6FF',
        '#551EB9',
        '#6AC7F0',
        '#00CC87',
        '#FD7271',
        '#FFBB01',
        '#7ACCB0',
        '#01A4EE',
        '#FFE499',
      ]

      const lineColors = this.colors.length ? this.colors : defaultLineColors

      Object.values(this.contentVolumeWidgetData).forEach(
        (volumeData, index) => {
          datasetsValue.push({
            label: Object.keys(volumeData)[0],
            color: lineColors[index],
            data: volumeData[Object.keys(volumeData)].map(
              (el) => el.post_count
            ),
          })
        }
      )

      return datasetsValue
    },
  },
  methods: {
    defaultDate,
  },
}
</script>
