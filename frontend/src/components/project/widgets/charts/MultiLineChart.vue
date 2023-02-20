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
  name: 'MultiLineChart',
  components: {
    Line,
  },
  props: {
    chartLabels: {
      type: Array,
      default: () => [],
    },
    datasets: {
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
    customChartData: {
      type: Object,
      default: () => {},
    },
    widgetData: {
      type: Object,
      default: () => {},
    },
    isDisplayLegend: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    labels() {
      let labelsCollection = []
      let keys = []

      Object.values(this.widgetData).forEach((el) => {
        keys.push(Object.keys(el))
        labelsCollection.push(el[keys[0]])
      })

      return labelsCollection[0]?.map((el) => this.formatDate(el.date))
    },
    chartDatasets() {
      let datasetsValue = []
      let lineColors = [
        '#516BEE',
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

      Object.values(this.widgetData).forEach((el, index) => {
        if (Object.keys(el)[0] === 'Missing in source') {
          datasetsValue.push({
            label: Object.keys(el)[0],
            borderColor: '#808080',
            pointStyle: 'circle',
            pointRadius: 3,
            pointBackgroundColor: '#808080',
            pointBorderWidth: 1,
            pointBorderColor: '#808080',
            borderWidth: 2,
            radius: 0.3,
            tension: 0.3,
            data: el[Object.keys(el)].map((el) => el.post_count),
            skipNull: true,
            color: '#808080',
          })
        } else {
          datasetsValue.push({
            label: Object.keys(el)[0],
            borderColor: lineColors[index],
            pointStyle: 'circle',
            pointRadius: 3,
            pointBackgroundColor: lineColors[index],
            pointBorderWidth: 1,
            pointBorderColor: '#FFFFFF',
            borderWidth: 2,
            radius: 0.3,
            tension: 0.3,
            data: el[Object.keys(el)].map((el) => el.post_count),
            skipNull: true,
            color: '#70767D',
          })
        }
      })

      return datasetsValue
    },
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
            display: this.isDisplayLegend,
            position: 'bottom',
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
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
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
