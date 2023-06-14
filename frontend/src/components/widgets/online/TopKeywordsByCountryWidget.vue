<template>
  <div class="container">
    <KeywordsWidget
      v-if="topKeywordsByCountryWidget.length"
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :keywords-values="currentWidgetData"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import KeywordsWidget from '@/components/widgets/KeywordsWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

export default {
  name: 'OnlineTopKeywordsByCountryWidget',
  components: {KeywordsWidget, WidgetsSwitcher},
  props: {
    widgetDetails: {type: Object, required: true},
  },
  data() {
    return {
      newActiveTab: '',
    }
  },
  computed: {
    ...mapState(['topKeywordsByCountryWidget']),
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    currentWidgetData() {
      return this.topKeywordsByCountryWidget.find((el) =>
        Object.keys(el).includes(this.activeTab)
      )[this.activeTab]
    },
    tabs() {
      return this.topKeywordsByCountryWidget.map((el) =>
        Object.keys(el).toString()
      )
    },
  },
  created() {
    if (!this.topKeywordsByCountryWidget.length) {
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

<style lang="scss" scoped>
.container {
  flex-direction: column;

  max-height: 450px;
  height: 100%;
}
</style>
