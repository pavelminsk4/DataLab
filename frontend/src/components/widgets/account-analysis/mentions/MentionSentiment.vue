<template>
  <SentimentDiagram
    :widget-details="widgetDetails"
    :sentiment-diagram="mentionSentiment"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import SentimentDiagram from '@/components/widgets/SentimentDiagram'

const {mapGetters, mapActions} = createNamespacedHelpers(
  'accountAnalysis/widgets'
)

export default {
  name: 'MentionSentiment',
  components: {SentimentDiagram},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      widgets: get.ACCOUNT_ANALYSIS_WIDGETS,
    }),
    mentionSentiment() {
      return this.widgets.mentionSentiment
    },
  },
  created() {
    if (!this.mentionSentiment.length) {
      this[action.GET_MENTION_SENTIMENT]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_MENTION_SENTIMENT]),
  },
}
</script>
