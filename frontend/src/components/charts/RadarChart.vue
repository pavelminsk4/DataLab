<template>
  <Radar :options="chartOptions" :data="chartData" />
</template>

<script>
import {Radar} from 'vue-chartjs'
import {defaultDate} from '@/lib/utilities'

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
  components: {Radar},
  props: {
    isLegendDisplayed: {type: Boolean, default: true},
    chartValues: {type: Object, default: () => {}},
    labels: {type: Array, default: () => []},
  },
  computed: {
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
        plugins: {
          legend: {
            display: false,
          },
          datalabels: {
            display: false,
          },
          tooltip: {
            callbacks: {
              label: (tooltipItem) => {
                return this.tooltipLabels
                  ? `${this.tooltipLabels}: ${tooltipItem.formattedValue}`
                  : `posts: ${tooltipItem.formattedValue}`
              },
            },
            yAlign: 'bottom',
            titleColor: '#151515',
            bodyColor: '#151515',
            backgroundColor: 'rgba(255, 255, 255, 0.96)',
            displayColors: false,
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
      const isDate = !isNaN(new Date(this.labels[0]))
      let currentLabels = [...this.labels]
      if (isDate) {
        currentLabels = currentLabels.map((date) =>
          defaultDate(date, this.platformLanguage)
        )
      }
      return {
        labels: currentLabels,
        datasets: [
          {
            label: '',
            backgroundColor: 'rgba(124, 89, 237, 0.25)',
            borderColor: '#7C59ED',
            pointBackgroundColor: '#7C59ED',
            pointBorderColor: '#7C59ED',
            pointHoverBackgroundColor: '#fff',
            pointHoverBorderColor: '#7C59ED',
            data: this.chartValues[0].data,
          },
        ],
      }
    },
  },
}
</script>
