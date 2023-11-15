<template>
  <div class="container">
    <VolumeWidget
      v-if="chartValues.length"
      v-bind="$attrs"
      :widget-details="widgetDetails"
      :labels="labels"
      :chart-values="chartValues"
    />
    <WidgetsSwitcher
      v-if="tabs.length"
      v-model="activeTab"
      :tabs="tabs"
      :isSentiment="true"
    />
  </div>
</template>

<script>
import {createNamespacedHelpers} from 'vuex'
import {get, action} from '@store/constants'
import {isAllFieldsEmpty} from '@lib/utilities'

import VolumeWidget from '@components/widgets/VolumeWidget'
import WidgetsSwitcher from '@components/layout/WidgetsSwitcher'

const {mapActions, mapGetters} = createNamespacedHelpers('online/widgets')

export default {
  name: 'AuthorsBySentimentWidget',
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
    authorsBySentiment() {
      return (
        this.widgetDetails.widgetData ||
        this.onlineWidgets.authorsBySentiment.data
      )
    },
    widgetId() {
      return this.onlineWidgets.authorsBySentiment.id
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
      return Object.keys(this.authorsBySentiment)
    },
    currentWidgetData() {
      return this.authorsBySentiment[this.activeTab]
    },
    labels() {
      if (!this.currentWidgetData) return []
      return this.currentWidgetData.map((el) => el[0].toString())
    },

    chartValues() {
      if (!this.currentWidgetData) return []
      return [
        {
          label: this.activeTab,
          data: this.currentWidgetData.map((el) => el[1]),
        },
      ]
    },
  },
  created() {
    const hasCurrentData =
      !isAllFieldsEmpty(this.authorsBySentiment) &&
      this.widgetId === this.widgetDetails.id

    if (!this.widgetDetails.widgetData && !hasCurrentData) {
      this[action.GET_AUTHORS_BY_SENTIMENT]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_SENTIMENT]),
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
