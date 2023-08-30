<template>
  <WidgetContainerWithSwitcher :tabs="tabs" @switch-tab="switchTab">
    <ContentVolumeWidget
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :content-volume-widget-data="widgetData"
      :colors="colors"
      :has-swithcer="true"
      :switcher-value="activeTab"
    />
  </WidgetContainerWithSwitcher>
</template>

<script>
import {COMPARISON_COLORS, SENTIMENT} from '@/lib/constants'

import WidgetContainerWithSwitcher from '@/components/widgets/WidgetContainerWithSwitcher'
import ContentVolumeWidget from '@/components/widgets/ContentVolumeWidget'

export default {
  name: 'ComparisonSentimentByPeriodWidget',
  components: {ContentVolumeWidget, WidgetContainerWithSwitcher},
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
    widgetData() {
      const formattedWidgetData = []
      this.widgetDetails.widgetData.map((project) => {
        const value = {}
        value[project.project] = project.data.map((el) => {
          const date = Object.keys(el)[0]
          return {
            date: date,
            post_count: el[date][this.activeTab],
          }
        })

        formattedWidgetData.push(value)
      })
      return formattedWidgetData
    },
    colors() {
      return COMPARISON_COLORS
    },
  },
  methods: {
    switchTab(tab) {
      this.activeTab = tab
    },
  },
}
</script>
