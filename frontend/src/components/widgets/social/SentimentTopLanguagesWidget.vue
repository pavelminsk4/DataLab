<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentTopLanguages"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllEmptyFields} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SentimentTop10LanguagesWidget',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentTopLanguages() {
      return this.socialWidgets.sentimentTopLanguages
    },
  },
  created() {
    if (isAllEmptyFields(this.sentimentTopLanguages)) {
      this[action.GET_SENTIMENT_TOP_LANGUAGES]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_TOP_LANGUAGES]),
  },
}
</script>
