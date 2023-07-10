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
import {PREDEFINED_COLORS} from '@/lib/constants'

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
          project.data.map((language, index) => {
            return {
              data: [
                Math.trunc((language.locations_count / totalValues) * 100),
              ],
              backgroundColor: PREDEFINED_COLORS[index],
              borderRadius: 12,
              barThickness: 'flex',
              label: language.locationString || 'No location',
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
