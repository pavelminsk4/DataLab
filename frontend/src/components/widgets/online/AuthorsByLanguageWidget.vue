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
import {mapActions, mapGetters} from 'vuex'
import {action, get} from '@store/constants'

import VolumeWidget from '@/components/widgets/VolumeWidget'
import WidgetsSwitcher from '@/components/layout/WidgetsSwitcher'

export default {
  name: 'AuthorsByLanguageWidget',
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
      authorsByLanguage: get.AUTHORS_BY_LANGUAGE,
    }),
    activeTab: {
      get() {
        return this.newActiveTab || this.tabs[0]
      },
      set(newTab) {
        this.newActiveTab = newTab
      },
    },
    tabs() {
      return this.authorsByLanguage.map((el) => Object.keys(el).toString())
    },
    currentWidgetData() {
      return this.authorsByLanguage.find((el) =>
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
    if (!this.authorsByLanguage.length) {
      this[action.GET_AUTHORS_BY_LANGUAGE]({
        projectId: this.widgetDetails.projectId,
        widgetId: this.widgetDetails.id,
      })
    }
  },
  methods: {
    ...mapActions([action.GET_AUTHORS_BY_LANGUAGE]),
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
