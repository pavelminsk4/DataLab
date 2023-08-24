<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :chart-values="chartValues"
    :tooltip-Labels="tooltipLabels"
    :isLegendDisplayed="isLegendDisplayed"
    :has-animation="widgets.hasAnimation"
    :is-interactive-data-shown="isInteractiveDataShown"
    :is-sentiment-chart="isSentimentChart"
    @open-interactive-data="openInteractiveData"
  />
</template>

<script>
import {mapState, mapActions} from 'vuex'
import {action} from '@store/constants'

import BaseSpinner from '@/components/BaseSpinner'
import BarChart from '@/components/charts/BarChart'
import PieChart from '@/components/charts/PieChart'
import LineChart from '@/components/charts/LineChart'
import MultiLineChart from '@/components/charts/MultiLineChart'
import MultiRadarChart from '@/components/charts/MultiRadarChart'
import RadarChart from '@/components/charts/RadarChart'
import HorizontalBarChart from '@/components/charts/HorizontalBarChart'
import DoughnutChart from '@/components/charts/DoughnutChart'
import WordCloudChart from '@/components/charts/WordCloudChart'
import WorldMapChart from '@/components/charts/WorldMapChart'
import ColoredWordCloudChart from '@/components/charts/ColoredWordCloudChart'
import StackedBarChart from '@/components/charts/StackedBarChart'
import BarLineChart from '@/components/charts/BarLineChart'
import HeatmapChart from '@/components/charts/HeatmapChart'
import TopEntitiesBarChart from '@/components/charts/TopEntitiesBarChart'
import MultiTopEntitiesBarChart from '@/components/charts/MultiTopEntitiesBarChart'

export default {
  name: 'ChartsView',
  components: {
    BaseSpinner,
    MultiLineChart,
    BarChart,
    PieChart,
    LineChart,
    HorizontalBarChart,
    MultiRadarChart,
    RadarChart,
    DoughnutChart,
    WordCloudChart,
    WorldMapChart,
    ColoredWordCloudChart,
    StackedBarChart,
    BarLineChart,
    HeatmapChart,
    TopEntitiesBarChart,
    MultiTopEntitiesBarChart,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartType: {type: String, required: true},
    widgetDetails: {type: Object, required: true},
    chartValues: {type: Array, default: () => []},
    isLegendDisplayed: {type: Boolean, default: true},
    tooltipLabels: {type: [Array, String], required: false},
    isInteractiveDataShown: {type: Boolean, default: true},
    isSentimentChart: {type: Boolean, default: false},
  },
  computed: {
    ...mapState(['loading', 'widgets']),
  },
  methods: {
    ...mapActions([
      action.SHOW_INTERACTIVE_DATA_MODAL,
      action.POST_INTERACTIVE_WIDGETS,
    ]),
    showIteractiveModalData(data) {
      this[action.SHOW_INTERACTIVE_DATA_MODAL]({
        value: {
          isShow: true,
          projectId: this.widgetDetails.projectId,
          widgetId: this.widgetDetails.id,
          data: {
            ...data,
            page_number: 1,
            posts_per_page: 4,
          },
        },
        moduleType: this.widgetDetails.moduleName,
      })
    },
    openInteractiveData(firstValue, secondValue) {
      const startOfTheDay = new Date(firstValue)
      let optimalPostWidgetData = null

      if (firstValue.includes('from')) {
        optimalPostWidgetData = firstValue.split(' ').filter((value) => {
          if (+value === 0) return value
          return +value
        })
      }

      if (
        startOfTheDay.toString() !== 'Invalid Date' &&
        !firstValue.includes('from')
      ) {
        let endOfTheDay = new Date(firstValue)
        endOfTheDay.setHours(23, 59, 59)
        this.showIteractiveModalData({
          first_value: Array.isArray(secondValue) ? secondValue : [secondValue],
          second_value: [],
          dates: [
            startOfTheDay.toLocaleString('sv-SE'),
            endOfTheDay.toLocaleString('sv-SE'),
          ],
        })
      } else {
        this.showIteractiveModalData({
          first_value: optimalPostWidgetData || [
            firstValue.replace(/ posts/gi, ''),
          ],
          second_value: [secondValue],
          dates: [],
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.spinner {
  flex: 1;
  display: flex;
  justify-content: center;
  align-items: center;

  width: 100%;
  height: 100%;
}
</style>
