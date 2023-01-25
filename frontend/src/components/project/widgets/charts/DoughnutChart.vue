<template>
  <Doughnut
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    ref="doughnut"
    class="doughnut-chart-widget"
  />
</template>

<script>
import {Doughnut} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'

import ChartDataLabels from 'chartjs-plugin-datalabels'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
  ChartDataLabels
)

export default {
  name: 'DoughnutChart',
  components: {
    Doughnut,
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
    colors() {
      let lineColors = [
        '#055FFC',
        '#7A9EF9',
        '#47F9B9',
        '#47F979',
        '#95F947',
        '#F5F947',
        '#F6AA37',
        '#F63737',
        '#F63787',
        '#D930F4',
      ]
      let finalColors = []

      this.labels.forEach((el, index) => {
        if (this.labels[index] === 'Missing in source') {
          finalColors.push('#808080')
        } else {
          finalColors.push(lineColors[index])
        }
      })

      return finalColors
    },
    fontColors() {
      let finalFontColors = []

      this.labels.forEach((el, index) => {
        if (this.labels[index] === 'Missing in source') {
          finalFontColors.push('#808080')
        } else {
          finalFontColors.push('#ffffff')
        }
      })

      return finalFontColors
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            backgroundColor: this.colors,
            cutout: '75%',
            borderColor: 'transparent',
            spacing: 10,
            data: this.values,
            options: {
              plugins: {
                datalabels: {
                  display: false,
                },
              },
            },
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: {
            position: 'right',
            labels: {
              color: 'white',
              font: {
                size: 12,
              },
            },
          },
          datalabels: {
            color: 'white',
            textAlign: 'center',
            font: {
              size: 8,
            },
          },
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
}
</script>

<style scoped>
.doughnut-chart-widget {
  width: 100%;
  max-height: 100%;
  margin-top: 25px;

  cursor: pointer;
}
</style>
