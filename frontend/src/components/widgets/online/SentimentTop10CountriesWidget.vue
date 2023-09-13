<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopCountries"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'SentimentTop10CountriesWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    sentimentTopCountries() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.sentimentTopCountries.data
      )
    },
    widgetId() {
      return this.onlineWidgets.sentimentTopCountries?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentTopCountries) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SENTIMENT_TOP_COUNTRIES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_COUNTRIES]),
  },
}
</script>
