<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
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
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopSources: get.SENTIMENT_TOP_SOURCES,
    }),
  },
  created() {
    if (!this.sentimentTopSources.length) {
      this[action.GET_SENTIMENT_TOP_SOURCES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_SOURCES]),
  },
}
</script>
