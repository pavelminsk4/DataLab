<template>
  <div class="chart-container">
    <Bar :chart-data="chartData()" :chart-options="config" :height="50" />
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
  name: 'SentimentBarChart',
  components: {
    Bar,
  },
  props: {
    chartValues: {type: Array, required: true},
  },
  created() {
    this.config = {
      indexAxis: 'y',
      responsive: true,
      maintainAspectRatio: false,
      animation: {
        easing: 'easeInOutQuad',
        duration: 520,
      },
      plugins: {
        datalabels: {
          display: false,
        },
        legend: {
          display: false,
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
  methods: {
    chartData() {
      return {
        labels: ['Positive', 'Negative', 'Neutral'],
        datasets: [
          {
            data: this.chartValues[0].data,
            backgroundColor: Object.values(this.chartValues[0].colors),
            borderColor: Object.values(this.chartValues[0].colors),
            borderRadius: 12,
            barPercentage: 1,
            tension: 0.25,
          },
        ],
      }
    },
  },
}
</script>
<style lang="scss">
.chart-container {
  position: relative;
  height: 50px;
  div {
    position: relative;
    height: 100%;
  }
}
</style>
