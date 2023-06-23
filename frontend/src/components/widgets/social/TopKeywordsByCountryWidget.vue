<template>
  <div class="container">
    <KeywordsWidget
      v-if="topKeywordsByCountry.length"
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :keywords-values="currentWidgetData"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {action} from '@store/constants'

import KeywordsWidget from '@/components/widgets/KeywordsWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

const {mapActions, mapState} = createNamespacedHelpers('social/widgets')

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
    ...mapState(['topKeywordsByCountry']),
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    currentWidgetData() {
      const widgetData = this.topKeywordsByCountry.find((el) =>
        Object.keys(el).includes(this.activeTab)
      )
      return widgetData[this.activeTab]
    },
    tabs() {
      return this.topKeywordsByCountry.map((el) => Object.keys(el)[0])
    },
  },
  created() {
    this[action.GET_TOP_KEYWORDS_BY_COUNTRY_WIDGET]({
      projectId: this.widgetDetails.projectId,
      widgetId: this.widgetDetails.id,
    })
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
