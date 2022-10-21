<template>
  <LineChart
    v-if="isLineChart"
    :chart-data="chartData"
    :chart-options="chartOptions"
    class="bar-chart-widget"
  />
  <BarChart
    v-else
    :chart-data="chartData"
    :chart-options="chartOptions"
    class="bar-chart-widget"
  />
</template>

<script>
import LineChart from '@/components/widgets/charts/LineChart'
import BarChart from '@/components/widgets/charts/BarChart'
export default {
  name: 'ChartsView',
  components: {BarChart, LineChart},
  props: {
    chartData: {
      type: Object,
      default: () => {},
    },
    chartOptions: {
      type: Object,
      default: () => {},
    },
    volumeValue: {
      type: [Object, Array],
      required: true,
    },
  },
  computed: {
    isLineChart() {
      return this.volumeValue?.length > 7
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
