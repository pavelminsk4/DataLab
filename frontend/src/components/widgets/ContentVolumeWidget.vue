<template>
  <WidgetsLayout title="Volume">
    <BarChart
      :chart-data="config"
      :options="options"
      class="volume-chart-wrapper"
    />
  </WidgetsLayout>
</template>

<script>
import {BarChart} from 'vue-chart-3'
import {
  Chart,
  BarController,
  CategoryScale,
  LinearScale,
  BarElement,
  Tooltip,
} from 'chart.js'
import WidgetsLayout from '@/components/layout/WidgetsLayout'
Chart.register(BarController, CategoryScale, LinearScale, BarElement, Tooltip)

export default {
  name: 'ContentVolumeWidget',
  components: {
    WidgetsLayout,
    BarChart,
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

<style lang="scss">
.volume-chart-wrapper {
  position: absolute !important;
  bottom: 0;

  width: 90%;
  max-height: 84%;
}
</style>
