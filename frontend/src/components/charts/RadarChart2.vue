<template>
  <Radar :chart-options="chartOptions" :chart-data="chartData" />
</template>

<script>
import {Radar} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  PointElement,
  LineElement,
  RadialLinearScale,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  PointElement,
  RadialLinearScale,
  LineElement
)

export default {
  name: 'RadarChart2',
  components: {Radar},
  props: {
    isDisplayLegend: {type: Boolean, default: true},
    chartsData: {type: Object, default: () => {}},
    labels: {type: Array, default: () => []},
  },
  computed: {
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          this.$emit('open-interactive-data', this.labels[dataOptions[0].index])
        },
        plugins: {
          legend: {
            display: false,
          },
          datalabels: {
            display: false,
          },
        },
        elements: {
          line: {
            borderWidth: 2,
          },
        },
        scales: {
          r: {
            grid: {
              circular: true,
            },
            beginAtZero: true,
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: '',
            backgroundColor: 'rgba(124, 89, 237, 0.25)',
            borderColor: '#7C59ED',
            pointBackgroundColor: '#7C59ED',
            pointBorderColor: '#7C59ED',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#7C59ED',
            data: this.chartsData[0].data,
          },
        ],
      }
    },
  },
}
</script>

<style scoped></style>
