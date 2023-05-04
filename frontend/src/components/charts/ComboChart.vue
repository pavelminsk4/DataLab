<template>
  <Bar :options="options" :data="data" />
</template>

<script>
import {Bar} from 'vue-chartjs'

export default {
  name: 'ComboChart',
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
            align: 'top',
            offset: 20,
          },
        },
      ],
    }
    this.options = {
      responsive: true,
      plugins: {
        legend: {
          display: false,
          position: 'top',
        },
        title: {
          display: false,
        },
        tooltip: {
          position: 'nearest',
        },
      },
    }
  },
}
</script>

<style lang="scss" scoped></style>
