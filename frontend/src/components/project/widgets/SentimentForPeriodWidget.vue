<template>
  <WidgetsLayout
    v-if="sentimentForPeriod"
    :title="availableWidgets['sentiment_for_period_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <LineChart
      v-if="isLineChart"
      :chart-data="chartData"
      :is-display-legend="false"
    />

    <PatternsBarChart
      v-else
      :chart-labels="labels"
      :neutral-values="sentiments.neutral"
      :negative-values="sentiments.negative"
      :positive-values="sentiments.positive"
    />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import LineChart from '@/components/project/widgets/charts/LineChart'
import PatternsBarChart from '@/components/project/widgets/charts/PatternsBarChart'

export default {
  name: 'SentimentForPeriodWidget',
  components: {LineChart, PatternsBarChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_SENTIMENT_FOR_PERIOD]({
      projectId: this.projectId,
      value: {
        author_dim_pivot:
          this.availableWidgets['sentiment_for_period_widget']
            .author_dim_pivot || null,
        language_dim_pivot:
          this.availableWidgets['sentiment_for_period_widget']
            .language_dim_pivot || null,
        country_dim_pivot:
          this.availableWidgets['sentiment_for_period_widget']
            .country_dim_pivot || null,
        sentiment_dim_pivot:
          this.availableWidgets['sentiment_for_period_widget']
            .sentiment_dim_pivot || null,
        source_dim_pivot:
          this.availableWidgets['sentiment_for_period_widget']
            .source_dim_pivot || null,
        smpl_freq:
          this.availableWidgets['sentiment_for_period_widget']
            .aggregation_period,
      },
    })
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      sentimentForPeriod: get.SENTIMENT_FOR_PERIOD,
    }),
    labels() {
      let labelsCollection = []

      this.sentimentForPeriod.forEach((el) => {
        Object.keys(el).forEach((i) => {
          labelsCollection.push(i)
        })
      })

      return labelsCollection.map((el) => this.formatDate(el))
    },
    sentiments() {
      let neutral = []
      let positive = []
      let negative = []

      this.sentimentForPeriod.forEach((el) => {
        Object.values(el).forEach((i) => {
          neutral.push(i.neutral)
          positive.push(i.positive)
          negative.push(i.negative)
        })
      })

      return {
        neutral: [...neutral],
        positive: [...positive],
        negative: [...negative],
      }
    },
    isLineChart() {
      return this.labels?.length > 7
    },
    chartDatasets() {
      return [
        {
          borderColor: '#F6AA37',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F6AA37',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.neutral,
          skipNull: true,
        },
        {
          borderColor: '#30F47E',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#30F47E',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.positive,
          skipNull: true,
        },
        {
          borderColor: '#F94747',
          pointStyle: 'circle',
          pointRadius: 3,
          pointBackgroundColor: '#F94747',
          pointBorderWidth: 1,
          pointBorderColor: '#FFFFFF',
          borderWidth: 1,
          radius: 0.3,
          fill: true,
          tension: 0.3,
          data: this.sentiments.negative,
          skipNull: true,
        },
      ]
    },
    chartData() {
      return {
        labels: this.labels,
        datasets: this.chartDatasets,
      }
    },
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_FOR_PERIOD]),
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

<style scoped></style>
