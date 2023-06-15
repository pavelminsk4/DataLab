<template>
  <div class="container">
    <VolumeWidget
      v-bind="$attrs"
      v-if="chartValues.length"
      :widget-details="widgetDetails"
      :labels="labels"
      :chart-values="chartValues"
    />
    <WidgetsSwitcher v-if="tabs.length" v-model="activeTab" :tabs="tabs" />
  </div>
</template>

<script>
import {mapActions, mapState} from 'vuex'
import {action} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

export default {
  name: 'AuthorsByCountryWidget',
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
    ...mapState(['authorsByCountry']),
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    tabs() {
      return this.authorsByCountry.map((el) => Object.keys(el).toString())
    },
    currentWidgetData() {
      return this.authorsByCountry.find((el) =>
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
          data: this.currentWidgetData[this.activeTab].map((el) => el[1]),
        },
      ]
    },
  },
  created() {
    if (!this.authorsByCountry.length) {
      this[action.GET_AUTHORS_BY_COUNTRY]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_COUNTRY]),
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
