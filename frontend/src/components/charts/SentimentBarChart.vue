<template>
  <div class="chart-container">
    <Bar
      :chart-data="chartValues[0]"
      :chart-options="chartOptions"
      :height="24"
      :width="100"
    />
  </div>
</template>

<script>
import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  Title,
  Tooltip,
} from 'chart.js'

import {Bar} from 'vue-chartjs'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'SentimentBarChart',
  components: {
    Bar,
  },
  props: {
    chartValues: {type: Object, required: true},
  },
  computed: {
    chartOptions() {
      return {
        indexAxis: 'y',
        maintainAspectRatio: false,
        responsive: true,
        animation: {
          easing: 'easeInOutQuad',
          duration: 520,
        },
        plugins: {
          datalabels: {
            display: false,
          },
          legend: {
            display: false,
          },
          tooltip: {
            enabled: false,
          },
        },
        scales: {
          x: {
            display: false,
            stacked: true,
          },
          y: {
            display: false,
            stacked: true,
          },
        },
      }
    },
  },
}
</script>
<style lang="scss">
.chart-container {
  display: block;
  width: 80%;
}
</style>
