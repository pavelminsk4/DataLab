<template>
  <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :plugins="plugins"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    class="bar-chart"
  />
</template>

<script>
import {Bar} from 'vue-chartjs'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale,
} from 'chart.js'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'SentimentBarChart',
  components: {
    Bar,
  },
  props: {
    labels: {
      type: Array,
      default: () => [],
    },
    neutralValues: {
      type: Array,
      default: () => [],
    },
    positiveValues: {
      type: Array,
      default: () => [],
    },
    negativeValues: {
      type: Array,
      default: () => [],
    },
    chartId: {
      type: String,
      default: 'bar-chart',
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
  },
  computed: {
    chartOptions() {
      return {
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
        },
        scales: {
          y: {
            beginAtZero: true,
            grid: {
              color: 'rgba(145, 152, 167, 0.1)',
            },
          },
          x: {
            beginAtZero: true,
            grid: {
              color: 'rgba(145, 152, 167, 0.1)',
            },
          },
        },
      }
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: 'Neutral',
            borderColor: 'rgba(246, 170, 55, 1)',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 6,
            barPercentage: 0.5,
            fill: true,
            backgroundColor: (ctx) => {
              const canvas = ctx.chart.ctx
              const gradient = canvas.createLinearGradient(0, 0, 0, 460)

              gradient.addColorStop(0, 'rgba(246, 170, 55, 0.8)')
              gradient.addColorStop(0.5, 'rgba(246, 170, 55, 0.5)')
              gradient.addColorStop(1, 'rgba(246, 170, 55, 0)')

              return gradient
            },
            tension: 0.25,
            data: this.neutralValues,
          },
          {
            label: 'Negative',
            borderColor: 'rgba(249,71,71, 1)',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 6,
            barPercentage: 0.5,
            fill: true,
            backgroundColor: (ctx) => {
              const canvas = ctx.chart.ctx
              const gradient = canvas.createLinearGradient(0, 0, 0, 460)

              gradient.addColorStop(0, 'rgba(249,71,71, 0.8)')
              gradient.addColorStop(0.5, 'rgba(249,71,71, 0.5)')
              gradient.addColorStop(1, 'rgba(249,71,71, 0)')

              return gradient
            },
            tension: 0.25,
            data: this.negativeValues,
          },
          {
            label: 'Positive',
            borderColor: 'rgba(48,244,126, 1)',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 6,
            barPercentage: 0.5,
            fill: true,
            backgroundColor: (ctx) => {
              const canvas = ctx.chart.ctx
              const gradient = canvas.createLinearGradient(0, 0, 0, 460)

              gradient.addColorStop(0, 'rgba(48,244,126, 0.8)')
              gradient.addColorStop(0.5, 'rgba(48,244,126, 0.5)')
              gradient.addColorStop(1, 'rgba(48,244,126, 0)')

              return gradient
            },
            tension: 0.25,
            data: this.positiveValues,
          },
        ],
      }
    },
  },
}
</script>

<style scoped>
.bar-chart {
  overflow: hidden;

  margin-top: 20px;
  height: 100%;
  width: 100%;
}
</style>
