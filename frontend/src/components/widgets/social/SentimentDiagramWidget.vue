<template>
  <SentimentDiagram
    v-if="sentimentDiagram"
    :widget-details="widgetDetails"
    :sentiment-diagram="sentimentDiagram"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentDiagram from '@components/widgets/SentimentDiagram'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  components: {SentimentDiagram},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentDiagram() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.sentimentDiagram.data
      )
    },
    widgetId() {
      return this.socialWidgets.sentimentDiagram?.id
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.sentimentDiagram) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SENTIMENT_DIAGRAM]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_DIAGRAM]),
  },
}
</script>
