<template>
  <TopPostsByEngagementsWidget
    v-if="topPostsByEngagements.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="topPostsByEngagements"
    :table-header="tableHeader"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import TopPostsByEngagementsWidget from '@/components/widgets/TopPostsByEngagementsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'TopPostsByEngagements',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {
    TopPostsByEngagementsWidget,
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    topPostsByEngagements() {
      return this.accountAnalysisWidgets.topPostsByEngagements
    },
  },
  created() {
    this.tableHeader = [
      {name: '', width: '3%'},
      {name: 'Tweet caption', width: '40%'},
      {name: 'Sentiment', width: '10%'},
      {
        name: 'Engagements',
        width: '8%',
        sortProperty: 'engagements',
        hasSort: true,
        isDefaultSort: true,
      },
      {
        name: 'ENGMT Rate',
        width: '8%',
        sortProperty: 'engmt_rate',
        hasSort: true,
      },
      {name: 'Date', width: '10%', sortProperty: 'date', hasSort: true},
    ]
    if (!this.topPostsByEngagements.length) {
      this[action.GET_TOP_POSTS_BY_ENGAGEMENTS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_POSTS_BY_ENGAGEMENTS]),
  },
}
</script>
