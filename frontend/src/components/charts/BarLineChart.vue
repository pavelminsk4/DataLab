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
  },

  created() {
    this.data = {
      labels: this.labels,
      datasets: [
        {
          label: 'Bar',
          data: this.chartValues[0],
          borderRadius: 12,
          backgroundColor: '#C5EAFF',
          order: 1,
          datalabels: {
            display: false,
          },
        },
        {
          label: 'Line',
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

<style lang="scss" scoped></style>
