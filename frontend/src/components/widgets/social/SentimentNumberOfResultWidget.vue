<template>
  <SentimentOverallWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="numOfResults"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentOverallWidget from '@/components/widgets/SentimentOverallWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'OnlineSentimentNumberOfResultsWidget',
  components: {SentimentOverallWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    numOfResults() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.sentimentNumberOfResult.data
      )
    },
    widgetId() {
      return this.socialWidgets.sentimentNumberOfResult?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.numOfResults) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SENTIMENT_NUMBER_OF_RESULT]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_NUMBER_OF_RESULT]),
  },
}
</script>
