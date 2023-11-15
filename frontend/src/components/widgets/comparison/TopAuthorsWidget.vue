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
  name: 'ComparisonTopAuthorsWidget',
  components: {TopEntitiesStackedBarWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  provide: {
    barHeight: '55px',
  },
  computed: {
    itemsColors() {
      const authors = this.widgetDetails.widgetData
        .map((project) => project.data)
        .flat()

      return getUniqueColors(authors, 'user_name')
    },
    widgetData() {
      const {widgetData} = this.widgetDetails
      const [labels, values] = [[], []]
      widgetData.forEach((project) => {
        const sumValues = project.data.reduce((currSum, currValue) => {
          return currSum + currValue.user_count || currValue.author_posts_count
        }, 0)

        labels.push(project.project)
        values.push(
          project.data.map((author) => {
            return {
              data: [
                Math.trunc(
                  ((author.user_count || author.author_posts_count) /
                    sumValues) *
                    100
                ),
              ],
              tooltipValue: author.user_count || author.author_posts_count,
              backgroundColor: this.itemsColors.get(
                author.user_name || author.entry_author
              ),
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
