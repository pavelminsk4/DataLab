<template>
  <SentimentKeywordsWidget
    :widget-details="widgetDetails"
    :keywords-values="sentimentTopKeywords"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentKeywordsWidget from '@components/widgets/SentimentKeywordsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'SentimentTopKeywordsWidget',
  components: {SentimentKeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    sentimentTopKeywords() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.sentimentTopKeywordsWidget.data
      )
    },
    widgetId() {
      return this.onlineWidgets.sentimentTopKeywordsWidget?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentTopKeywords) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
