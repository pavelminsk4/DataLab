<template>
  <TopEntitiesStackedBarWidget
    v-if="widgetDetails.widgetData"
    v-bind="$attrs"
    :chart-values="widgetData.values"
    :labels="widgetData.labels"
    :widgetDetails="widgetDetails"
  />
</template>

<script>
import {getUniqueColors} from '@lib/utilities'

import TopEntitiesStackedBarWidget from '@components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'ComparisonTopWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
    fields: {type: Object, required: true},
  },
  provide: {
    barHeight: '55px',
  },
  computed: {
    itemsColors() {
      const widgetData = this.widgetDetails.widgetData
        .map((project) => project.data)
        .flat()

      return getUniqueColors(widgetData, this.fields.label)
    },
    widgetData() {
      const {widgetData} = this.widgetDetails
      const labels = []
      const values = []

      widgetData.forEach((project) => {
        const totalValues = project.data.reduce((sum, currValue) => {
          return sum + currValue[this.fields.value]
        }, 0)

        labels.push(project.project)
        values.push(
          project.data.map((dataset) => {
            return {
              data: [
                Math.trunc((dataset[this.fields.value] / totalValues) * 100),
              ],
              tooltipValue: dataset[this.fields.value],
              backgroundColor: this.itemsColors.get(dataset[this.fields.label]),
              borderRadius: 12,
              barThickness: 'flex',
              label: dataset[this.fields.label] || this.fields.undefinedLabel,
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
