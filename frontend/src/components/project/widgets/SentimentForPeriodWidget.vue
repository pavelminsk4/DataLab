<template>
  <WidgetsLayout
    :title="availableWidgets['sentiment_for_period_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <MultiLineChart
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

export default {
  name: 'SentimentForPeriodWidget',
  components: {MultiLineChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  created() {
    this[action.GET_SENTIMENT_FOR_PERIOD](this.projectId)
  },
  computed: {
    ...mapGetters({
      availableWidgets: get.AVAILABLE_WIDGETS,
      sentimentForPeriod: get.SENTIMENT_FOR_PERIOD,
    }),
    sentimentForPeriodValues() {
      return Object.values(this.sentimentForPeriod)
    },
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
