<template>
  <TopMentionsByEngagementsWidget
    v-if="topMentionsByEngagements.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="topMentionsByEngagements"
    :table-header="tableHeader"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import TopMentionsByEngagementsWidget from '@/components/widgets/TopMentionsByEngagementsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'TopMentionsByEngagements',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {
    TopMentionsByEngagementsWidget,
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    topMentionsByEngagements() {
      return this.accountAnalysisWidgets.topMentionsByEngagements
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '5%'},
      {name: 'Mentioned by', width: ''},
      {name: 'Tweet caption', width: ''},
      {name: 'Sentiment', width: '15%'},
      {
        name: 'Engagements',
        width: '',
        sortProperty: 'engagements',
        hasSort: true,
        isDefaultSort: true,
      },
      {name: 'Likes', width: '', hasSort: true, sortProperty: 'likes'},
      {name: 'Retweets', width: '', hasSort: true, sortProperty: 'retweets'},
      {name: 'Date', width: '10%', hasSort: true, sortProperty: 'date'},
    ]
    if (!this.topMentionsByEngagements.length) {
      this[action.GET_TOP_MENTIONS_BY_ENGAGEMENTS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_MENTIONS_BY_ENGAGEMENTS]),
  },
}
</script>
