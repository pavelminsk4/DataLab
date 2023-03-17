<template>
  <KeywordsWidget
    v-if="topKeywords.length"
    :title="title"
    :chartType="chartType"
    :widget-id="widgetId"
    :is-widget="isWidget"
    :keywords-values="topKeywords"
  />
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@/components/widgets/KeywordsWidget'

export default {
  name: 'TopKeywordsWidget',
  components: {KeywordsWidget},
  props: {
    projectId: {type: Number, required: true},
    widgetId: {type: Number, required: true},
    title: {type: String, required: true},
    chartType: {type: String, required: true},
    isWidget: {type: Boolean, default: true},
  },
  computed: {
    ...mapGetters({
      topKeywords: get.TOP_KEYWORDS_WIDGET,
    }),
  },
  created() {
    if (!this.topKeywords.length) {
      this[action.GET_TOP_KEYWORDS_WIDGET]({
        projectId: this.projectId,
        widgetId: this.widgetId,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_KEYWORDS_WIDGET]),
  },
}
</script>

<style scoped></style>
