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

import KeywordsWidget from '@/components/widgets/KeywordsWidget'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'OnlineTopKeywordsWidget',
  components: {KeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topKeywords() {
      return this.socialWidgets.topKeywords
    },
  },
  created() {
    if (!this.topKeywords.length) {
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
