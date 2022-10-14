<template>
  <WidgetsLayout title="Line Chart">
    <LineChart
      :chart-data="config"
      :options="options"
      class="volume-chart-wrapper"
    />
  </WidgetsLayout>
</template>

<script>
import {LineChart} from 'vue-chart-3'
import {
  Chart,
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
} from 'chart.js'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
Chart.register(
  LineController,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement
)

export default {
  name: 'ContentVolumeWidget',
  components: {
    WidgetsLayout,
    LineChart,
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
