<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
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
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopLanguages: get.SENTIMENT_TOP_LANGUAGES,
    }),
  },
  created() {
    if (!this.sentimentTopLanguages.length) {
      this[action.GET_SENTIMENT_TOP_LANGUAGES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_LANGUAGES]),
  },
}
</script>
