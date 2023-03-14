<template>
  <SentimentWidget
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :sentiment-widget-data="sentimentTopLanguages"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'

import SentimentWidget from '@/components/widgets/SentimentWidget'

export default {
  name: 'SentimentTop10LanguagesWidget',
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
      sentimentTopLanguages: get.SENTIMENT_TOP_LANGUAGES,
    }),
  },
  created() {
    if (!this.sentimentTopLanguages.length) {
      this[action.GET_SENTIMENT_TOP_LANGUAGES]({
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_LANGUAGES]),
  },
}
</script>

<style scoped></style>
