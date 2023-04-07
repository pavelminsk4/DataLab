<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :chart-values="chartValues"
    :isDisplayLegend="isDisplayLegend"
    @open-sentiment-interactive-data="openSentimentInteractiveData"
  />
</template>

<script>
import {mapState} from 'vuex'

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
  },
  emits: ['open-sentiment-interactive-modal'],
  props: {
    labels: {type: Array, default: () => []},
    chartType: {type: String, required: true},
    chartValues: {type: Array, required: true, default: () => []},
    isDisplayLegend: {type: Boolean, default: true, required: false},
  },
  computed: {
    ...mapState(['loading']),
  },
  methods: {
    openSentimentInteractiveData(source, sentiment) {
      this.$emit('open-sentiment-interactive-modal', source, sentiment)
    },
  },
}
</script>
