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
  name: 'SentimentHorizontalStackedBarChart',
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
        indexAxis: 'y',
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
          x: {
            stacked: true,
          },
          y: {
            stacked: true,
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
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 12,
            barPercentage: 1,
            fill: true,
            backgroundColor: '#516BEE',
            tension: 0.25,
            data: this.neutralValues,
          },
          {
            label: 'Negative',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 12,
            barPercentage: 1,
            fill: true,
            backgroundColor: '#FD7271',
            tension: 0.25,
            data: this.negativeValues,
          },
          {
            label: 'Positive',
            pointStyle: 'circle',
            borderWidth: 0,
            borderRadius: 12,
            barPercentage: 1,
            fill: true,
            backgroundColor: '#57C7B3',
            tension: 0.25,
            data: this.positiveValues,
          },
        ],
      }
    },
  },
}
</script>

<style scoped></style>
