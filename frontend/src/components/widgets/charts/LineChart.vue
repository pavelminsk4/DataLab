<template>
  <Line
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
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement
)

export default {
  name: 'LineChart',
  components: {
    Line,
  },
  props: {
    chartValue: {
      type: Array,
      default: () => [],
    },
    chartLabels: {
      type: Array,
      default: () => [],
    },
    plugins: {
      type: Array,
      default: () => [],
    },
    chartId: {
      type: String,
      default: 'line-chart',
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
  },
  data() {
    return {
      chartOptions: {
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
      },
    }
  },
  computed: {
    chartData() {
      return {
        labels: this.chartLabels,
        datasets: [
          {
            borderColor: '#055FFC',
            pointStyle: 'circle',
            pointRadius: 5,
            pointBackgroundColor: '#055FFC',
            pointBorderWidth: 1,
            pointBorderColor: '#FFFFFF',
            borderWidth: 3,
            radius: 0.3,
            fill: true,
            backgroundColor: (ctx) => {
              const canvas = ctx.chart.ctx
              const gradient = canvas.createLinearGradient(0, 0, 0, 460)

              gradient.addColorStop(0, 'rgba(5, 95, 252, 0.5)')
              gradient.addColorStop(0.5, 'rgba(5, 95, 252, 0.25)')
              gradient.addColorStop(1, 'rgba(5, 95, 252, 0)')

              return gradient
            },
            tension: 0.25,
            data: this.chartValue,
          },
        ],
      }
    },
  },
}
</script>
