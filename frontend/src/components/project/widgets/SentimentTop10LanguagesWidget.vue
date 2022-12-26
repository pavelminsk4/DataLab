<template>
  <WidgetsLayout
    v-if="sentimentTopLanguages"
    :title="widgets['sentiment_top_10_languages_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <PatternsBarChart
      :chart-labels="labels"
      :neutral-values="sentiment.neutral"
      :negative-values="sentiment.negative"
      :positive-values="sentiment.positive"
    />
  </WidgetsLayout>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import PatternsBarChart from '@/components/project/widgets/charts/PatternsBarChart'

export default {
  name: 'SentimentTop10LanguagesWidget',
  components: {PatternsBarChart, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
  },
  data() {
    return {
      neutral: [],
      positive: [],
      negative: [],
    }
  },
  created() {
    if (!this.sentimentTopLanguages.length) {
      this[action.GET_SENTIMENT_TOP_LANGUAGES](this.projectId)
    }
  },
  computed: {
    ...mapGetters({
      sentimentTopLanguages: get.SENTIMENT_TOP_LANGUAGES,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    labels() {
      return Object.keys(this.sentimentTopLanguages)
    },
    sentiment() {
      let neutral = []
      let positive = []
      let negative = []

      Object.values(this.sentimentTopLanguages).forEach((el) => {
        Object.values(el).filter((i) => {
          switch (i.sentiment) {
            case 'neutral':
              return neutral.push(i.sentiment_count)
            case 'positive':
              return positive.push(i.sentiment_count)
            case 'negative':
              return negative.push(i.sentiment_count)
          }
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
    ...mapActions([action.GET_SENTIMENT_TOP_LANGUAGES]),
  },
}
</script>

<style scoped></style>
