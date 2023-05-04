<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :chart-values="chartValues"
    :isDisplayLegend="isDisplayLegend"
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
import SentimentWordCloudChart from '@/components/charts/SentimentWordCloudChart'
import SentimentBarChart from '@/components/charts/SentimentBarChart'
import BarLineChart from '@/components/charts/BarLineChart'

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
    SentimentWordCloudChart,
    SentimentBarChart,
    BarLineChart,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartType: {type: String, required: true},
    widgetDetails: {type: Object, required: true},
    chartValues: {type: Array, required: true, default: () => []},
    isDisplayLegend: {type: Boolean, default: true, required: false},
  },
  computed: {
    ...mapState(['loading']),
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

      if (startOfTheDay.toString() !== 'Invalid Date') {
        let endOfTheDay = new Date(firstValue)
        endOfTheDay.setHours(23, 59, 59)
        this.showIteractiveModalData({
          first_value: Array.isArray(secondValue) ? secondValue : [secondValue],
          second_value: [],
          dates: [startOfTheDay, endOfTheDay],
        })
      } else {
        this.showIteractiveModalData({
          first_value: [firstValue.replace(/ posts/gi, '')],
          second_value: [secondValue],
          dates: [],
        })
      }
    },
  },
}
</script>
