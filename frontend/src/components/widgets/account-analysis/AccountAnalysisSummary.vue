<template>
  <AccountAnalysisSummaryWidget :widget-data="summary" :stats="statistics" />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import AccountAnalysisSummaryWidget from '@/components/widgets/AccountAnalysisSummaryWidget'

import {isAllFieldsEmpty} from '@/lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'AccountAnalysisSummary',
  components: {
    AccountAnalysisSummaryWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    summary() {
      return this.accountAnalysisWidgets.summary
    },
    statistics() {
      const {stats} = this.summary
      if (isAllFieldsEmpty(stats)) return []
      return [
        {
          name: 'Total followers',
          value: stats.total_followers,
          iconName: 'List',
        },
        {
          name: 'Total following',
          value: stats.total_following,
          iconName: 'MatrixDots',
        },
        {
          name: 'Total tweets',
          value: stats.total_tweets,
          iconName: 'Twitter',
        },
        {
          name: 'Tweets this period',
          value: stats.tweets_this_period,
          iconName: 'Calendar',
        },
        {
          name: 'Engagements',
          value: stats.engagements,
          iconName: 'Engagement',
        },
        {
          name: 'AVG likes per post',
          value: stats.avg_likes_per_post,
          iconName: 'Heart',
        },
        {
          name: 'AVG retweets per post',
          value: stats.avg_retweets_per_post,
          iconName: 'Retweet',
        },
        {
          name: 'AVG engagements rate',
          value: stats.avg_engagement_rate,
          iconName: 'Graph',
        },
      ]
    },
  },
  created() {
    if (!this.summary.length) {
      this[action.GET_SUMMARY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SUMMARY]),
  },
}
</script>
