<template>
  <WidgetsLayout
    :title="this.widgets['volume_widget'].title"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :chart-data="chartData"
      :chart-options="chartOptions"
      :is-line="isLineChart"
      :is-bar="isBarChart"
      :chart-labels="volumeLabels"
      :chart-value="volumeValue"
    />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  CategoryScale,
  LinearScale,
  PointElement,
  Filler,
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement,
  Filler
)

export default {
  name: 'ContentVolumeWidget',
  components: {WidgetsLayout, ChartsView},
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
          tooltip: {
            yAlign: 'bottom',
            titleColor: '#151515',
            bodyColor: '#151515',
            backgroundColor: 'rgba(255, 255, 255, 0.96)',
            displayColors: false,
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
    ...mapGetters({widgets: get.AVAILABLE_WIDGETS, volume: get.VOLUME_WIDGET}),
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
        datasets: [
          {
            borderColor: '#055FFC',
            pointStyle: 'circle',
            pointRadius: 5,
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
            data: this.volumeValue,
          },
        ],
      }
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
