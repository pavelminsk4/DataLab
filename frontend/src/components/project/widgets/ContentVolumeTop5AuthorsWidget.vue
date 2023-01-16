<template>
  <WidgetsLayout
    v-if="contentVolumeTopAuthors"
    :title="widgets['content_volume_top_5_authors_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart :chart-data="chartData" class="line-chart" />
  </WidgetsLayout>
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'

export default {
  name: 'ContentVolumeTop5AuthorsWidget',
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
          this.widgets['content_volume_top_5_authors_widget']
            .author_dim_pivot || null,
        language_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.widgets['content_volume_top_5_authors_widget']
            .source_dim_pivot || null,
        smpl_freq:
          this.widgets['content_volume_top_5_authors_widget']
            .aggregation_period,
      },
    })
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
        if (Object.keys(el)[0] === 'Missing in source') {
          datasetsValue.push({
            label: Object.keys(el)[0],
            borderColor: '#808080',
            pointStyle: 'circle',
            pointRadius: 3,
            pointBackgroundColor: '#808080',
            pointBorderWidth: 1,
            pointBorderColor: '#808080',
            borderWidth: 1,
            radius: 0.3,
            fill: true,
            tension: 0.3,
            data: el[Object.keys(el)].map((el) => el.post_count),
            skipNull: true,
            color: '#808080',
          })
        } else {
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
            color: '#FFFFFF',
          })
        }
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
