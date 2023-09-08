<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopLanguages"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'SentimentTop10LanguagesWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    sentimentTopLanguages() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.sentimentTopLanguages.data
      )
    },
    widgetId() {
      return this.onlineWidgets.sentimentTopLanguages?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentTopLanguages) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
