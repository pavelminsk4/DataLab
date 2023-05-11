<template>
  <ProfileTimelineWidget
    v-if="profileTimeline.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :labels="labels"
    :chart-values="chartValues"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import ProfileTimelineWidget from '@/components/widgets/ProfileTimelineWidget'
import {defaultDate} from '@/lib/utilities'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'ProfileTimeline',
  components: {
    ProfileTimelineWidget,
  },
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    profileTimeline() {
      return this.accountAnalysisWidgets.profileTimeline
    },
    labels() {
      if (!this.profileTimeline.length) return
      return this.profileTimeline.map((el) => {
        return defaultDate(el.date).split(',')[0]
      })
    },
    chartValues() {
      if (!this.profileTimeline.length) return
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
