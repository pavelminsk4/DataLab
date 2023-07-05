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
  name: 'ComparisonTopAuthorsWidget',
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
      const [labels, values] = [[], []]
      widgetData.forEach((project) => {
        const sumValues = project.data.reduce((currSum, currValue) => {
          return currSum + currValue.user_count || currValue.author_posts_count
        }, 0)

        labels.push(project.project)
        values.push(
          project.data.map((author, index) => {
            return {
              data: [
                +(
                  ((author.user_count || author.author_posts_count) /
                    sumValues) *
                  100
                ).toFixed(),
              ],
              backgroundColor: PREDEFINED_COLORS[index],
              borderRadius: 12,
              barThickness: 'flex',
              label: author.user_name || author.entry_author || 'No author',
            }
          })
        )
      })

      return {labels, values}
    },
  },
}
</script>
