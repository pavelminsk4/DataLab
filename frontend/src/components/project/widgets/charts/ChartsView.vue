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
    @open-interactive-data="openInteractiveData"
    @open-sentiment-interactive-data="openSentimentInteractiveData"
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
import MultiRadarChart from '@/components/project/widgets/charts/MultiRadarChart'
import SentimentBarChart from '@/components/project/widgets/charts/SentimentBarChart'
import SentimentHorizontalStackedBarChart from '@/components/project/widgets/charts/SentimentHorizontalStackedBarChart'
import BaseSpinner from '@/components/BaseSpinner'
import InteractiveWidgetModal from '@/components/modals/InteractiveWidgetModal'

export default {
  name: 'ChartsView',
  components: {
    InteractiveWidgetModal,
    BaseSpinner,
    BarChart,
    PieChart,
    LineChart,
    RadarChart,
    MultiLineChart,
    MultiRadarChart,
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
  methods: {
    openInteractiveData(value) {
      this.$emit('open-interactive-modal', value)
    },
    openSentimentInteractiveData(source, sentiment) {
      this.$emit('open-sentiment-interactive-modal', source, sentiment)
    },
  },
}
</script>

<style scoped>
.spinner {
  margin: auto;
}
</style>
