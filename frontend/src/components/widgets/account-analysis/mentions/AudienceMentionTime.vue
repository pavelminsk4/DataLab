<template>
  <TimeMapWidget
    :widget-details="widgetDetails"
    :widget-data="audienceMentionTime"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import TimeMapWidget from '@/components/widgets/TimeMapWidget'

const {mapActions, mapGetters} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'AudienceMentionTime',
  props: {
    widgetDetails: {type: Object, required: true},
  },
  components: {TimeMapWidget},
  computed: {
    ...mapGetters({
      accountAnalysisWidgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    audienceMentionTime() {
      return this.accountAnalysisWidgets.audienceMentionTime
    },
  },
  created() {
    if (isAllFieldsEmpty(this.audienceMentionTime)) {
      this[action.GET_AUDIENCE_MENTION_TIME]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
        value: this.widgetDetails.aggregation_period,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUDIENCE_MENTION_TIME]),
    isAllFieldsEmpty,
  },
}
</script>
