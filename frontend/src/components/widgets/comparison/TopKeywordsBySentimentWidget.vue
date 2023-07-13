<template>
  <WidgetContainerWithSwitcher :tabs="tabs" @switch-tab="switchTab">
    <ColoredKeywordsWidget
      :widget-details="widgetDetails"
      :chart-values="chartValues"
    />
  </WidgetContainerWithSwitcher>
</template>

<script>
import {COMPARISON_COLORS, SENTIMENT} from '@/lib/constants'

import WidgetContainerWithSwitcher from '@/components/widgets/WidgetContainerWithSwitcher'
import ColoredKeywordsWidget from '@/components/widgets/ColoredKeywordsWidget'

export default {
  name: 'TopKeywordsBySentimentWidget',
  components: {ColoredKeywordsWidget, WidgetContainerWithSwitcher},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      activeTab: SENTIMENT.NEUTRAL,
    }
  },
  computed: {
    tabs() {
      return [SENTIMENT.NEUTRAL, SENTIMENT.POSITIVE, SENTIMENT.NEGATIVE]
    },
    chartValues() {
      return this.widgetDetails.widgetData.map((project, index) => {
        const data = []
        const labels = []

        project.data[this.activeTab].forEach((values) => {
          labels.push(values.key)
          data.push(+(values.value * 100).toFixed(2))
        })

        return {
          type: project.project,
          color: COMPARISON_COLORS[index],
          data,
          labels,
          hasLegends: true,
        }
      })
    },
  },
  methods: {
    switchTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>
