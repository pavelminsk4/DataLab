<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :charts-data="chartsData"
    :isDisplayLegend="isDisplayLegend"
    @open-sentiment-interactive-data="openSentimentInteractiveData"
  />
</template>

<script>
import {mapState} from 'vuex'

import BaseSpinner from '@/components/BaseSpinner'
import BarChart2 from '@/components/charts/BarChart2'
import PieChart2 from '@/components/charts/PieChart2'
import LineChart2 from '@/components/charts/LineChart2'
import MultiLineChart2 from '@/components/charts/MultiLineChart2'
import MultiRadarChart2 from '@/components/charts/MultiRadarChart2'
import RadarChart2 from '@/components/charts/RadarChart2'
import HorizontalBarChart2 from '@/components/charts/HorizontalBarChart2'

export default {
  name: 'ChartsView2',
  components: {
    BaseSpinner,
    MultiLineChart2,
    BarChart2,
    PieChart2,
    LineChart2,
    HorizontalBarChart2,
    MultiRadarChart2,
    RadarChart2,
  },
  props: {
    labels: {
      type: Array,
      default: () => [],
    },
    chartType: {
      type: String,
      required: true,
    },
    chartsData: {
      type: Array,
      required: true,
      default: () => [],
    },
    isDisplayLegend: {
      type: Boolean,
      default: true,
      required: false,
    },
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

<style scoped></style>
