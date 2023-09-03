<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopAuthors"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SentimentTop10AuthorsWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentTopAuthors() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.sentimentTopAuthors.data
      )
    },
    widgetId() {
      return this.socialWidgets.sentimentTopAuthors?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentTopAuthors) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SENTIMENT_TOP_AUTHORS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_AUTHORS]),
  },
}
</script>
