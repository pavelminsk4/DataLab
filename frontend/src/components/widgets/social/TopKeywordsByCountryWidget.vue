<template>
  <div class="container">
    <KeywordsWidget
      v-if="topKeywordsByCountry.length"
      v-bind="$attrs"
      :active-tab="activeTab"
      :widget-details="widgetDetails"
      :keywords-values="currentWidgetData"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action, get} from '@store/constants'

import KeywordsWidget from '@components/widgets/KeywordsWidget'
import WidgetsSwitcher from '@components/layout/WidgetsSwitcher'

const {mapActions, mapGetters} = createNamespacedHelpers('social/widgets')

export default {
  name: 'SocialTopKeywordsByCountryWidget',
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
      socialWidgets: get.SOCIAL_WIDGETS,
    }),
    topKeywordsByCountry() {
      return (
        this.widgetDetails.widgetData ||
        this.socialWidgets.topKeywordsByCountry.data
      )
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
      const widgetData = this.topKeywordsByCountry.find((values) =>
        Object.keys(values).includes(this.activeTab)
      )
      return widgetData[this.activeTab]
    },
    tabs() {
      return this.topKeywordsByCountry.map((values) => Object.keys(values)[0])
    },
    widgetId() {
      return this.socialWidgets.topKeywordsByCountry?.id
    },
  },
  created() {
    const hasCurrentData =
      this.topKeywordsByCountry.length &&
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
