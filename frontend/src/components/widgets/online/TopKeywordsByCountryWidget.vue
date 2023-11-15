<template>
  <div class="container">
    <KeywordsWidget
      v-if="topKeywordsByCountryWidget.length"
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :keywords-values="currentWidgetData"
      :active-tab="activeTab"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@components/widgets/KeywordsWidget'
import WidgetsSwitcher from '@components/layout/WidgetsSwitcher'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

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
    ...mapGetters({
      onlineWidgets: get.ONLINE_WIDGETS,
    }),
    topKeywordsByCountryWidget() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.topKeywordsByCountryWidget.data
      )
    },
    widgetId() {
      return this.onlineWidgets.topKeywordsByCountryWidget?.id
    },
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    currentWidgetData() {
      const widgetData = this.topKeywordsByCountryWidget.find((el) =>
        Object.keys(el).includes(this.activeTab)
      )
      return widgetData[this.activeTab]
    },
    tabs() {
      return this.topKeywordsByCountryWidget.map((el) =>
        Object.keys(el).toString()
      )
    },
  },
  created() {
    const hasCurrentData =
      this.topKeywordsByCountryWidget.length &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
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
  align-items: center;

  width: 100%;
  max-height: 450px;
  height: 100%;
}
</style>
