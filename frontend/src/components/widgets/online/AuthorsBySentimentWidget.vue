<template>
  <SentimentDiagram
    v-if="authorsBySentiment"
    :widget-details="widgetDetails"
    :sentiment-diagram="authorsBySentimentValues"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import SentimentDiagram from '@/components/widgets/SentimentDiagram'

export default {
  name: 'AuthorsBySentimentWidget',
  components: {SentimentDiagram},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      authorsBySentiment: get.AUTHORS_BY_SENTIMENT,
    }),
    authorsBySentimentValues() {
      return this.authorsBySentiment.map((el) => el.author_count)
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
