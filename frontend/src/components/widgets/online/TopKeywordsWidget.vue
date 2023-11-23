<template>
  <KeywordsWidget
    v-if="topKeywords.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :keywords-values="topKeywords"
  />
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@components/widgets/KeywordsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'OnlineTopKeywordsWidget',
  components: {KeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topKeywords: get.TOP_KEYWORDS_WIDGET,
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topKeywords() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.topKeywordsWidget.data
      )
    },
    widgetId() {
      return this.onlineWidgets.topKeywordsWidget?.id
    },
  },
  created() {
    const hasCurrentData =
      this.topKeywords.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_TOP_KEYWORDS_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_KEYWORDS_WIDGET]),
  },
}
</script>
