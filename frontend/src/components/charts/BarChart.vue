<template>
  <Bar :chart-options="chartOptions" :chart-data="chartData" />
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
import {lowerFirstLetter} from '@/lib/utilities'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'BarChart',
  components: {
    Bar,
  },
  props: {
    labels: {type: Array, default: () => []},
    chartValues: {type: Object, default: () => {}},
  },
  computed: {
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-sentiment-interactive-data',
            this.labels[dataOptions[0].index],
            lowerFirstLetter(
              dataOptions[0].element.$datalabels[0].$context.dataset.label
            )
          )
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
              display: false,
            },
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
          backgroundColor: el.color,
          data: el.data,
        })
      })

      return datasetsValue
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
