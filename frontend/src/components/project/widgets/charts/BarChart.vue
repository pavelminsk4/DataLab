<template>
  <Bar
    :chart-options="chartOptions"
    :chart-data="chartData"
    :chart-id="chartId"
    :dataset-id-key="datasetIdKey"
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
  name: 'BarChart',
  components: {
    Bar,
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
    chartData() {
      return {
        labels: this.labels,
        datasets: [
          {
            label: 'count',
            borderColor: '#055FFC',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 12,
            barPercentage: 0.5,
            fill: true,
            backgroundColor: '#516BEE',
            tension: 0.25,
            data: this.values,
          },
        ],
      }
    },
  },
}
</script>
