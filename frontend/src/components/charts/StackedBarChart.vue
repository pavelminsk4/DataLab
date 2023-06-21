<template>
  <div class="chart-container">
    <Bar :data="chartData[0]" :options="chartOptions" :height="24" />
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
  name: 'StackedBarChart',
  components: {
    Bar,
  },
  props: {
    chartValues: {type: Object, required: true},
    isShowTooltips: {type: Boolean, default: false},
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
            enabled: this.isShowTooltips || false,
            position: 'nearest',
            caretSize: 0,
            callbacks: {
              label(context) {
                const {dataset} = context
                return `${dataset.tooltip}: ${dataset.data[0].toFixed()}`
              },
            },
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
    chartData() {
      return [
        {
          labels: [''],
          datasets: this.chartValues,
        },
      ]
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
