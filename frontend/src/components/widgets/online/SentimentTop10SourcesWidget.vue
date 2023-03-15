<template>
  <SentimentWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :sentiment-widget-data="sentimentTopSources"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import SentimentWidget from '@/components/widgets/SentimentWidget'

export default {
  name: 'SentimentTop10SourcesWidget',
  components: {SentimentWidget},
  props: {
    projectId: {
      type: Number,
      required: true,
    },
    widgetId: {
      type: Number,
      required: true,
    },
    title: {
      type: String,
      required: true,
    },
    chartType: {
      type: String,
      required: true,
    },
    isWidget: {
      type: Boolean,
      default: true,
    },
  },
  computed: {
    ...mapGetters({
      sentimentTopSources: get.SENTIMENT_TOP_SOURCES,
    }),
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
