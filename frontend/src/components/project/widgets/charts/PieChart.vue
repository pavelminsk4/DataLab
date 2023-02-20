<template>
  <Pie
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
import {Pie} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  ArcElement,
  CategoryScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, ArcElement, CategoryScale)

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
  name: 'PieChart',
  components: {
    Pie,
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
        '#6AC7F0',
        '#CDC6FF',
        '#01A4EE',
        '#FFBB01',
        '#00CC87',
        '#551EB9',
        '#7C59ED',
        '#FFE499',
        '#7ACCB0',
        '#8779B2',
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
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            backgroundColor: this.colors,
            cutout: '0%',
            borderColor: 'red',
            borderWidth: 0,
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
            position: 'bottom',
            labels: {
              color: '#484c52',
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
