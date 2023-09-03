<template>
  <KeywordsWidget
    v-if="topKeywords.length"
    v-bind="$attrs"
    :widget-details="widgetDetails"
    :keywords-values="topKeywords"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@/components/widgets/KeywordsWidget'

export default {
  name: 'OnlineTopKeywordsWidget',
  components: {KeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topKeywords: get.TOP_KEYWORDS_WIDGET,
    }),
  },
  created() {
    // if (!this.topKeywords.length) {
    this[action.GET_TOP_KEYWORDS_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
    // }
  },
  methods: {
    ...mapActions([action.GET_TOP_KEYWORDS_WIDGET]),
  },
}
</script>
