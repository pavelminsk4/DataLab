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
  name: 'ComparisonTopLanguagesWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '55px',
  },
  computed: {
    itemsColors() {
      const languages = this.widgetDetails.widgetData
        .map((project) => project.data)
        .flat()

      return getUniqueColors(languages, 'language')
    },
    widgetData() {
      const {widgetData} = this.widgetDetails
      const labels = []
      const values = []

      widgetData.forEach((project) => {
        const totalValues = project.data.reduce((sum, currValue) => {
          return sum + currValue.language_count
        }, 0)

        labels.push(project.project)
        values.push(
          project.data.map((language) => {
            return {
              data: [Math.trunc((language.language_count / totalValues) * 100)],
              tooltipValue: language.language_count,
              backgroundColor: this.itemsColors.get(language.language),
              borderRadius: 12,
              barThickness: 'flex',
              label: language.language || 'No language',
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
