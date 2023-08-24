<template>
  <EngagementsTimelineWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
    :tooltip-Labels="currentTooltipLabels"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import translate from '@/lib/mixins/translate.js'

import EngagementsTimelineWidget from '@/components/widgets/EngagementsTimelineWidget'
import {defaultDate} from '@/lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'ProfileTimeline',
  mixins: [translate],
  components: {
    EngagementsTimelineWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      tooltipLabels: ['Tweets', 'Engagements'],
    }
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    currentTooltipLabels() {
      return this.tooltipLabels.map((tooltip) => this.translatedText(tooltip))
    },
    profileTimeline() {
      return this.accountAnalysisWidgets.profileTimeline
    },
    labels() {
      if (!this.profileTimeline.length) return []
      return this.profileTimeline.map((dateValue) => {
        return defaultDate(dateValue.date)
      })
    },
    chartValues() {
      if (!this.profileTimeline.length) return []
      const tweets = []
      const engagement = []
      this.profileTimeline.map((el) => {
        tweets.push(el.created_count), engagement.push(el.engagement)
      })
      return [tweets, engagement]
    },
  },
  created() {
    if (!this.profileTimeline.length) {
      this[action.GET_PROFILE_TIMELINE]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_PROFILE_TIMELINE]),
  },
}
</script>
