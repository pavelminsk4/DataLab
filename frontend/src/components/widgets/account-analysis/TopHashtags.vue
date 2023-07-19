<template>
  <TopHashtagsWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :widget-data="topHashtags"
    tooltip-Labels="Engagements"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import TopHashtagsWidget from '@/components/widgets/TopHashtagsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'TopHashtags',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {
    TopHashtagsWidget,
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    topHashtags() {
      return this.accountAnalysisWidgets.topHashtags
    },
  },
  created() {
    if (!this.topHashtags.length) {
      this[action.GET_TOP_HASHTAGS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_HASHTAGS]),
  },
}
</script>
