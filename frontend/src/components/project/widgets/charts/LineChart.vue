<template>
  <Line
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
    :css-classes="cssClasses"
    :styles="styles"
    :width="width"
    :height="height"
    class="line-chart"
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
    values: {
      type: Array,
      default: () => [],
    },
    labels: {
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
    isDisplayLegend: {
      type: Boolean,
      default: true,
    },
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
          data: this.values,
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
            display: this.isDisplayLegend,
            onClick: (evt, legendItem, legend) => {
              const datasets = legend.legendItems.map((dataset) => {
                return dataset.text
              })
              const index = datasets.indexOf(legendItem.text)
              if (legend.chart.isDatasetVisible(index) === true) {
                legend.chart.hide(index)
              } else {
                legend.chart.show(index)
              }
            },
            labels: {
              generateLabels: (chart) => {
                let visibility = []
                chart.data.datasets.forEach((el, index) => {
                  if (chart.isDatasetVisible(index) === false) {
                    visibility.push(true)
                  } else {
                    visibility.push(false)
                  }
                })

                return chart.data.datasets.map((dataset, index) => ({
                  text: dataset.label,
                  fillStyle: dataset.borderColor,
                  strokeStyle: dataset.borderColor,
                  fontColor: dataset.color,
                  hidden: visibility[index],
                }))
              },
            },
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

<style scoped>
.line-chart {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>
