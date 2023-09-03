<template>
  <SentimentForPeriodWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-for-period="sentimentForPeriod"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {defaultDate} from '@/lib/utilities'

import SentimentForPeriodWidget from '@/components/widgets/SentimentForPeriodWidget'

export default {
  name: 'OnlineSentimentForPeriodWidget',
  components: {SentimentForPeriodWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentForPeriod: get.SENTIMENT_FOR_PERIOD,
    }),
  },
  created() {
    // if (!this.sentimentForPeriod.length) {
    this[action.GET_SENTIMENT_FOR_PERIOD]({
      projectId: this.widgetDetails.projectId,
      value: {
        author_dim_pivot: this.widgetDetails.author_dim_pivot || null,
        language_dim_pivot: this.widgetDetails.language_dim_pivot || null,
        country_dim_pivot: this.widgetDetails.country_dim_pivot || null,
        sentiment_dim_pivot: this.widgetDetails.sentiment_dim_pivot || null,
        source_dim_pivot: this.widgetDetails.source_dim_pivot || null,
        aggregation_period: this.widgetDetails.aggregation_period,
      },
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    defaultDate,
    ...mapActions([action.GET_SENTIMENT_FOR_PERIOD]),
  },
}
</script>
