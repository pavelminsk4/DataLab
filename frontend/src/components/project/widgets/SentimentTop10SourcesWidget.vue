<template>
  <WidgetsLayout
    v-if="sentimentTopSources && isGeneralWidget"
    :title="widgets['sentiment_top_10_sources_widget'].title"
    @delete-widget="$emit('delete-widget')"
    @open-modal="$emit('open-settings-modal')"
  >
    <ChartsView
      :labels="labels"
      :neutral-values="sentiment.neutral"
      :negative-values="sentiment.negative"
      :positive-values="sentiment.positive"
      :chart-type="chartType"
    />
  </WidgetsLayout>

  <ChartsView
    v-else
    :labels="labels"
    :neutral-values="sentiment.neutral"
    :negative-values="sentiment.negative"
    :positive-values="sentiment.positive"
    :chart-type="chartType"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import WidgetsLayout from '@/components/layout/WidgetsLayout'
import ChartsView from '@/components/project/widgets/charts/ChartsView'

export default {
  name: 'SentimentTop10SourcesWidget',
  components: {ChartsView, WidgetsLayout},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
    isGeneralWidget: {
      type: Boolean,
      default: true,
    },
  },
  data() {
    return {
      neutral: [],
      positive: [],
      negative: [],
    }
  },
  computed: {
    ...mapGetters({
      sentimentTopSources: get.SENTIMENT_TOP_SOURCES,
      widgets: get.AVAILABLE_WIDGETS,
    }),
    labels() {
      return Object.keys(this.sentimentTopSources)
    },
    sentiment() {
      let neutral = []
      let positive = []
      let negative = []

      Object.values(this.sentimentTopSources).forEach((el) => {
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
  created() {
    if (!this.sentimentTopSources.length) {
      this[action.GET_SENTIMENT_TOP_SOURCES]({
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_SOURCES]),
  },
}
</script>

<style scoped></style>
