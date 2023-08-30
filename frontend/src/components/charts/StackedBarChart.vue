<template>
  <div class="chart-container">
    <Bar :data="chartData[0]" :options="chartOptions" :height="24" />
  </div>
</template>

<script>
import {
  BarElement,
  CategoryScale,
  Chart as ChartJS,
  Legend,
  LinearScale,
  Title,
  Tooltip,
} from 'chart.js'

import {Bar} from 'vue-chartjs'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'StackedBarChart',
  components: {
    Bar,
  },
  props: {
    iteractiveLabel: {type: String, required: false},
    chartValues: {type: Object, required: true},
    isShowTooltips: {type: Boolean, default: false},
    hasAnimation: {type: Boolean, default: true},
  },
  computed: {
    chartOptions() {
      return {
        onClick: (e, dataOptions) => {
          this.$emit(
            'open-interactive-data',
            this.iteractiveLabel,
            dataOptions[0].element.$datalabels[0].$context.dataset.label,
            dataOptions[0].index
          )
        },
        indexAxis: 'y',
        maintainAspectRatio: false,
        responsive: true,
        animation: {
          easing: 'easeInOutQuad',
          duration: this.hasAnimation ? 520 : 0,
        },
        plugins: {
          datalabels: {
            display: false,
          },
          legend: {
            display: false,
          },
          tooltip: {
            enabled: this.isShowTooltips,
            position: 'nearest',
            caretSize: 0,
            callbacks: {
              label(context) {
                const {dataset} = context
                const value =
                  dataset.tooltipValue || `${Math.trunc(dataset.data[0])}%`
                return `${dataset.label}: ${value}`
              },
            },
          },
        },
        scales: {
          x: {
            display: false,
            stacked: true,
          },
          y: {
            display: false,
            stacked: true,
          },
        },
      }
    },
    chartData() {
      return [
        {
          labels: [''],
          datasets: this.chartValues,
        },
      ]
    },
  },
}
</script>

<style lang="scss">
.chart-container {
  display: block;
  width: 80%;

  cursor: pointer;
}
</style>
