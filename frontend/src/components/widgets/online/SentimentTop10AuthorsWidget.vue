<template>
  <SentimentWidget
    :title="title"
    :chartType="chartType"
    :is-widget="isWidget"
    :widget-id="widgetId"
    :sentiment-widget-data="sentimentTopAuthors"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import SentimentWidget from '@/components/widgets/SentimentWidget'

export default {
  name: 'SentimentTop10AuthorsWidget',
  components: {SentimentWidget},
  props: {
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopAuthors: get.SENTIMENT_TOP_AUTHORS,
    }),
  },
  created() {
    if (!this.sentimentTopAuthors.length) {
      this[action.GET_SENTIMENT_TOP_AUTHORS]({
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_AUTHORS]),
  },
}
</script>
