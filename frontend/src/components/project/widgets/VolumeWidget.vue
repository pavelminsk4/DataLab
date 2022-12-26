<template>
  <WidgetsLayout
    :title="this.widgets['volume_widget'].title"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart
      v-if="isLineChart"
      :datasets="chartDatasets"
      :chart-labels="volumeLabels"
    />
    <BarChart
      v-else
      :chart-values="volumeValues"
      :chart-labels="volumeLabels"
    />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'
import BarChart from '@/components/project/widgets/charts/BarChart'

export default {
  name: 'VolumeWidget',
  components: {BarChart, LineChart, WidgetsLayout},
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
    if (this.isOpenWidget && !this.volume.length) {
      this[action.GET_VOLUME_WIDGET]({
        projectId: this.projectId,
        value: {
          author_dim_pivot:
            this.widgets['volume_widget'].author_dim_pivot || null,
          language_dim_pivot:
            this.widgets['volume_widget'].language_dim_pivot || null,
          country_dim_pivot:
            this.widgets['volume_widget'].country_dim_pivot || null,
          sentiment_dim_pivot:
            this.widgets['volume_widget'].sentiment_dim_pivot || null,
          source_dim_pivot:
            this.widgets['volume_widget'].source_dim_pivot || null,
          smpl_freq: this.widgets['volume_widget'].aggregation_period,
        },
      })
    }
  },
  computed: {
    ...mapGetters({
      widgets: get.AVAILABLE_WIDGETS,
      volumeWidgetData: get.VOLUME_WIDGET,
    }),
    volumeData() {
      return Object.values(this.volume)
    },
    volumeLabels() {
      return this.volumeData.map((el) => this.formatDate(el.date))
    },
    isLineChart() {
      return this.volumeValues?.length > 7
    },
    volumeValues() {
      return this.volumeData.map((el) => el.created_count)
    },
    chartDatasets() {
      return [
        {
          borderColor: '#055FFC',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#055FFC',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 3,
          radius: 0.3,
          fill: true,
          backgroundColor: (ctx) => {
            const canvas = ctx.chart.ctx
            const gradient = canvas.createLinearGradient(0, 0, 0, 460)

            gradient.addColorStop(0, 'rgba(5, 95, 252, 0.5)')
            gradient.addColorStop(0.5, 'rgba(5, 95, 252, 0.25)')
            gradient.addColorStop(1, 'rgba(5, 95, 252, 0)')

            return gradient
          },
          tension: 0.25,
          data: this.volumeValues,
        },
      ]
    },
  },
  watch: {
    isOpenWidget() {
      if (this.isOpenWidget) {
        this[action.GET_VOLUME_WIDGET]({
          projectId: this.projectId,
          value: {
            smpl_freq: this.widgets['volume_widget'].aggregation_period,
            author_dim_pivot:
              this.widgets['volume_widget'].author_dim_pivot || null,
            language_dim_pivot:
              this.widgets['volume_widget'].language_dim_pivot || null,
            country_dim_pivot:
              this.widgets['volume_widget'].country_dim_pivot || null,
            sentiment_dim_pivot:
              this.widgets['volume_widget'].sentiment_dim_pivot || null,
            source_dim_pivot:
              this.widgets['volume_widget'].source_dim_pivot || null,
          },
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
