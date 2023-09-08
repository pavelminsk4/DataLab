<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopSources"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'SentimentTop10SourcesWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    sentimentTopSources() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.sentimentTopSources.data
      )
    },
    widgetId() {
      return this.onlineWidgets.sentimentTopSources?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentTopSources) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
