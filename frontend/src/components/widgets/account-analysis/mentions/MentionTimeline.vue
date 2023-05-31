<template>
  <EngagementsTimelineWidget
    v-if="mentionTimeline.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import EngagementsTimelineWidget from '@/components/widgets/EngagementsTimelineWidget'
import {defaultDate} from '@/lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MentionTimeline',
  components: {
    EngagementsTimelineWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mentionTimeline() {
      return this.accountAnalysisWidgets.mentionTimeline
    },
    labels() {
      if (!this.mentionTimeline.length) return
      return this.mentionTimeline.map((el) => {
        return defaultDate(el.date).split(',')[0]
      })
    },
    chartValues() {
      if (!this.mentionTimeline.length) return
      const tweets = []
      const engagement = []
      this.mentionTimeline.map((el) => {
        tweets.push(el.created_count), engagement.push(el.engagement)
      })
      return [tweets, engagement]
    },
  },
  created() {
    if (!this.mentionTimeline.length) {
      this[action.GET_MENTION_TIMELINE]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MENTION_TIMELINE]),
  },
}
</script>
