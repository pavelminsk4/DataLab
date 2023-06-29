<template>
  <SentimentKeywordsWidget
    :widget-details="widgetDetails"
    :keywords-values="sentimentTopKeywords"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@/lib/utilities'

import SentimentKeywordsWidget from '@/components/widgets/SentimentKeywordsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SentimentTopKeywordsWidget',
  components: {
    SentimentKeywordsWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentTopKeywords() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets.sentimentTopKeywords
      )
    },
  },
  created() {
    if (
      !this.widgetDetails.widgetData &&
      isAllFieldsEmpty(this.sentimentTopKeywords)
    ) {
      this[action.GET_SENTIMENT_TOP_KEYWORDS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_KEYWORDS]),
  },
}
</script>

<style scoped></style>
