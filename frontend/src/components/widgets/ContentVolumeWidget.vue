<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :chart-type="chartType"
      :chart-values="chartValues"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
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
    isWidget: {type: Boolean, default: true},
    title: {type: String, required: true},
    widgetId: {type: Number, required: true},
    chartType: {type: String, required: true},
    contentVolumeWidgetData: {type: Array, required: true, default: () => {}},
  },
  computed: {
    widgetWrapper() {
      return this.isWidget ? 'WidgetsLayout' : 'div'
    },
    labels() {
      let labelsCollection = []
      let keys = []

      Object.values(this.contentVolumeWidgetData).forEach((el) => {
        keys.push(Object.keys(el))
        labelsCollection.push(el[keys[0]])
      })

      return labelsCollection[0]?.map((el) =>
        this.defaultDate(el.creation_date)
      )
    },
    chartValues() {
      let datasetsValue = []
      let lineColors = [
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
    openInteractiveModal(source, sentiment) {
      this.$emit('open-sentiment-interactive', source, sentiment, this.widgetId)
    },
  },
}
</script>
