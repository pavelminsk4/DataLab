<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :values="values"
    :widget-data="widgetData"
    :neutral-values="neutralValues"
    :negative-values="negativeValues"
    :positive-values="positiveValues"
    :isDisplayLegend="isDisplayLegend"
  />
</template>

<script>
import {mapState} from 'vuex'

import BarChart from '@/components/project/widgets/charts/BarChart'
import PieChart from '@/components/project/widgets/charts/PieChart'
import LineChart from '@/components/project/widgets/charts/LineChart'
import RadarChart from '@/components/project/widgets/charts/RadarChart'
import HorizontalBarChart from '@/components/project/widgets/charts/HorizontalBarChart'
import MultiLineChart from '@/components/project/widgets/charts/MultiLineChart'
import SentimentBarChart from '@/components/project/widgets/charts/SentimentBarChart'
import SentimentHorizontalStackedBarChart from '@/components/project/widgets/charts/SentimentHorizontalStackedBarChart'
import BaseSpinner from '@/components/BaseSpinner'

export default {
  name: 'ChartsView',
  components: {
    BaseSpinner,
    BarChart,
    PieChart,
    LineChart,
    RadarChart,
    MultiLineChart,
    HorizontalBarChart,
    SentimentBarChart,
    SentimentHorizontalStackedBarChart,
  },
  props: {
    chartType: {
      type: String,
      required: true,
    },
    labels: {
      type: Array,
      default: () => [],
    },
    values: {
      type: Array,
      default: () => [],
    },
    widgetData: {
      type: Object,
      default: () => {},
    },
    neutralValues: {
      type: Array,
      default: () => [],
    },
    positiveValues: {
      type: Array,
      default: () => [],
    },
    negativeValues: {
      type: Array,
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
}
</script>

<style scoped>
.spinner {
  margin: auto;
}
</style>
