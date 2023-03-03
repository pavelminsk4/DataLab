<template>
  <Radar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
  />
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
  name: 'RadarChart',
  components: {
    Radar,
  },
  props: {
    chartId: {
      type: String,
      default: 'doughnut-chart',
    },
    datasetIdKey: {
      type: String,
      default: 'label',
    },
    width: {
      type: Number,
      default: 400,
    },
    height: {
      type: Number,
      default: 400,
    },
    cssClasses: {
      default: '',
      type: String,
    },
    styles: {
      type: Object,
      default: () => {},
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    labels: {
      type: Array,
      default: () => [],
    },
    values: {
      type: Array,
      default: () => [],
    },
  },
  computed: {
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
            data: this.values,
          },
        ],
      }
    },
    chartOptions() {
      return {
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
  },
}
</script>

<style scoped></style>
