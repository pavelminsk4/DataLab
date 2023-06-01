<template>
  <SentimentOverallWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="numOfResults"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentOverallWidget from '@/components/widgets/SentimentOverallWidget'

export default {
  name: 'OnlineSentimentNumberOfResultsWidget',
  components: {SentimentOverallWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      numOfResults: get.SENTIMENT_NUMBER_OF_RESULT,
    }),
  },
  created() {
    if (isAllFieldsEmpty(this.numOfResults)) {
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
