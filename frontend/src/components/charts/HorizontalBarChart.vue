<template>
  <Bar :options="chartOptions" :data="chartData" />
</template>

<script>
import {Bar} from 'vue-chartjs'
import {defaultDate} from '@lib/utilities'

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
  name: 'HorizontalBarChart',
  components: {
    Bar,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Object, default: () => {}},
    hasAnimation: {type: Boolean, default: true},
    tooltipLabels: {type: [Array, String], required: false},
  },
  computed: {
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.labels[dataOptions[0].index],
            dataOptions[0].element.$datalabels[0].$context.dataset.label
          )
        },
        indexAxis: 'y',
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          easing: 'easeInOutQuad',
          duration: this.hasAnimation ? 520 : 0,
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
        scales: {
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
          },
        },
      }
    },
    chartDatasets() {
      let datasetsValue = []
      let defaultSettings = {
        pointStyle: 'circle',
        borderWidth: 0,
        borderRadius: 12,
        barPercentage: 1,
        fill: true,
        tension: 0.25,
      }

      this.chartValues.forEach((el) => {
        datasetsValue.push({
          ...defaultSettings,
          label: el.label,
          backgroundColor: this.chartValues[0]?.colors || el.color || '#516BEE',
          data: el.data,
        })
      })

      return datasetsValue
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
