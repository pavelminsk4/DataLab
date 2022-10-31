<template>
  <WidgetsLayout
    :title="this.widgets['volume_widget'].title"
    @open-modal="$emit('open-content-volume-modal')"
  >
    <ChartsView
      :chart-data="chartData"
      :chart-options="chartOptions"
      :is-line="isLineChart"
      :is-bar="isBarChart"
    />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/widgets/charts/ChartsView'

export default {
  name: 'ContentVolumeWidget',
  components: {
    ChartsView,
    WidgetsLayout,
  },
  props: {
    volume: {
      type: [Array, Object],
      default: () => [],
    },
    projectId: {
      type: [String, Number],
      required: true,
    },
    isOpenWidget: {
      type: Boolean,
      required: true,
    },
  },
  created() {
    if (this.isOpenWidget) {
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: this.widgets['volume_widget'].aggregation_period,
      })
    }
  },
  computed: {
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS}),
    volumeData() {
      return Object.values(this.volume)
    },
    volumeLabels() {
      return this.volumeData.map((el) => this.formatDate(el.date))
    },
    isLineChart() {
      return this.volumeValue?.length > 7
    },
    isBarChart() {
      return this.volumeValue?.length <= 7
    },
    volumeValue() {
      return this.volumeData.map((el) => el.created_count)
    },
    chartData() {
      return {
        labels: this.volumeLabels,
        legend: {
          display: false,
        },
        datasets: [
          {
            data: this.volumeValue,
            backgroundColor: ['rgba(5, 95, 252, 0.2)'],
            borderColor: ['#055FFC'],
            borderWidth: 1,
            tension: 0.4,
          },
        ],
      }
    },
    chartOptions() {
      return {
        plugins: {
          legend: false,
        },
        responsive: true,
        maintainAspectRatio: false,
      }
    },
  },
  watch: {
    isOpenWidget() {
      if (this.isOpenWidget) {
        this[action.GET_VOLUME_WIDGET]({
          projectId: this.projectId,
          value: 'day',
        })
      }
    },
  },
  methods: {
    ...mapActions([action.GET_VOLUME_WIDGET]),
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
