<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopAuthors"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {mapActions, mapGetters} from 'vuex'
import {isAllEmptyFields} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

export default {
  name: 'SentimentTop10AuthorsWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      sentimentTopAuthors: get.SENTIMENT_TOP_AUTHORS,
    }),
  },
  created() {
    if (isAllEmptyFields(this.sentimentTopAuthors)) {
      this[action.GET_SENTIMENT_TOP_AUTHORS]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_AUTHORS]),
  },
}
</script>
