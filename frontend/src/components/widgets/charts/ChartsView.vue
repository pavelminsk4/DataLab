<template>
  <LineChart
    v-if="false"
    :chart-data="chartData"
    :chart-options="chartOptions"
  />
  <BarChart :chart-data="chartData" :chart-options="chartOptions" />
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
  },
}
</script>

<style scoped></style>
