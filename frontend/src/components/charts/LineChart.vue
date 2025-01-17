<template>
  <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import {Line} from 'vue-chartjs'
import {defaultDate} from '@lib/utilities'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement,
  Filler,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement,
  Filler
)

export default {
  name: 'LineChart',
  components: {
    Line,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Object, default: () => {}},
    isLegendDisplayed: {type: Boolean, default: false},
    tooltipLabels: {type: [Array, String], required: false},
    hasAnimation: {type: Boolean, default: true},
    isInteractiveDataShown: {type: Boolean, default: true},
  },
  computed: {
    chartDatasets() {
      return [
        {
          borderColor: '#516BEE',
          pointStyle: 'circle',
          pointRadius: 4,
          pointBackgroundColor: '#FFFFFF',
          pointBorderWidth: 2,
          pointBorderColor: '#516BEE',
          borderWidth: 3,
          radius: 0.3,
          fill: true,
          backgroundColor: (ctx) => {
            const canvas = ctx.chart.ctx
            const gradient = canvas.createLinearGradient(0, 0, 0, 460)

            gradient.addColorStop(1, 'rgba(113, 135, 253, 0.1)')

            return gradient
          },
          tension: 0.5,
          data: this.chartValues[0].data,
        },
      ]
    },
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          if (!this.isInteractiveDataShown) return

          this.$emit(
            'open-interactive-data',
            this.labels[dataOptions[0].index],
            dataOptions[0].element.$datalabels[0].$context.dataset.label ||
              this.chartValues[0].label
          )
        },
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          easing: 'easeInOutQuad',
          duration: this.hasAnimation ? 520 : 0,
        },
        onHover: (event, chartElement) => {
          const target = event.native ? event.native.target : event.target
          target.style.cursor =
            chartElement[0] && this.isInteractiveDataShown
              ? 'pointer'
              : 'default'
        },
        plugins: {
          datalabels: {
            display: false,
          },
          legend: {
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
          customTitle: {
            y: {
              display: true,
              text: 'Numbers',
            },
            x: {
              display: true,
              text: 'Month',
              offsetX: 5,
              offsetY: 5,
              font: '12px Comic Sans MS',
            },
          },
        },
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
        datasets: this.chartDatasets,
      }
    },
  },
}
</script>
