<template>
  <Line :options="chartOptions" :data="chartData" />
</template>

<script>
import {Line} from 'vue-chartjs'

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
    isDisplayLegend: {type: Boolean, default: false},
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
          this.$emit('open-interactive-data', this.labels[dataOptions[0].index])
        },
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          easing: 'easeInOutQuad',
          duration: 520,
        },
        onHover: (event, chartElement) => {
          const target = event.native ? event.native.target : event.target
          target.style.cursor = chartElement[0] ? 'pointer' : 'default'
        },
        plugins: {
          datalabels: {
            display: false,
          },
          legend: {
            display: false,
          },
          tooltip: {
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
      return {
        labels: this.labels,
        datasets: this.chartDatasets,
      }
    },
  },
}
</script>
