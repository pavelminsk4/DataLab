<template>
  <BaseSpinner v-if="loading" class="spinner" />

  <component
    v-else
    :is="chartType"
    :labels="labels"
    :widget-data="widgetData"
    :isDisplayLegend="isDisplayLegend"
    @open-sentiment-interactive-data="openSentimentInteractiveData"
  />
</template>

<script>
import {mapState} from 'vuex'

import BaseSpinner from '@/components/BaseSpinner'
import BarChart2 from '@/components/charts/BarChart2'
import MultiLineChart2 from '@/components/charts/MultiLineChart2'

export default {
  name: 'ChartsView2',
  components: {BaseSpinner, MultiLineChart2, BarChart2},
  props: {
    labels: {
      type: Array,
      default: () => [],
    },
    chartType: {
      type: String,
      required: true,
    },
    widgetData: {
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
