<template>
  <div>Matrix chart</div>
  <div class="chart-container">
    <canvas id="matrix-chart"></canvas>
  </div>
</template>

<script>
import {Chart, TimeScale} from 'chart.js'
import {MatrixController, MatrixElement} from 'chartjs-chart-matrix'
import 'chartjs-adapter-date-fns'

Chart.register(MatrixController, MatrixElement, TimeScale)

export default {
  name: 'MatrixChart',
  mounted() {
    new Chart('matrix-chart', {
      type: 'matrix',
      data: {
        datasets: [
          {
            label: 'Basic matrix',
            data: [
              {x: 1, y: 1},
              {x: 2, y: 1},
              {x: 1, y: 2},
              {x: 2, y: 2},
            ],
            borderWidth: 1,
            borderColor: 'rgba(0,0,0,0.5)',
            backgroundColor: 'rgba(200,200,0,0.3)',
            width: ({chart}) => (chart.chartArea || {}).width / 2 - 1,
            height: ({chart}) => (chart.chartArea || {}).height / 2 - 1,
          },
        ],
      },
      options: {
        scales: {
          x: {
            display: true,
            min: 0.5,
            max: 2.5,
            offset: false,
          },
          y: {
            min: 0.5,
            max: 2.5,
          },
        },
      },
    })
  },
}
</script>

<style lang="scss" scoped></style>
