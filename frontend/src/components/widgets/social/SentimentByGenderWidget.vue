<template>
  <SentimentWidget
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :sentiment-widget-data="sentimentByGender"
  />
</template>

<script>
import {action, get} from '@store/constants'
import {createNamespacedHelpers} from 'vuex'
import {isAllFieldsEmpty} from '@lib/utilities'

import SentimentWidget from '@/components/widgets/SentimentWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SentimentSentimentByGender',
  components: {SentimentWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    sentimentByGender() {
      return (
        this.widgetDetails.widgetData || this.socialWidgets.sentimentByGender
      )
    },
  },
  created() {
    if (
      !this.widgetDetails.widgetData &&
      isAllFieldsEmpty(this.sentimentByGender)
    ) {
      this[action.GET_SENTIMENT_BY_GENDER]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SENTIMENT_BY_GENDER]),
  },
}
</script>
