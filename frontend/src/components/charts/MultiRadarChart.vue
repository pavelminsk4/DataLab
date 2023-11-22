<template>
  <Radar :options="chartOptions" :data="chartData" />
</template>

<script>
import {Radar} from 'vue-chartjs'
import {defaultDate} from '@lib/utilities'

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
  name: 'MultiRadarChart',
  components: {Radar},
  props: {
    isLegendDisplayed: {type: Boolean, default: true},
    chartValues: {type: Object, default: () => {}},
    labels: {type: Array, default: () => []},
    hasAnimation: {type: Boolean, default: true},
  },
  computed: {
    chartDatasets() {
      let datasetsValue = []

      this.chartValues.forEach((el) => {
        datasetsValue.push({
          label: el.label,
          data: el.data,
          borderColor: el.color,
          pointBackgroundColor: el.color,
          pointHoverBackgroundColor: '#fff',
          pointHoverBorderColor: '#7C59ED',
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
          duration: this.hasAnimation ? 520 : 0,
        },
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.labels[dataOptions[0].index],
            dataOptions.map(
              (el) => el.element.$datalabels[0].$context.dataset.label
            )
          )
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
            display: this.isLegendDisplayed,
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
        elements: {
          line: {
            borderWidth: 2,
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
