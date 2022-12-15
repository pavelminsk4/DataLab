<template>
  <WidgetsLayout
    :title="this.widgets['volume_widget'].title"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart
      v-if="isLineChart"
      :chart-values="volumeValues"
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
  name: 'ContentVolumeWidget',
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
  data() {
    return {
      plugins: [],
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        animation: {
          easing: 'easeInOutQuad',
          duration: 520,
        },
        onHover: (event, chartElement) => {
          const target = event.native ? event.native.target : event.target
          target.style.cursor = chartElement[0] ? 'pointer' : 'default'
        },
        plugins: {
          legend: {
            display: false,
          },
          customTitle: {
            y: {
              display: true,
              text: 'Numbers',
            },
            x: {
              display: true,
              text: 'Month',
              offsetX: 5,
              offsetY: 5,
              font: '12px Comic Sans MS',
            },
          },
        },
      },
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
