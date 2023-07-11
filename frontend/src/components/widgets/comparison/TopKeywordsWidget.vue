<template>
  <ColoredKeywordsWidget
    :widget-details="widgetDetails"
    :chart-values="chartValues"
  />
</template>

<script>
import {COMPARISON_COLORS} from '@/lib/constants'
import ColoredKeywordsWidget from '@/components/widgets/ColoredKeywordsWidget'

export default {
  name: 'TopKeywordsWidget',
  components: {ColoredKeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    chartValues() {
      return this.widgetDetails.widgetData.map((project, index) => {
        const data = []
        const labels = []

        project.data.forEach((values) => {
          labels.push(values.key)
          data.push(+(values.value * 100).toFixed(2))
        })

        return {
          type: project.project,
          color: COMPARISON_COLORS[index],
          data,
          labels,
        }
      })
    },
  },
}
</script>
