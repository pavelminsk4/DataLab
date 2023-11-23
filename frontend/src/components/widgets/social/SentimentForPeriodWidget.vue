<template>
  <SentimentForPeriodWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-for-period="sentimentForPeriod"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'

import SentimentForPeriodWidget from '@components/widgets/SentimentForPeriodWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialSentimentForPeriodWidget',
  components: {SentimentForPeriodWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentForPeriod() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.sentimentForPeriod.data
      )
    },
    widgetId() {
      return this.socialWidgets.sentimentForPeriod?.id
    },
  },
  created() {
    const hasCurrentData =
      this.sentimentForPeriod.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_FOR_PERIOD]),
  },
}
</script>
