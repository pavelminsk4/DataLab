<template>
  <SentimentKeywordsWidget
    :widget-details="widgetDetails"
    :keywords-values="sentimentTopKeywords"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SentimentKeywordsWidget from '@/components/widgets/SentimentKeywordsWidget'

export default {
  name: 'SentimentTopKeywordsWidget',
  components: {SentimentKeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopKeywords: get.SENTIMENT_TOP_KEYWORDS_WIDGET,
    }),
  },
  created() {
    if (!this.sentimentTopKeywords.length) {
      this[action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_KEYWORDS_WIDGET]),
  },
}
</script>

<style scoped></style>
