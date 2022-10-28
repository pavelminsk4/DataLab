<template>
  <LineChart
    v-if="isLine"
    :chart-data="chartData"
    :chart-options="chartOptions"
    class="bar-chart-widget"
  />
  <BarChart
    v-if="isBar"
    :chart-data="chartData"
    :chart-options="chartOptions"
    class="bar-chart-widget"
  />
  <DoughnutChart
    v-if="isDoughnut"
    :chart-data="chartData"
    :chart-options="chartOptions"
  />
</template>

<script>
import LineChart from '@/components/widgets/charts/LineChart'
import BarChart from '@/components/widgets/charts/BarChart'
import DoughnutChart from '@/components/widgets/charts/DoughnutChart'

export default {
  name: 'ChartsView',
  components: {DoughnutChart, BarChart, LineChart},
  props: {
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
}
</style>
