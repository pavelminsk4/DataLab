<template>
  <WidgetsLayout
    v-if="sentimentForPeriod"
    :title="availableWidgets['sentiment_for_period_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <MultiLineChart
      v-if="isLineChart"
      :chart-labels="labels"
      :neutral-values="sentiments.neutral"
      :negative-values="sentiments.negative"
      :positive-values="sentiments.positive"
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
import MultiLineChart from '@/components/project/widgets/charts/MultiLineChart'
import PatternsBarChart from '@/components/project/widgets/charts/PatternsBarChart'

export default {
  name: 'SentimentForPeriodWidget',
  components: {PatternsBarChart, MultiLineChart, WidgetsLayout},
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
