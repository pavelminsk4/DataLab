<template>
  <div class="container">
    <KeywordsWidget
      v-if="topKeywords.length"
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :keywords-values="topKeywords"
    />
    <!-- <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" /> -->
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@/components/widgets/KeywordsWidget'
// import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

export default {
  name: 'OnlineTopKeywordsWidget',
  components: {KeywordsWidget},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  computed: {
    ...mapGetters({
      topKeywords: get.TOP_KEYWORDS_BY_COUNTRY_WIDGET,
    }),
  },
  created() {
    if (!this.topKeywords.length) {
      this[action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET]),
  },
}
</script>
