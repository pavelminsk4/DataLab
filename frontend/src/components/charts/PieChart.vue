<template>
  <Pie :options="chartOptions" :data="chartData" />
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
  components: {Pie},
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Object, default: () => {}},
    hasAnimation: {type: Boolean, default: true},
  },
  computed: {
    colors() {
      if (this.chartValues[0].colors) return this.chartValues[0].colors
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
            data: this.chartValues[0].data,
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
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.labels[dataOptions[0].index],
            dataOptions[0].element.$datalabels[0].$context.dataset.label ||
              this.chartValues[0].label
          )
        },
        hoverOffset: 10,
        animation: {
          duration: this.hasAnimation ? 1000 : 0,
        },
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
