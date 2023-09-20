<template>
  <div class="container">
    <VolumeWidget
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :labels="labels"
      :chart-values="chartValues"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'SourcesByCountryWidget',
  components: {VolumeWidget, WidgetsSwitcher},
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
    sourcesByCountry() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.sourcesByCountry.data
      )
    },
    widgetId() {
      return this.onlineWidgets.sourcesByCountry.id
    },
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    tabs() {
      return this.sourcesByCountry.map((el) => Object.keys(el).toString())
    },
    currentWidgetData() {
      return this.sourcesByCountry.find((el) =>
        Object.keys(el).includes(this.activeTab)
      )
    },
    labels() {
      if (!this.currentWidgetData) return []
      return this.currentWidgetData[this.activeTab].map((el) => el[0] + '')
    },

    chartValues() {
      if (!this.currentWidgetData) return []
      return [
        {
          label: this.activeTab,
          data: this.currentWidgetData[this.activeTab].map((el) => el[1]),
        },
      ]
    },
  },
  created() {
    const hasCurrentData =
      this.sourcesByCountry.length && this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_SOURCES_BY_COUNTRY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_SOURCES_BY_COUNTRY]),
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
