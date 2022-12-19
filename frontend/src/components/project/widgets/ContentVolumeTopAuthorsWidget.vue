<template>
  <WidgetsLayout
    v-if="contentVolumeTopAuthors"
    :title="widgets['content_volume_top_10_authors_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart
      :chart-options="chartOptions"
      :chart-data="chartData"
      class="line-chart"
    />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'

export default {
  name: 'ContentVolumeTopAuthors',
  components: {LineChart, WidgetsLayout},
  props: {
    projectId: {
      type: [Number, String],
      required: true,
    },
    widgets: {
      type: [Array, Object],
      default: () => [],
    },
  },
  created() {
    this[action.GET_CONTENT_VOLUME_TOP_AUTHORS]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.widgets['content_volume_top_10_authors_widget']
            .author_dim_pivot || null,
        language_dim_pivot:
          this.widgets['content_volume_top_10_authors_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.widgets['content_volume_top_10_authors_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.widgets['content_volume_top_10_authors_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.widgets['content_volume_top_10_authors_widget']
            .source_dim_pivot || null,
        smpl_freq:
          this.widgets['content_volume_top_10_authors_widget']
            .aggregation_period,
      },
    })
  },
  data() {
    return {
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        skipNull: true,
        animation: {
          easing: 'easeInOutQuad',
          duration: 520,
        },
        onHover: (event, chartElement) => {
          const target = event.native ? event.native.target : event.target
          target.style.cursor = chartElement[0] ? 'pointer' : 'default'
        },
        plugins: {
          datalabels: {
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
    ...mapGetters({
      contentVolumeTopAuthors: get.CONTENT_VOLUME_TOP_AUTHORS,
    }),
    labels() {
      let labelsCollection = []
      let keys = []

      Object.values(this.contentVolumeTopAuthors).forEach((el) => {
        keys.push(Object.keys(el))
        labelsCollection.push(el[keys[0]])
      })

      return labelsCollection[0]?.map((el) => this.formatDate(el.date))
    },
    chartDatasets() {
      let datasetsValue = []
      let lineColors = [
        '#055FFC',
        '#7A9EF9',
        '#47F9B9',
        '#47F979',
        '#95F947',
        '#F5F947',
        '#F6AA37',
        '#F63737',
        '#F63787',
        '#D930F4',
      ]

      Object.values(this.contentVolumeTopAuthors).forEach((el, index) => {
        datasetsValue.push({
          label: Object.keys(el)[0],
          borderColor: lineColors[index],
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: lineColors[index],
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: el[Object.keys(el)].map((el) => el.post_count),
          skipNull: true,
        })
      })

      return datasetsValue
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: this.chartDatasets,
      }
    },
  },
  methods: {
    ...mapActions([action.GET_CONTENT_VOLUME_TOP_AUTHORS]),
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

<style scoped>
.line-chart {
  overflow: hidden;
  height: 100%;
  width: 100%;
}
</style>
