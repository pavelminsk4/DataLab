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
import {isAllEmptyFields} from '@lib/utilities'

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
      return this.socialWidgets.sentimentNumberOfResult
    },
  },
  created() {
    if (isAllEmptyFields(this.numOfResults)) {
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
