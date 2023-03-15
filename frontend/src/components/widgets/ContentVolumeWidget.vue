<template>
  <component
    :is="widgetWrapper"
    :title="title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView2
      :labels="labels"
      :chart-type="chartType"
      :charts-data="chartsData"
      :is-display-legend="isWidget"
      @open-sentiment-interactive-modal="openInteractiveModal"
    />
  </component>
</template>

<script>
import {defaultDate} from '@/lib/utilities'

import ChartsView2 from '@/components/charts/ChartsView2'
import WidgetsLayout from '@/components/layout/WidgetsLayout'

export default {
  name: 'ContentVolumeWidget',
  components: {ChartsView2, WidgetsLayout},
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

      return labelsCollection[0]?.map((el) => this.defaultDate(el.date))
    },
    chartsData() {
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

      Object.values(this.contentVolumeWidgetData).forEach((el, index) => {
        datasetsValue.push({
          label: Object.keys(el)[0],
          color: lineColors[index],
          data: el[Object.keys(el)].map((el) => el.post_count),
        })
      })

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

<style scoped></style>
