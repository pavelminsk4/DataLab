<template>
  <WidgetsLayout title="Bar chart">
    <DoughnutChart
      :chart-data="config"
      :options="options"
      class="volume-chart-wrapper bar-chart"
    />
  </WidgetsLayout>
</template>

<script>
import {DoughnutChart} from 'vue-chart-3'
import {Chart, DoughnutController, ArcElement} from 'chart.js'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
Chart.register(DoughnutController, ArcElement)

export default {
  name: 'BarWidget',
  components: {
    WidgetsLayout,
    DoughnutChart,
  },
  props: {
    volume: {
      type: [Array, Object],
      default: () => [],
    },
  },
  data() {
    return {
      options: {
        plugins: {
          title: {
            text: 'Bar',
          },
        },
      },
    }
  },
  computed: {
    volumeData() {
      return Object.values(this.volume)
    },
    volumeDate() {
      return this.volumeData.map((el) => this.formatDate(el.date))
    },
    volumeCount() {
      return this.volumeData.map((el) => el.created_count)
    },
    config() {
      return {
        labels: this.volumeDate,
        datasets: [
          {
            label: 'Volume',
            data: this.volumeCount,
            backgroundColor: ['rgba(5, 95, 252, 0.2)'],
            borderColor: ['#055FFC'],
            borderWidth: 1,
          },
        ],
      }
    },
  },
  methods: {
    formatDate(date) {
      return new Date(date).toLocaleString('en-US', {
        month: 'short',
        day: 'numeric',
        year: 'numeric',
      })
    },
  },
}
</script>

<style>
.bar-chart {
  height: 80%;
  width: 90%;
}
</style>
