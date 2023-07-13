<template>
  <Bar :options="options" :data="data" />
</template>

<script>
import {Bar} from 'vue-chartjs'
import {Chart as ChartJS} from 'chart.js'

import ChartDataLabels from 'chartjs-plugin-datalabels'

ChartJS.register(ChartDataLabels)

export default {
  name: 'BarLineChart',
  components: {Bar},
  props: {
    chartValues: {type: Object, required: true},
    labels: {type: Array, required: true},
    tooltipLabels: {type: Array, required: false},
  },

  created() {
    this.data = {
      labels: this.labels,
      datasets: [
        {
          label: this.tooltipLabels[0],
          data: this.chartValues[0],
          borderRadius: 12,
          backgroundColor: '#C5EAFF',
          order: 1,
          datalabels: {
            display: false,
          },
        },
        {
          label: this.tooltipLabels[1],
          data: this.chartValues[1],
          borderColor: '#007EC7',
          backgroundColor: 'white',
          type: 'line',
          order: 0,
          datalabels: {
            anchor: 'start',
            align: 'top',
            clamp: true,
          },
        },
      ],
    }

    this.options = {
      onClick: (e, dataOptions) => {
        this.$emit(
          'open-interactive-data',
          this.labels[dataOptions[0].index],
          dataOptions[0].element.$datalabels[0].$context.dataset.label ||
            this.chartValues[0].label
        )
      },
      onHover: (event, chartElement) => {
        const target = event.native ? event.native.target : event.target
        target.style.cursor = chartElement[0] ? 'pointer' : 'default'
      },
      responsive: true,
      maintainAspectRatio: false,
      plugins: {
        legend: {
          display: false,
        },
        title: {
          display: false,
        },
      },
    }
  },
}
</script>
