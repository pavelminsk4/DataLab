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
import {getUniqueColors} from '@/lib/utilities'

import TopEntitiesStackedBarWidget from '@/components/widgets/TopEntitiesStackedBarWidget'

export default {
  name: 'ComparisonTopLocationsWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '55px',
  },
  computed: {
    itemsColors() {
      const locations = this.widgetDetails.widgetData
        .map((project) => project.data)
        .flat()

      return getUniqueColors(locations, 'locationString')
    },
    widgetData() {
      const {widgetData} = this.widgetDetails
      const labels = []
      const values = []

      widgetData.forEach((project) => {
        const totalValues = project.data.reduce((sum, currValue) => {
          return sum + currValue.locations_count
        }, 0)

        labels.push(project.project)
        values.push(
          project.data.map((location) => {
            return {
              data: [
                Math.trunc((location.locations_count / totalValues) * 100),
              ],
              backgroundColor: this.itemsColors.get(location.locationString),
              borderRadius: 12,
              barThickness: 'flex',
              label: location.locationString || 'No location',
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
