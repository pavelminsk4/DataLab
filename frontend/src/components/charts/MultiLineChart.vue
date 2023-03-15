<template>
  <Line :chart-options="chartOptions" :chart-data="chartData" />
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
    isDisplayLegend: {type: Boolean, default: true},
    chartValues: {type: Object, default: () => {}},
    labels: {type: Array, default: () => []},
  },
  computed: {
    chartDatasets() {
      let datasetsValue = []

      this.chartValues.forEach((el) => {
        datasetsValue.push({
          label: el.label,
          borderColor: el.color,
          pointBackgroundColor: el.color,
          pointBorderColor: '#FFFFFF',
          data: el.data,
          color: '#70767D',
        })
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
}
</script>
