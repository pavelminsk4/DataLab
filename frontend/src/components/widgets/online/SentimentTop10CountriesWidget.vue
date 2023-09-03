<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopCountries"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
// import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

export default {
  name: 'SentimentTop10CountriesWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopCountries: get.SENTIMENT_TOP_COUNTRIES,
    }),
  },
  created() {
    // if (isAllFieldsEmpty(this.sentimentTopCountries)) {
    this[action.GET_SENTIMENT_TOP_COUNTRIES]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_COUNTRIES]),
  },
}
</script>
