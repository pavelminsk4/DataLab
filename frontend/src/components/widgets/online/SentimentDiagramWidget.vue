<template>
  <SentimentDiagram
    v-if="sentimentDiagram"
    :widget-details="widgetDetails"
    :sentiment-diagram="sentimentDiagram"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SentimentDiagram from '@/components/widgets/SentimentDiagram'
export default {
  components: {SentimentDiagram},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentDiagram: get.SENTIMENT_DIAGRAM,
    }),
  },
  created() {
    this[action.GET_SENTIMENT_DIAGRAM]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_DIAGRAM]),
  },
}
</script>

<style lang="scss" scoped></style>
