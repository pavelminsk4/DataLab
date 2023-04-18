<template>
  <SentimentDiagram
    v-if="authorsBySentiment"
    :widget-details="widgetDetails"
    :sentiment-diagram="authorsBySentiment"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import SentimentDiagram from '@/components/widgets/SentimentDiagram'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'AuthorsBySentimentWidget',
  components: {SentimentDiagram},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    authorsBySentiment() {
      return this.socialWidgets.authorsBySentiment
    },
  },
  created() {
    if (!this.authorsBySentiment.length) {
      this[action.GET_AUTHORS_BY_SENTIMENT]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_SENTIMENT]),
  },
}
</script>
