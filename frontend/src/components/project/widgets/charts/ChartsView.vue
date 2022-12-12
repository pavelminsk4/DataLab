<template>
  <LineChart
    v-if="isLine"
    :chart-value="chartValue"
    :chart-labels="chartLabels"
    :plugins="plugins"
    class="bar-chart-widget"
  />
  <BarChart
    v-if="isBar"
    :chart-value="chartValue"
    :chart-labels="chartLabels"
    :plugins="plugins"
    class="bar-chart-widget"
  />
</template>

<script>
import LineChart from '@/components/project/widgets/charts/LineChart'
import BarChart from '@/components/project/widgets/charts/BarChart'

export default {
  name: 'ChartsView',
  components: {BarChart, LineChart},
  props: {
    chartValue: {
      type: Array,
      default: () => [],
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    chartLabels: {
      type: Array,
      default: () => [],
    },
    chartData: {
      type: Object,
      default: () => {},
    },
    chartOptions: {
      type: Object,
      default: () => {},
    },
    isDoughnut: {
      type: Boolean,
      default: false,
    },
    isLine: {
      type: Boolean,
      default: false,
    },
    isBar: {
      type: Boolean,
      default: false,
    },
  },
}
</script>

<style scoped>
.bar-chart-widget {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>
